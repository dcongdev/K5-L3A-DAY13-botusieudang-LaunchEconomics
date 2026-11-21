# Bảng chi phí · Nhiệm vụ A và B

Nhóm botusieudang · L3A · Trợ lý hoàn phí LogiX-VN
Nguồn số: `cd src && python3 lab13.py` trên `logix_runs.csv` (1.624 lần chạy) và `logix_requests.csv` (1.200 yêu cầu). Toàn bộ dữ liệu là giả lập; số nào tính từ cột `*_simulated` ghi nhãn **[simulated]**.

## A1 · Ba phép thử đáp án biết trước (p = 0,8)

| Phép thử | Kết quả code | Đáp án | Trạng thái |
|---|---|---|---|
| Số lần chạy trung bình, tối đa 2 lần | 1,20 | 1,20 | ĐẠT |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 | 1,25 | ĐẠT |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 | 1,25 | ĐẠT (= 1/p, k triệt tiêu) |

## A2 · Chi phí mỗi việc thành công, tính từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
|---|---:|---|---|
| Token (mọi lần chạy, kể cả lỗi) | 245.585 | logix_runs.csv | đo từ trace |
| Tool (5.600 lần gọi × 15 đ) | 84.000 | logix_runs.csv | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt > 1 | đo từ trace |
| Xem lại (890 phút × 2.000 đ) | 1.780.000 | phut_xem_lai_simulated | simulated |
| Làm lại (1.132 phút × 2.000 đ) | 2.264.000 | phut_lam_lai_simulated | simulated |
| Tổng chi phí | 4.373.585 | | có phần simulated |
| Số việc thành công | 978 | ket_qua = thanh_cong | |
| **Chi phí mỗi việc thành công** | **4.472** | 4.373.585 ÷ 978 | simulated |
| Hoá đơn token + tool chia số yêu cầu | 274,7 | 329.585 ÷ 1.200 | đo từ trace |

1. Chi phí mỗi việc thành công **4.472 đ [simulated]** gấp **16,3 lần** "hoá đơn chia số yêu cầu" (274,7 đ).
2. Khoản lớn nhất là **làm lại: 51,8%** tổng chi phí [simulated], tiếp theo xem lại 40,7% [simulated]; giờ nhân viên chiếm 92,5% [simulated]. Token chỉ 5,6%, tool 1,9%.

**Lưu ý khi so với 12.000 đ.** 4.472 đ chỉ chia cho việc trợ lý làm xong, chưa tính 222 yêu cầu không thành công (148 chuyen_nhan_vien + 74 lam_lai) mà nhân viên phải làm thay. Chi phí cả hệ thống mỗi yêu cầu = (4.373.585 + 222 × 12.000) ÷ 1.200 = **5.865 đ = 0,49× của 12.000 đ** [simulated]. Đây là con số dùng khi so với nhân viên tự làm, không phải 0,37×.

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Lần chạy / yêu cầu | Chi phí mỗi việc thành công [simulated] | So với 12.000 đ [simulated] |
|---|---:|---:|---:|---:|---:|
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ | **1,88×** |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ | 0,85× |
| *Phạm vi pilot: noi_dia + hang_nang* | *982* | *91,6%* | *1,17* | *3.414 đ* | *0,28×* |

Tỉ lệ `status = ok` theo từng lần thử (đo từ trace):

| Loại | Lần 1 | Lần 2 | Lần 3 |
|---|---:|---:|---:|
| noi_dia | 91,0% (n=824) | 75,7% (n=74) | 38,9% (n=18) |
| hang_nang | 70,9% (n=158) | 39,1% (n=46) | 17,9% (n=28) |
| quoc_te | 30,0% (n=150) | 11,4% (n=105) | 2,2% (n=93) |
| doi_tac | 51,5% (n=68) | 18,2% (n=33) | 14,8% (n=27) |

**Kết luận A3.** quoc_te không đáng để trợ lý xử lý: 1,88× chi phí nhân viên tự làm [simulated], chỉ 27,3% thành công dù chạy trung bình 2,32 lần. Chạy lại không giúp: lần 2 chỉ đúng 11,4%, lần 3 chỉ 2,2% — lỗi lặp lại trên cùng yêu cầu, chạy lại chỉ tốn thêm tiền. doi_tac sát ngưỡng (0,85× [simulated], 54,4% thành công) và có điều khoản riêng nên cũng loại khỏi phạm vi pilot.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

Chi phí mỗi việc thành công trong phạm vi = 3.072.513 ÷ 900 = 3.414 đ [simulated]. Số việc thành công mỗi tháng = 45.000 × 900 ÷ 1.200.

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định [simulated] | So với 12.000 đ [simulated] |
|---|---:|---:|---:|---:|
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | **4.599 đ** | **0,38×** |
| Một nửa khối lượng (ví dụ giai đoạn pilot) | 16.875 | 2.370 đ | 5.784 đ | 0,48× |

