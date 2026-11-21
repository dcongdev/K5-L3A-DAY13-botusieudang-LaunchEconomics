# Chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

Nhóm botusieudang · L3A · Số tính bằng `cd src && python3 lab13.py` trên 1.200 yêu cầu của đợt chạy thử (giả lập).

> Ghi chú cách đọc: đợt chạy thử **không có nhóm đối chứng**, nên chỉ viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số từ 0,70".

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu | Event dùng để tính |
|---|---|---|---|---|
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | (dong_trong_24h = 1 và mo_lai_trong_7_ngay = 0) ÷ tổng số yêu cầu | **82,83%** (994/1.200); trong phạm vi noi_dia + hang_nang: 92,26% (906/982) | `refund_request_created`, `ticket_closed`, `ticket_reopened` |
| Dùng | Tỉ lệ bỏ qua gợi ý | (quyet_dinh_xem_lai = sua hoặc bo) ÷ số yêu cầu được xem lại | **27,12%** (48/177; sua 41, bo 7, giu 129) | `agent_suggestion_shown`, `staff_review_decision` |
| An toàn | Tỉ lệ lỗi lọt đến khách | mo_lai_trong_7_ngay = 1 ÷ tổng số yêu cầu | **4,25%** (51/1.200); trong phạm vi 3,97% (noi_dia 3,16%, hang_nang 8,23%) | `refund_request_created`, `ticket_reopened` |
| Dùng (nhóm đề xuất) | Tỉ lệ nhân viên nhóm trợ lý thực sự mở trợ lý | Số yêu cầu của nhóm trợ lý có `agent_suggestion_shown` và nhân viên mở xem ÷ số yêu cầu được giao cho nhóm trợ lý | Không cần tính | `refund_request_created` (arm), `agent_suggestion_shown` |
| An toàn (nhóm đề xuất) | % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm như ca 5, 17) | Số đơn có so_tien_da_hoan ≠ so_tien_dung ÷ 100 đơn kiểm tra mẫu/tuần | Không cần tính | `audit_sample_checked`, `refund_ledger_write` |
| An toàn (nhóm đề xuất) | Số ca hoàn trùng / báo "đã hoàn" khi sổ cái lỗi (ca 7, 20) | Đếm trace có > 1 `refund_ledger_write` ok cho cùng đơn, hoặc tin nhắn "đã hoàn" không có ledger ok | Không cần tính; ngưỡng 0 | `refund_ledger_write`, `agent_run_completed` |

## Danh sách event (10 event, mọi event đều có `trace_id`)

| # | Event | Ai tạo | Thuộc tính chính | Thời điểm |
|---:|---|---|---|---|
| 1 | `refund_request_created` | App khách | request_id, loai, so_tien_vnd, depot, staff_id, arm (tro_ly / doi_chung), **trace_id** | Khi khách gửi yêu cầu |
| 2 | `agent_run_completed` | Agent | attempt, tokens_in, tokens_out, tool_calls, status (ok/loi), model, phien_ban_bang_gia, **trace_id** | Sau mỗi lần chạy, kể cả lần lỗi |
| 3 | `agent_suggestion_shown` | Giao diện nhân viên | staff_id, so_tien_de_xuat, ly_do, opened (có/không), **trace_id** | Khi gợi ý hiện cho nhân viên |
| 4 | `staff_review_decision` | Nhân viên | quyet_dinh (giu/sua/bo), phut_xem_lai (đo thật, từ lúc mở đến lúc bấm), **trace_id** | Khi bấm gửi / sửa / bỏ |
| 5 | `staff_rework_completed` | Nhân viên | phut_lam_lai (đo thật), ly_do, **trace_id** | Khi làm lại xong |
| 6 | `refund_ledger_write` | Dịch vụ sổ cái | idempotency_key, so_tien, ket_qua (ok/loi, mã HTTP), **trace_id** | Khi ghi lệnh hoàn |
| 7 | `handoff_to_staff` | Agent | reason (thieu_du_lieu / ngoai_pham_vi / het_lan_chay / input_khong_ho_tro), tom_tat, **trace_id** | Khi chuyển cho nhân viên |
| 8 | `ticket_closed` | Hệ thống ticket | closed_at, kenh_thong_bao, **trace_id** | Khi đóng yêu cầu |
| 9 | `ticket_reopened` | Khách (qua hệ thống ticket) | reopened_at, reason (so_tien / chua_nhan / khac), **trace_id** | Khi khách mở lại |
| 10 | `audit_sample_checked` | Kế toán | so_tien_da_hoan, so_tien_dung, phien_ban_bang_gia, **trace_id** | Hằng tuần, 100 đơn mẫu |

