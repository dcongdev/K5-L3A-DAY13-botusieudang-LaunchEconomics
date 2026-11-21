# Bảng lỗi và cách khắc phục · Nhiệm vụ C

Nhóm botusieudang · L3A. 20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo **nguyên nhân gốc**, không theo chỗ cần sửa.

| Loại | Câu hỏi để nhận ra |
|---|---|
| Do người dùng | Đầu vào hoặc lựa chọn của khách có sai không? |
| Hệ thống | Trợ lý làm sai so với thiết kế/chính sách, và sai đó đã lộ ra (khách, nhân viên hoặc log thấy)? |
| Ngữ cảnh | Kết quả đúng thiết kế/chính sách, chỉ giả định của hệ thống không khớp hoàn cảnh khách? |
| Giới hạn hệ thống | Trợ lý không thể làm được dù cố: thiếu dữ liệu, ngoài phạm vi, dạng đầu vào không xử lý được? |
| Ngầm | Có sai (về tiền hoặc chi phí) nhưng không ai nhận ra cho tới khi kiểm tra mẫu/đối soát? |

## Hai bộ nhãn độc lập

Người gắn nhãn 1: ... · Người gắn nhãn 2: ... (gắn trong 8 phút, không trao đổi; điền cột của mình trước khi xem cột người kia)

| Ca | Tóm tắt | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- | --- |
| 1 | Khách nhập thiếu 2 chữ số tài khoản, ngân hàng trả lỗi | ... | ... | ... | ... |
| 2 | Gọi tool bảng giá với tham số hàng thường cho kiện 28 kg, hoàn thiếu 45.000 đ | ... | ... | ... | ... |
| 3 | Hoàn về ví LogiX đúng thiết kế, khách chờ tiền về ngân hàng | ... | ... | ... | ... |
| 4 | Chặng do hãng nước ngoài giao, LogiX không có dữ liệu | ... | ... | ... | ... |
| 5 | 14 đơn có mã giảm giá bị hoàn theo giá trước giảm, không ai báo | ... | ... | ... | ... |
| 6 | Khách chọn mục "giao trễ" nhưng hàng bị vỡ | ... | ... | ... | ... |
| 7 | API sổ cái 503, trợ lý vẫn báo "đã hoàn thành công" | ... | ... | ... | ... |
| 8 | Dẫn "Điều 7.2" không tồn tại, số tiền vẫn đúng | ... | ... | ... | ... |
| 9 | Khách nhập mã đơn sàn TMĐT thay vì mã vận đơn | ... | ... | ... | ... |
| 10 | Từ chối hoàn do bão đúng chính sách, app vẫn hiện "cam kết 24 giờ" | ... | ... | ... | ... |
| 11 | Tin nhắn thoại 40 giây, trợ lý không xử lý âm thanh | ... | ... | ... | ... |
| 12 | Tool D05 thiếu trường, token D05 gấp 3 lần suốt 3 tuần, không ai thấy | ... | ... | ... | ... |
| 13 | Hỏi hoàn phí bảo hiểm (ngoài phạm vi), trợ lý trả lời chung chung | ... | ... | ... | ... |
| 14 | Khách bấm nhầm "Xác nhận đã nhận tiền" | ... | ... | ... | ... |
| 15 | Trễ 26 giờ, trợ lý tính hoàn 100% thay vì 50%, nhân viên bắt được | ... | ... | ... | ... |
| 16 | Gửi Zalo lúc 2:14 sáng theo thiết kế "gửi ngay" | ... | ... | ... | ... |
| 17 | Bảng giá cũ trong bộ nhớ đệm, lệch 1.000–2.000 đ × 212 đơn, không ai mở lại | ... | ... | ... | ... |
| 18 | Hoàn đúng 15.000 đ nhưng không ghi cách tính, khách mở lại | ... | ... | ... | ... |
| 19 | Đơn 14 tháng trước, trợ lý chỉ truy cập 12 tháng, chuyển nhân viên | ... | ... | ... | ... |
| 20 | Khách gửi lại sau 10 phút, hoàn 2 lần vì thiếu khoá chống trùng | ... | ... | ... | ... |

**Tỉ lệ đồng thuận:** ... / 20 = ...%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% (dưới 16/20) thì ghi định nghĩa đã viết lại trước khi đi tiếp.

- ...

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện đo được (event, ngưỡng, tần suất); người phụ trách là một vai trò. Nếu nhãn thống nhất của nhóm cho 5 ca này khác cột "Loại lỗi", sửa lại cho khớp.

| Ca | Loại lỗi | Phát hiện bằng gì (đo được) | Khắc phục thế nào | Ai phụ trách |
|---:|---|---|---|---|
| 9 | Do người dùng | Event `input_validation_failed` (reason = `ma_khong_hop_le`, kèm trace_id); cảnh báo khi > 2% số yêu cầu/ngày | Nhận diện định dạng mã đơn sàn TMĐT và tự tra sang mã vận đơn; không tra được thì hiện hướng dẫn kèm ảnh chỗ lấy mã vận đơn | PM trợ lý hoàn phí |
| 7 | Hệ thống | Job đối soát mỗi giờ: tin nhắn "đã hoàn" không có bản ghi `refund_ledger_write` status = ok cùng trace_id; ngưỡng **0 ca** (1 ca là báo động) | Chỉ được báo "đã hoàn" khi sổ cái trả ok; 503 sau 3 lần thử thì báo "đang xử lý" và `handoff_to_staff`; thêm idempotency key (đồng thời chặn ca 20) | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Tỉ lệ `ticket_reopened` với reason = `so_tien` mà kiểm tra thấy số tiền đúng, theo tuần; ngưỡng > 1% số yêu cầu đã đóng | Mẫu tin nhắn luôn ghi cách tính: "Phí giao 30.000 đ × 50% (trễ 24–48 giờ) = 15.000 đ", kèm link điều khoản | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với reason = `thieu_du_lieu`, theo dõi theo loại yêu cầu mỗi tuần | Giữ cách chuyển nhân viên kèm tóm tắt và nói rõ lý do; đưa quoc_te ra khỏi phạm vi pilot (A3: 1,88× [simulated], 27,3% thành công) | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra mẫu 100 đơn/tuần (`audit_sample_checked`) so với bảng giá hiện hành; ngưỡng > 1% đơn lệch tiền | Xoá bộ nhớ đệm khi có bảng giá mới; ghi `phien_ban_bang_gia` vào mỗi trace để truy được đơn bị ảnh hưởng | Kế toán trưởng |
