# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Trạng thái: **Xong, có bằng chứng · Chưa · Giả lập**. Gate 2a chỉ duyệt **kế hoạch pilot**. Số có nhãn [simulated] tính từ phút xem lại / làm lại giả lập.

Nhóm: botusieudang · Lớp: L3A

**Phạm vi đề xuất:** chỉ noi_dia + hang_nang (982/1.200 yêu cầu), chia theo nhân viên 20 + 20, giới hạn 2 lần chạy.

| # | Mục | Con số chính | Trạng thái | Người phụ trách |
|---:|---|---|---|---|
| 1 | Chi phí mỗi việc thành công | 4.472 đ toàn bộ = 16,3× hoá đơn token chia số yêu cầu (274,7 đ); trong phạm vi 3.414 đ, cộng cố định 40 triệu/tháng: 4.599 đ (45.000 yc/tháng), 5.784 đ nếu khối lượng còn một nửa [simulated] | Giả lập | PM trợ lý hoàn phí |
| 2 | Ba yếu tố nhạy nhất | Làm lại ×2: +51,8% · xem lại ×2: +40,7% · lương +25%: +23,1%; giá token ×2 chỉ +5,6% [simulated] | Giả lập | PM trợ lý hoàn phí |
| 3 | So với nhân viên tự làm (12.000 đ) | Cả hệ thống 5.865 đ/yêu cầu = **0,49×**; phạm vi + cố định 0,38×; theo loại: noi_dia 0,22× · hang_nang 0,69× · doi_tac 0,85× · **quoc_te 1,88×**; **xem lại 100%: 0,98×, 1,03× với phút làm lại thật** (B4) [simulated] | Giả lập | Giám đốc tài chính |
| 4 | Chỉ số chính, dùng, an toàn | Chính 82,83% (994/1.200) · bỏ qua gợi ý 27,12% (48/177) · mở lại 7 ngày 4,25% (51/1.200); 10 event có trace_id | Xong, có bằng chứng | Trưởng nhóm phân tích dữ liệu |
| 5 | Bảng lỗi và cách khắc phục | 20 ca, đồng thuận 20/20 = 100%; 5 cách khắc phục có ngưỡng đo được; lỗi nặng nhất: ca 7, 20 (báo hoàn sai, hoàn trùng) | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 | Pilot plan | Chia theo nhân viên 20 + 20 cụm; MDE 6 điểm, n = 859/nhóm, m ≥ 299, DE 6,96; **power 0,64 nếu tác động thật 5 điểm**; 4 luật dừng; quyết định 2027-01-14 | Xong, có bằng chứng | Giám đốc vận hành |
| 7 | Rủi ro kinh tế | Làm lại ×2 → 6.787 đ; xem lại 100% → 0,98–1,03×; khối lượng còn một nửa → cố định +2.370 đ/việc; ép 1 lần chạy → cả hệ thống đắt hơn 548.561 đ [simulated] | Giả lập | PM trợ lý hoàn phí |

**Con số bất lợi đã nêu và cách xử lý**

- Xem lại 100% không tiết kiệm (0,98×; 1,03× nếu làm lại 15,3 phút như dữ liệu [simulated]) → giảm xem lại theo bậc khi sua + bo < 15%, mục tiêu ≤ 4,8 phút mỗi lần xem lại.
- So đúng với 12.000 đ phải dùng chi phí cả hệ thống 0,49× [simulated], không phải 4.472 ÷ 12.000 = 0,37×.
- 40 nhân viên không đủ để thấy mức chênh 5 điểm (tối đa 1.000 < 1.251) → chấp nhận MDE 6 điểm, power chỉ 0,64 ở mức 5 điểm.
- hang_nang có tỉ lệ mở lại 8,23%, cao hơn trần 6% → luật an toàn so với đối chứng, theo dõi riêng hang_nang; vượt ngưỡng chi phí thì thu về noi_dia.
- Không đặt trần mở lại 3% vì tỉ lệ hiện tại trong phạm vi đã 3,97% → dùng +2 điểm so với đối chứng kèm trần 6%.

**Đề xuất:** **Go có điều kiện** — pilot noi_dia + hang_nang, chia theo nhân viên 20 + 20, bắt đầu 2026-12-07, với các điều kiện:

| Điều kiện | Người phụ trách | Ngày kiểm tra |
|---|---|---|
| Sửa khoá chống trùng (idempotency key) và đối soát sổ cái trước khi báo "đã hoàn" (ca 7, 20); test 0 ca lỗi | Kỹ sư trưởng agent | 2026-12-03 |
| Ký chấp nhận MDE 6 điểm và power 0,64 ở mức 5 điểm; chốt pilot_plan.yaml | Giám đốc vận hành | 2026-12-04 |
| Bật đủ 10 event có trace_id; thay phút simulated bằng phút đo thật và tính lại bảng chi phí | Trưởng nhóm phân tích dữ liệu | 2026-12-14 (cuối tuần 1) |
| Áp quy tắc giảm xem lại theo bậc; % được xem lại ≤ 50% cuối bước 0.25 | Trưởng nhóm CSKH | 2026-12-21 |
