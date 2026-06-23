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

## Risk & quản lý lệnh (ĐỀ XUẤT — sửa cho khớp bạn)
- Risk mỗi lệnh: **1%** tài khoản (giảm còn 0.5% khi tín hiệu yếu / ngược HTF bias).
- RR tối thiểu nhận lệnh: **1:2**. Scalp tối thiểu **1:1.5**.
- Chốt lời từng phần: TP1 ~1:1 (dời SL về BE) → TP2 1:2 → để runner nếu thuận HTF.
- Tối đa lệnh thua liên tiếp/ngày: **2** → nghỉ, tránh revenge_trade.
- Khung: bias D1/H4/H1 · đánh POI H4/H1 · vào lệnh M5 (xác nhận cấu trúc M15).

## Khung giờ ưu tiên (giờ VN, UTC+7 — ĐỀ XUẤT)
- **London open:** ~14:00–17:00 — phiên chính, ưu tiên cao nhất.
- **NY open / overlap London–NY:** ~19:00–23:00 — biến động mạnh, dễ FOMO, cẩn thận.
- **Asia:** ~07:00–14:00 — thường range; chủ yếu quan sát + đánh dấu thanh khoản (asia_high / asia_low).

> Các con số trên là mặc định hợp lý cho SMC, **KHÔNG phải luật gốc của bạn** — sửa lại cho đúng phong cách & kích thước tài khoản của bạn.
