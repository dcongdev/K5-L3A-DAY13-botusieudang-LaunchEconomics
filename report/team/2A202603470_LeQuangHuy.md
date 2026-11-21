# Báo cáo cá nhân — LeQuangHuy-2A202603470

## 1. Thông tin thành viên

- Họ tên: Lê Quang Huy
- MSSV: 2A202603470
- Email: lehuy20112002@gmail.com
- Vai trong nhóm: người kiểm số

## 2. Phần việc phụ trách

- Người kiểm số: thiết lập môi trường chạy code độc lập trên máy thứ hai (Windows), kiểm tra 3 phép thử và luồng thực thi `src/lab13.py`, xuất output `report/team/output_kiem_so.txt`.
- Tính tay bằng máy tính bỏ túi hai con số cốt lõi (Chi phí mỗi việc thành công [simulated] và cỡ mẫu tối thiểu mỗi nhân viên D1e) để đối chiếu độc lập với kết quả code in ra.
- Đối chiếu số liệu các bảng A2, A3, B1–B4 trong `report/team/bang_chi_phi.md` với output từ terminal.

## 3. Đóng góp cụ thể

- Chạy kiểm thử độc lập `src/lab13.py` trên máy thứ hai, xác nhận dòng "Ba phép thử đáp án biết trước: ĐẠT" và dòng cuối "Xong.", lưu toàn bộ kết quả vào `report/team/output_kiem_so.txt`.
- Thực hiện tính tay bằng máy tính bỏ túi:
  + Chi phí mỗi việc thành công: (245.585 + 84.000 + 890 × 2.000 + 1.132 × 2.000) ÷ 978 = 4.373.585 ÷ 978 = 4.471,97 đ ≈ 4.472 đ (khớp 100% với code).
  + Cỡ mẫu D1e: 20m ≥ 859 × (0,98 + 0,02m) ↔ 2,82m ≥ 841,82 ↔ m ≥ 298,52 → m ≥ 299 (khớp 100% với code).
- Điền bảng đối chiếu kiểm số tay vào cuối file `report/team/bang_chi_phi.md`.
- Rà soát tính hợp lý kinh tế của các kịch bản độ nhạy B1–B4 và câu trả lời giới hạn chạy lại B3.

## 4. Bằng chứng

- Commit: commit kiểm số tay và chạy code máy 2, tài khoản GitHub `lequanghuy2005`.
- File:
  + `report/team/output_kiem_so.txt`
  + `report/team/bang_chi_phi.md` (mục `## Kiểm số tay (Người kiểm số: Lê Quang Huy)`)
  + `report/team/2A202603470_LeQuangHuy.md`

## 5. Công cụ AI đã dùng

- Công cụ: Trợ lý AI (Claude / ChatGPT / Gemini) được dùng để hỗ trợ rà soát cú pháp Markdown và trình bày bảng đối chiếu.
- Cách tự kiểm tra: Tự thực hiện toàn bộ các phép tính số học (cộng, nhân, chia, giải bất phương trình bậc nhất một ẩn) bằng máy tính bỏ túi vật lý Casio fx-580VN X, không dùng code hay AI tính toán thay, sau đó so sánh từng con số với output chạy trực tiếp từ `python lab13.py`.

## 6. Tự đánh giá

- Hoàn thành đầy đủ, chính xác và đúng thời hạn toàn bộ trách nhiệm của Người kiểm số theo đúng checklist nộp bài và tiêu chí đánh giá Lab 13.
