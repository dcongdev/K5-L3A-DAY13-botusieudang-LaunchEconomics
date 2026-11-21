# Báo cáo cá nhân — NguyenKhoiNguyen-2A202603453

## 1. Thông tin thành viên

- Họ tên: Nguyễn Khôi Nguyên
- MSSV: 2A202603453
- Email: nguyenkhoinguyen07122005@gmail.com
- Vai trong nhóm: Người viết code

## 2. Phần việc phụ trách

Viết và chạy `src/lab13.py` cho nhiệm vụ A, B, D1 (kèm D3 và E1); chép số vào các file hồ sơ trong `report/team/`.

## 3. Đóng góp cụ thể

- A1: ba hàm `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`; ba phép thử in ĐẠT (1,20 · 1,25 · 1,25).
- A2–A4: hàm `mo_hinh()` cộng token + tool của mọi lần chạy và phút xem lại / làm lại [simulated], chia cho 978 việc thành công → 4.472 đ; tách theo loại; tỉ lệ ok theo lần thử; chi phí cả hệ thống 0,49×; cộng cố định 40 triệu/tháng → 4.599 đ = 0,38× [simulated].
- B1–B4: 9 kịch bản độ nhạy, một cặp, chi phí cả hệ thống theo giới hạn chạy, xem lại 100% (0,98×; 1,03× với phút làm lại 15,3) và mức hoà vốn 4,8–5,1 phút [simulated].
- D1: cỡ mẫu 1.251 / 3.103 / 1.000 / 300 / m ≥ 299 và power 0,64 bằng công thức và statsmodels.
- E1: ba chỉ số 82,83% · 27,12% · 4,25%.

## 4. Bằng chứng

- File: `src/lab13.py`, `report/team/bang_chi_phi.md`, `report/team/pilot_plan.yaml`.
- Commit: các commit `src/lab13.py` và hồ sơ của tài khoản GitHub `nguyenkhoinguyen07122005-cpu`.
- Output: `cd src && python3 lab13.py` (in đủ A1 → E1 và kiểm tra `pilot_plan.yaml` đọc được, không còn dấu `?`).

## 5. Công cụ AI đã dùng

- Claude: hỗ trợ viết code `lab13.py` và kiểm tra các file hồ sơ từ số do code in ra.
- Tự kiểm tra: chạy lại `lab13.py`, đối chiếu từng con số với bảng "số để tự đối chiếu" trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (lệch 0%, riêng B4 độ nhạy 12.415 so với 12.414 do làm tròn); tính tay lại chi phí mỗi việc thành công 4.373.585 ÷ 978 = 4.472 đ và m ≥ 299 ở câu D1e.
- Không dùng AI để gắn nhãn 20 ca lỗi (nhiệm vụ C do hai người gắn nhãn của nhóm làm độc lập) hay chấm nhóm khác.

## 6. Tự đánh giá

- Hoàn thành phần code A, B, D1; `src/lab13.py` chạy từ đầu đến cuối và khớp số đối chiếu trong hướng dẫn.
- Cần cải thiện: phút xem lại và làm lại vẫn là số giả lập; lần sau nên kiểm tra giả định của đề (9 phút làm lại so với 15,3 phút trong dữ liệu) sớm hơn.