- Chi phí cố định **không đổi kết luận** ở quy mô đầy đủ (0,38× [simulated]), nhưng tăng gấp đôi khi khối lượng giảm một nửa (+2.370 đ/việc); ở pilot 50% nhân viên, khối lượng qua trợ lý còn nhỏ hơn nên hồ sơ phải ghi rõ số đã cộng cố định hay chưa, ở khối lượng nào.

## B1 · Bảng độ nhạy (đổi từng yếu tố)

| Kịch bản | Cách tính | Chi phí mỗi việc thành công [simulated] | Thay đổi |
|---|---|---:|---:|
| Gốc (A2) | | 4.472 đ | |
| Giá token gấp đôi | 52 đ và 260 đ / 1.000 token; tool giữ nguyên | 4.723 đ | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ | **+51,8%** |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ / phút | 5.506 đ | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ attempt > 2; yêu cầu có so_lan_chay > 2 → chuyen_nhan_vien, phút = 0 | 4.237 đ | −5,2% |
| Chỉ cho chạy 1 lần | Bỏ attempt > 1; tương tự | 4.111 đ | −8,1% |

Tự kiểm tra: mỗi kịch bản "giảm một nửa" giảm đúng bằng nửa mức tăng của "gấp đôi" (5,6 → 2,8; 40,7 → 20,3; 51,8 → 25,9) vì mô hình tuyến tính.

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi **và** xem lại gấp đôi: **6.543 đ (+46,3%) [simulated]** = 5,6% + 40,7%, đúng bằng tổng hai tác động riêng (mô hình cộng tuyến tính).
- **Xếp hạng ba yếu tố nhạy nhất: 1. số ca làm lại (+51,8%) · 2. tỉ lệ xem lại (+40,7%) · 3. lương nhân viên (+23,1%)** [simulated]. Giá token xếp sau cùng (+5,6%) → pilot phải theo dõi tỉ lệ làm lại và tỉ lệ xem lại, không phải giá token.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn?

Chi phí cả hệ thống = tổng chi phí trợ lý + 12.000 đ × số yêu cầu không thành công (nhân viên làm thay).

| Giới hạn | Tổng trợ lý [simulated] | Không thành công | Cả hệ thống [simulated] | Chi phí mỗi việc thành công [simulated] |
|---|---:|---:|---:|---:|
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | 4.111 đ (thấp nhất) |
| 2 lần | 4.093.220 đ | 234 | **6.901.220 đ (rẻ nhất)** | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

**Trả lời B3.** Giới hạn **2 lần** rẻ nhất cho công ty (6.901.220 đ [simulated], rẻ hơn 3 lần 136.365 đ và hơn 1 lần 548.561 đ). Nó **không trùng** với giới hạn có chi phí mỗi việc thành công thấp nhất (1 lần, 4.111 đ): tối ưu riêng chỉ số đó sẽ đẩy thêm 85 việc (319 − 234) sang nhân viên.

## B4 · Nếu tuần đầu phải xem lại tất cả (phạm vi noi_dia + hang_nang, 982 yêu cầu)

| Bước | Tính | Số tiền [simulated] |
|---|---|---:|
| Xem lại mọi yêu cầu có ≥ 1 lần chạy ok | 948 × 5 phút × 2.000 đ | 9.480.000 đ |
| Làm lại các ca sai bị bắt trước khi gửi | 48 × 9 phút × 2.000 đ | 864.000 đ |
| Token + tool mọi lần chạy của 982 yêu cầu | đo từ trace | 224.513 đ |
| Tổng | | 10.568.513 đ |
| **Chi phí mỗi việc thành công** | ÷ 900 việc thành công | **11.743 đ = 0,98× của 12.000 đ** |

**Độ nhạy theo phút làm lại.** Đề giả định 9 phút/ca, nhưng cột `phut_lam_lai_simulated` trung bình **15,3 phút/ca** (trung vị 14,5) trên 74 ca lam_lai. Thay 9 bằng 15,3: 48 × 15,3 × 2.000 = 1.468.800 đ → tổng 11.173.313 đ → **12.415 đ = 1,03×** [simulated], tức xem lại 100% còn **đắt hơn** nhân viên tự làm. Mức hoà vốn: mỗi lần xem lại phải **≤ 5,1 phút** (làm lại 9 phút) hoặc **≤ 4,8 phút** (làm lại 15,3 phút) [simulated].

**Trả lời B4.** Xem lại 100% thì trợ lý không tiết kiệm được gì: 0,98× (1,03× với phút làm lại thật) [simulated], vì tiền xem lại chiếm 90% chi phí. Pilot phải học được tỉ lệ xem lại có thể giảm an toàn xuống mức nào, và mỗi lần xem lại có xuống dưới ~4,8 phút được không.
