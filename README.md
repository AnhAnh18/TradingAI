# TradingAI — Plan • Session • Lesson

Hệ thống ghi chép giao dịch có cấu trúc cho XAUUSD (SMC + Volume Profile),
để sau N ngày có thể tra cứu: **setup nào tốt, zone nào phản ứng, mình hay sai ở đâu.**

## Vòng lặp mỗi ngày

1. **Plan (trước phiên)** — `plans/YYYY-MM-DD.yaml`: bias HTF + các zone quan trọng + kịch bản kỳ vọng.
2. **Session (trong phiên)** — `sessions/YYYY-MM-DD_<session>.yaml`: thị trường thực sự làm gì, mình vào lệnh ra sao, kết quả.
3. **Lesson (sau phiên)** — thêm 1 dòng vào `lessons/lessons.md`.

> Quy trình mong muốn: bạn chỉ gửi **ảnh chart + bias trong đầu + vài câu note**.
> AI viết/cập nhật file YAML theo đúng từ vựng chuẩn trong [`knowledge/vocab.md`](knowledge/vocab.md).

## Thư mục

| Đường dẫn | Vai trò |
|---|---|
| `knowledge/vocab.md` | Từ vựng chuẩn (enum). **Đọc & tuân theo TRƯỚC khi ghi.** |
| `knowledge/method.md` | Phương pháp SMC + Volume Profile theo lời bạn |
| `plans/` | Kế hoạch từng ngày |
| `sessions/` | Nhật ký từng phiên (có kết quả để tính thống kê) |
| `lessons/lessons.md` | Bài học, append-only |
| `scripts/analyze.py` | Tính winrate / RR / breakdown từ `sessions/` |
| `knowledge/htf_zones.yaml` | Bản đồ vùng khung lớn (D1/H4) — đối chiếu để biết cản M15 nào mạnh |
| `scripts/fetch_telegram.py` | Kéo plan từ bot Telegram → `cloud_inbox/` (cloud) hoặc `inbox/` (local) |
| `.github/workflows/fetch.yml` | Cloud cron: tự kéo plan mỗi ~15' (không cần treo máy) |

## Phân vai: SỐ vs DIỄN GIẢI (quan trọng)

- **`analyze.py` lo phần SỐ** — winrate, RR, breakdown. Deterministic, đáng tin, tái lập được.
- **AI lo phần DIỄN GIẢI** — đọc pattern định tính, gợi ý chỉnh method.
- AI **không** tự nhẩm thống kê qua hàng trăm file (dễ sai). Muốn số → luôn chạy script.

## Sự thật về thống kê (đọc 1 lần)

- Mọi con số in kèm **n (cỡ mẫu)**. `n < 30` ⇒ chỉ là cảm giác, chưa đáng tin.
- Buckets nhân nhanh (setup × zone × phiên) ⇒ stats chia nhỏ cần nhiều tháng dữ liệu.
- Gắn `regime` (trend/range) để khỏi trung bình cộng hai chế độ thị trường khác nhau.
- **Log trung thực cả lệnh THUA và setup BỎ QUA** — chỉ ghi ngày đẹp thì database sẽ nói dối bạn.

## Chạy thống kê

```bash
pip install pyyaml
python scripts/analyze.py
```
