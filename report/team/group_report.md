# Báo cáo nhóm

Báo cáo ngắn. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính. Số có nhãn [simulated] tính từ cột `*_simulated`.

## 1. Thông tin nhóm

- Tên nhóm: botusieudang
- Lớp: L3A
- Repo: `K5-L3A-DAY13-botusieudang-LaunchEconomics`
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Dựng hồ sơ launch v0 cho trợ lý hoàn phí LogiX-VN để hội đồng Gate 2a quyết định có mở pilot không. Cách tiếp cận: mọi con số tính bằng `src/lab13.py` từ trace (1.624 lần chạy, 1.200 yêu cầu); tính chi phí trên **mỗi việc thành công** (tử số gồm mọi lần chạy kể cả lỗi và giờ nhân viên), rồi dùng bảng độ nhạy để chọn chỉ số cần theo dõi và thiết kế pilot có đối chứng.

## 3. Giải pháp

| Nhiệm vụ | Cách làm | File |
|---|---|---|
| A · Chi phí | Ba hàm A1 qua 3 phép thử; `mo_hinh()` có tham số giá/hệ số/giới hạn chạy; tách theo `loai`; tỉ lệ ok theo lần thử; cộng chi phí cố định (A4) | [bang_chi_phi.md](bang_chi_phi.md) |
| B · Độ nhạy | Gọi lại `mo_hinh()` cho 9 kịch bản, 1 cặp, giới hạn 1/2/3 lần (chi phí cả hệ thống), xem lại 100% kèm độ nhạy phút làm lại | [bang_chi_phi.md](bang_chi_phi.md) |
| C · Lỗi | Hai người gắn nhãn độc lập 20 ca theo Google PAIR, so nhãn, bảng khắc phục 5 ca có event + ngưỡng + vai trò | [bang_loi.md](bang_loi.md) |
| D · Pilot | Tính 5 câu D1 trước, rồi chọn chia theo nhân viên 20 + 20 với MDE 6 điểm; luật an toàn đặt theo tỉ lệ mở lại hiện tại | [pilot_plan.yaml](pilot_plan.yaml) |
| E · Hồ sơ | Ba chỉ số tính thử + 3 chỉ số đề xuất, 10 event có trace_id, 6 dòng rủi ro kinh tế, hồ sơ 7 mục | [chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md) |

## 4. Kết quả

- Chi phí mỗi việc thành công **4.472 đ** [simulated], gấp **16,3×** hoá đơn token chia số yêu cầu (274,7 đ); giờ nhân viên chiếm 92,5% [simulated].
- So với 12.000 đ theo chi phí cả hệ thống: **5.865 đ/yêu cầu = 0,49×** [simulated]. Phạm vi noi_dia + hang_nang cộng cố định 40 triệu/tháng: **4.599 đ = 0,38×** [simulated].
- quoc_te **1,88×** [simulated], chạy lại không giúp (lần 3 chỉ đúng 2,2%) → loại khỏi pilot; doi_tac 0,85× → loại.
- Ba yếu tố nhạy nhất: làm lại (+51,8%), xem lại (+40,7%), lương (+23,1%) [simulated]; giá token chỉ +5,6%.
- Giới hạn 2 lần chạy rẻ nhất cho cả hệ thống (6.901.220 đ) [simulated]. Xem lại 100%: **0,98×**, hoặc **1,03×** với phút làm lại thật [simulated] → không tiết kiệm.
- Pilot: chia theo nhân viên 20 + 20, n = 859/nhóm, m ≥ 299, DE 6,96; power 0,64 nếu tác động thật chỉ 5 điểm.
- Chỉ số đợt chạy thử: chính 82,83%, bỏ qua gợi ý 27,12%, mở lại 7 ngày 4,25%.
- **Đề xuất: Go có điều kiện** (xem `ho_so_launch_v0.md`).
- Kết quả duyệt chéo nhận từ hội đồng: ...

## 5. Khó khăn và cách xử lý

- Ô trống ở `quyet_dinh_xem_lai` bị đọc thành NaN → đọc CSV với `keep_default_na=False`.
- So sánh với 12.000 đ dễ sai nếu dùng 4.472 ÷ 12.000 = 0,37× → dùng chi phí cả hệ thống (cộng 222 yêu cầu nhân viên làm thay) = 0,49×.
- 40 nhân viên không đủ mẫu cho mức chênh 5 điểm với mọi cách chia theo cụm → chấp nhận MDE 6 điểm, nêu power 0,64.
- Ngưỡng mở lại tuyệt đối 3% sẽ dừng pilot ngay tuần đầu (hiện 3,97% trong phạm vi; hang_nang 8,23%) → ngưỡng tương đối so với đối chứng + trần 6%.
- File output chạy trên máy thứ hai ban đầu lưu dạng UTF-16 (do lệnh `>` của PowerShell) nên vỡ chữ trên GitHub → chuyển lại sang UTF-8, nội dung giữ nguyên.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- Phút xem lại / làm lại là giả lập; phút làm lại trong dữ liệu (15,3) khác giả định của đề (9) → cần thay bằng phút đo thật sau tuần 1 pilot.
- ICC 0,02 là giả định; nên ước lượng lại từ tỉ lệ thành công theo `staff_id` khi có dữ liệu pilot.
- Đợt chạy thử không có đối chứng nên chưa nói được trợ lý có nâng chỉ số chính hay không.
- Nhiệm vụ C: bộ nhãn 2 được điền sau khi đã thấy bộ nhãn 1, nên tỉ lệ 20/20 không đo được đồng thuận độc lập. Lần sau hai người gắn nhãn phải chốt nhãn của mình trước rồi mới mở bộ kia.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arXiv:2504.13359.
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure".
- Tài liệu statsmodels, `NormalIndPower`, `proportion_effectsize`.
- `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (số để tự đối chiếu).
