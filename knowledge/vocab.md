# Từ vựng chuẩn (Controlled Vocabulary)

> Mọi file YAML PHẢI dùng đúng các giá trị dưới đây.
> Sai chính tả / dùng biến thể = stats thành rác.
> Cần giá trị mới? Thêm vào đây TRƯỚC, rồi mới dùng trong plan/session.

## bias / mss / bos / choch
`bullish` · `bearish` · `neutral` · `none`

## regime (chế độ thị trường)
`trending_up` · `trending_down` · `ranging`

## timeframe
`d1` · `h4` · `h1` · `m30` · `m15` · `m5` · `m1`
- HTF = d1, h4 · MTF = h1 · LTF = m15, m5

## session (phiên)
`asia` · `london` · `ny_am` · `ny_pm`

## zone.type (loại POI)
`supply` · `demand`

## zone.origin (vì sao là zone — trả lời câu "tại sao")
`swing_high` · `swing_low` · `order_block` · `fvg` ·
`volume_poc` · `value_area_high` · `value_area_low` ·
`range_high` · `range_low` · `round_number` ·
`previous_day_high` · `previous_day_low`
> Ghép nhiều yếu tố bằng " + ", vd: `swing_low + round_number`.

## zone.strength
`weak` · `medium` · `strong`

## liquidity (thanh khoản bị quét)
`asia_high` · `asia_low` · `pdh` · `pdl` ·
`session_high` · `session_low` · `equal_highs` · `equal_lows`

## entry.model (mô hình vào lệnh)
`ob_retest` · `fvg_fill` · `sweep_reclaim` · `breaker` · `range_fade`

## decision
`buy` · `sell` · `scalp_buy` · `scalp_sell` · `wait` · `no_trade`

## result
`tp1` · `tp2` · `tp3` · `partial` · `be` · `sl` · `no_trade`
- WIN = tp1/tp2/tp3 · LOSS = sl · BE = be · bỏ khỏi stats = no_trade

## mistakes (gắn thẻ lỗi — list, rỗng nếu không có)
`entered_mid_range` · `no_mss` · `fomo` · `early_entry` ·
`moved_sl` · `overleveraged` · `revenge_trade` ·
`against_htf_bias` · `no_confirmation`
