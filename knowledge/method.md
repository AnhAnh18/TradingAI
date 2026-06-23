# Phương pháp — SMC + Volume Profile

> File sống. Sửa theo đúng cách BẠN giao dịch. AI đọc file này để hiểu "gu" của bạn
> trước khi viết plan/session hay đưa nhận định.

## Triết lý lõi
Plan → Thị trường thực sự làm gì → Mình phản ứng → Kết quả → Bài học.
Không đoán bừa: **chờ giá tới zone rồi mới quyết định.**

## Quy trình

### 1. HTF bias (D1 → H4 → H1)
- Xác định xu hướng & cấu trúc: HH-HL / LH-LL, BOS (phá cấu trúc), CHoCH (đổi tính chất).
- Ghi `regime`: trend hay range.

### 2. Đánh dấu zone quan trọng (POI)
- Supply / Demand từ cấu trúc HTF + Volume Profile (POC, VAH/VAL).
- Mỗi zone ghi rõ `origin` (vì sao là zone) + `tf` + `strength`.

### 3. Lọc zone (giữ cái mạnh)
- **Confluence**: nhiều yếu tố trùng (vd swing_low + round_number + volume_poc).
- Khung lớn > khung nhỏ. Zone HTF chưa test > zone đã test nhiều lần.

### 4. Chờ phản ứng tại zone (LTF: M15 / M5)
- Xác nhận cần có: **quét thanh khoản (sweep) + MSS** đúng hướng.
- Vào theo entry model: `ob_retest` / `fvg_fill` / `sweep_reclaim`...

### 5. Gồng hay không?
- **Gồng** khi: thuận HTF bias + cấu trúc LTF chưa gãy + chưa chạm zone đối diện.
- **Cắt / giảm** khi: MSS ngược hướng, hoặc giá đâm vào zone đối diện mạnh.

## Luật tránh (mặc định)
- Không vào **giữa range** → `entered_mid_range`
- Chưa có **MSS** thì không vào → `no_mss`
- Tránh **FOMO** lúc NY open → `fomo`

## (Bạn bổ sung — để AI áp đúng luật của bạn)
- Risk mỗi lệnh: ____ %
- RR tối thiểu nhận lệnh: ____
- Khung vào lệnh ưu tiên: ____
- Khung giờ giao dịch trong ngày: ____
