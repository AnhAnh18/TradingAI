#!/usr/bin/env python3
"""
TradingAI - fetch_telegram.py
Kéo tin (plan) bạn forward vào BOT TELEGRAM CỦA BẠN về thư mục inbox/.

Cách hoạt động:
  - Bạn tạo bot riêng qua @BotFather -> có token.
  - Bạn forward/gửi plan (text hoặc ảnh) cho bot đó.
  - Script gọi Telegram Bot API (getUpdates) -> lưu tin mới vào inbox/.
  - Sau đó AI đọc inbox/ để dựng plan YAML.

Token (BÍ MẬT - đừng commit):
  - đặt env TELEGRAM_BOT_TOKEN, hoặc
  - tạo file secrets/telegram_token.txt chứa token (đã .gitignore).

Chỉ dùng thư viện chuẩn (urllib, json) - KHÔNG cần pip install.

Dùng:
    python scripts/fetch_telegram.py
"""
from __future__ import annotations

import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

# Windows console cp1252 -> ép UTF-8 để in tiếng Việt
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
INBOX = ROOT / "inbox"
SECRETS = ROOT / "secrets"
OFFSET_FILE = INBOX / ".offset"
API = "https://api.telegram.org"


def get_token() -> str:
    tok = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
    if tok:
        return tok
    f = SECRETS / "telegram_token.txt"
    if f.exists():
        return f.read_text(encoding="utf-8").strip()
    print("Chưa có token. Đặt env TELEGRAM_BOT_TOKEN hoặc tạo secrets/telegram_token.txt")
    sys.exit(1)


def api_call(token: str, method: str, **params):
    url = f"{API}/bot{token}/{method}"
    if params:
        url += "?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url, timeout=40) as r:
        data = json.loads(r.read().decode("utf-8"))
    if not data.get("ok"):
        raise RuntimeError(f"Telegram API lỗi: {data}")
    return data["result"]


def read_offset() -> int:
    if OFFSET_FILE.exists():
        try:
            return int(OFFSET_FILE.read_text().strip())
        except ValueError:
            return 0
    return 0


def download_file(token: str, file_id: str, dest: Path):
    info = api_call(token, "getFile", file_id=file_id)
    url = f"{API}/file/bot{token}/{info['file_path']}"
    with urllib.request.urlopen(url, timeout=60) as r:
        dest.write_bytes(r.read())


def main():
    INBOX.mkdir(exist_ok=True)
    token = get_token()
    offset = read_offset()

    try:
        updates = api_call(token, "getUpdates", offset=offset + 1, timeout=10)
    except urllib.error.URLError as e:
        print(f"Không gọi được Telegram API: {e}")
        sys.exit(1)

    if not updates:
        print("Không có tin mới.")
        return

    saved = 0
    for u in updates:
        offset = max(offset, u["update_id"])
        msg = u.get("message") or u.get("channel_post")
        if not msg:
            continue
        ts = time.strftime("%Y-%m-%d_%H%M%S", time.localtime(msg.get("date", time.time())))
        stamp = f"{ts}_{u['update_id']}"

        text = msg.get("text") or msg.get("caption")
        if text:
            (INBOX / f"{stamp}.txt").write_text(text, encoding="utf-8")
            saved += 1
        if "photo" in msg:
            try:
                download_file(token, msg["photo"][-1]["file_id"], INBOX / f"{stamp}.jpg")
                saved += 1
            except Exception as e:  # noqa: BLE001
                print(f"[WARN] tải ảnh lỗi: {e}")
        if "document" in msg:
            doc = msg["document"]
            name = doc.get("file_name", "file.bin")
            try:
                download_file(token, doc["file_id"], INBOX / f"{stamp}_{name}")
                saved += 1
            except Exception as e:  # noqa: BLE001
                print(f"[WARN] tải file lỗi: {e}")

    OFFSET_FILE.write_text(str(offset), encoding="utf-8")
    print(f"Đã lưu {saved} mục mới vào inbox/ (offset={offset}).")
    print("Bước tiếp: bảo AI 'đọc inbox' để dựng plan YAML.")


if __name__ == "__main__":
    main()