Phụ trợ cho bảng lỗi (ca 9): `input_validation_failed` — Agent — reason, gia_tri_nhap (đã che), **trace_id** — khi đầu vào không hợp lệ.

**Kiểm tra chéo chỉ số ↔ event:** mọi chỉ số trong bảng E1 đều có cột "Event dùng để tính" trỏ đến event trong danh sách → đều đo được. Chi phí mỗi việc thành công tính được từ event 2 (token, tool), 4 và 5 (phút đo thật thay cho cột simulated), 8–9 (thành công).

## E2 · Rủi ro kinh tế (số lấy từ bảng độ nhạy)

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
|---|---|---|---|---|
| Số ca làm lại tăng gấp đôi | +51,8%, chi phí mỗi việc thành công lên 6.787 đ [simulated] (B1) | Tỉ lệ làm lại theo tuần > 7% (đợt chạy thử: 4,9% trong phạm vi) | Thu hẹp về noi_dia, rà 20 trace làm lại, sửa tool/prompt trước khi mở lại hang_nang | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ = 0,98× nhân viên tự làm; 12.415 đ = 1,03× nếu làm lại 15,3 phút như dữ liệu [simulated] (B4) | % yêu cầu được xem lại còn > 50% cuối bước 0.25 | Giảm xem lại theo bậc 100 → 50 → 20 → 10% khi tỉ lệ sua + bo < 15%; đo phút xem lại thật, mục tiêu ≤ 4,8 phút/lần (mức hoà vốn) | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Cố định 40 triệu/tháng: +1.185 đ/việc ở 45.000 yêu cầu/tháng (4.599 đ = 0,38×), +2.370 đ/việc nếu còn một nửa (5.784 đ = 0,48×) [simulated] (A4) | Số việc thành công qua trợ lý theo tuần < 50% kế hoạch | Không mở rộng pilot; xem lại hợp đồng chi phí cố định trước Gate tiếp theo | PM trợ lý hoàn phí |
| Lương nhân viên tăng 25% | +23,1%, lên 5.506 đ [simulated] (B1) — vẫn < 12.000 đ nhưng cũng làm baseline đắt hơn | Thay đổi bảng lương / chi phí phút nhân viên | Cập nhật LUONG_PHUT và BASELINE cùng lúc, tính lại tỉ số | Giám đốc tài chính |
| Tối ưu sai chỉ số: ép chạy 1 lần để CPS thấp | CPS 4.111 đ nhưng chi phí cả hệ thống 7.449.781 đ, đắt hơn giới hạn 2 lần 548.561 đ [simulated] (B3) | Số yêu cầu chuyển nhân viên/tuần tăng > 20% | Giữ giới hạn 2 lần; báo cáo luôn kèm chi phí cả hệ thống | Kỹ sư trưởng agent |
| Lỗi ngầm làm tăng token (như ca 12) | Một depot gấp 3 lần token; token chỉ 5,6% tổng nên tác động CPS nhỏ (+5,6% khi giá token ×2) nhưng kéo dài không ai thấy | Token trung bình mỗi yêu cầu theo depot > 1,5× trung vị các depot, theo tuần | Cảnh báo tự động theo depot; rà tool của depot bị lệch | Kỹ sư trưởng agent |
