#!/usr/bin/env python3
"""
TradingAI - analyze.py
Đọc toàn bộ file YAML trong sessions/ rồi in thống kê.

Phần SỐ do script tính (deterministic, đáng tin).
Phần DIỄN GIẢI pattern để AI / người đọc làm.

Dùng:
    python scripts/analyze.py
Yêu cầu:
    pip install pyyaml
"""
from __future__ import annotations

import sys
from pathlib import Path
from collections import Counter, defaultdict

# Windows console mặc định cp1252 -> ép UTF-8 để in được tiếng Việt
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

try:
    import yaml
except ImportError:
    print("Thiếu thư viện PyYAML. Cài bằng:  pip install pyyaml")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
SESSIONS = ROOT / "sessions"

WIN = {"tp1", "tp2", "tp3"}
LOSS = {"sl"}
BE = {"be"}
SKIP_RESULT = {"no_trade", "pending", None, ""}

MIN_SAMPLE = 30


def load_sessions():
    rows = []
    for f in sorted(SESSIONS.glob("*.yaml")):
        if f.name.startswith("_"):          # bỏ qua template
            continue
        try:
            data = yaml.safe_load(f.read_text(encoding="utf-8"))
        except Exception as e:               # noqa: BLE001
            print(f"[WARN] Lỗi đọc {f.name}: {e}")
            continue
        if not data:
            continue
        data["_file"] = f.name
        rows.append(data)
    return rows


def pct(n, d):
    return f"{100 * n / d:.0f}%" if d else "n/a"


def flag(n):
    return "  ⚠ mẫu nhỏ" if n < MIN_SAMPLE else ""


def breakdown(traded, key, label):
    groups = defaultdict(list)
    for r in traded:
        if key == "model":
            v = (r.get("entry") or {}).get("model")
        else:
            v = r.get(key)
        if v:
            groups[v].append(r)
    if not groups:
        return
    print(f"\n— Theo {label} —")
    for k, g in sorted(groups.items(), key=lambda x: -len(x[1])):
        w = sum(1 for r in g if r.get("result") in WIN)
        l = sum(1 for r in g if r.get("result") in LOSS)
        print(f"  {k:<22} winrate {pct(w, w + l):>4}  (W:{w} L:{l}, n={len(g)}){flag(len(g))}")


def main():
    rows = load_sessions()
    excluded = [r for r in rows if r.get("exclude_from_stats")]
    traded = [r for r in rows
              if r.get("result") not in SKIP_RESULT and not r.get("exclude_from_stats")]
    n = len(traded)

    print("=" * 52)
    print("TradingAI — Thống kê (số do script tính)")
    print("=" * 52)
    print(f"Tổng phiên ghi nhận : {len(rows)}")
    print(f"Tổng lệnh có kết quả : {n}")
    if excluded:
        print(f"(Bỏ khỏi thống kê — lệnh test: {len(excluded)})")

    if n == 0:
        print("\nChưa có lệnh nào để tính. Hãy điền vào sessions/.")
        return

    wins = sum(1 for r in traded if r.get("result") in WIN)
    losses = sum(1 for r in traded if r.get("result") in LOSS)
    bes = sum(1 for r in traded if r.get("result") in BE)
    print(f"\nWinrate (loại BE) : {pct(wins, wins + losses)}"
          f"  — W:{wins} L:{losses} BE:{bes}, tổng {n}{flag(n)}")

    rrs = [r["rr"] for r in traded if isinstance(r.get("rr"), (int, float))]
    if rrs:
        print(f"Avg RR            : {sum(rrs) / len(rrs):.2f}  (n={len(rrs)})")

    breakdown(traded, "model", "entry model")
    breakdown(traded, "session", "phiên")

    mistakes = Counter()
    for r in traded:
        for m in (r.get("mistakes") or []):
            mistakes[m] += 1
    if mistakes:
        print("\n— Lỗi hay gặp —")
        for m, c in mistakes.most_common():
            print(f"  {m:<22} {c} lần")

    print(f"\nGhi chú: n < {MIN_SAMPLE} ⇒ chỉ là cảm giác, chưa đáng tin.")
    print("Diễn giải pattern: để AI / bạn đọc, đừng để script 'kết luận'.")


if __name__ == "__main__":
    main()
