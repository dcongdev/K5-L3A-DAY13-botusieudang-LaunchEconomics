# Team

## Thông tin nhóm

*   Tên nhóm: botusieudang
*   Lớp: L3A
*   Repo nhóm: `K5-L3A-DAY13-botusieudang-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
*   URL repo, nhánh nộp, commit chốt: https://github.com/dcongdev/K5-L3A-DAY13-botusieudang-LaunchEconomics · `main` · ...

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --- | --- | --- | --- | --- | --- |
| 1 | Nguyễn Khôi Nguyên | 2A202603453 | ... | nguyenkhoinguyen07122005-cpu | Người viết code |
| 2 | Dương Văn Công | 2A202603468 | congvduong.work@gmail.com | dcongdev | Người gắn nhãn 2, kiêm giữ hồ sơ |
| 3 | Lê Quang Huy | 2A202603470 | lequanghuy2005@gmail.com | lequanghuy2005 | Người kiểm số |
| 4 | Nguyễn Hải Anh | 2A202603484 | haianh29112@gmail.com | haianh02034 | Người gắn nhãn 1 |

Bốn vai của lab:

*   **Người viết code:** viết và chạy `src/lab13.py`.
*   **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
*   **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
*   **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## NguyenKhoiNguyen-2A202603453

### Phần việc phụ trách

*   Người viết code: `src/lab13.py` (A1–A4, B1–B4, D1, D3, E1).

### Đóng góp cụ thể

*   Viết ba hàm A1, hàm `mo_hinh()` có tham số cho nhiệm vụ B, các bảng A3/A4, độ nhạy, B3, B4, cỡ mẫu D1 và ba chỉ số E1.
*   Soạn bản đầu `bang_chi_phi.md`, `pilot_plan.yaml`, `chi_so.md`, `ho_so_launch_v0.md`, `group_report.md` từ số do code in ra.

### Bằng chứng

*   Commit của tài khoản nguyenkhoinguyen07122005-cpu; output `cd src && python3 lab13.py`; báo cáo `report/team/2A202603453_NguyenKhoiNguyen.md`.

## DuongVanCong-MSSV

### Phần việc phụ trách

*   Phụ trách cột nhãn người 2, đối chiếu hai cột nhãn ở CP3 và giữ hồ sơ launch v0.

### Đóng góp cụ thể

*   Hoàn thiện cột nhãn người 2 cho 20 ca. Ghi 20/20 ca trùng và đối chiếu nhãn của 5 ca trong bảng khắc phục.

### Bằng chứng

*   [Bảng lỗi CP3](report/team/bang_loi.md) và [báo cáo cá nhân của Công](report/team/2A202603468_DuongVanCong.md).

## LeQuangHuy-2A202603470

### Phần việc phụ trách

*   Người kiểm số: chạy kiểm thử `src/lab13.py` trên máy thứ hai, tính tay hai con số đối chiếu, kiểm tra bảng chi phí A2, A3, B1–B4.

### Đóng góp cụ thể

*   Chạy `src/lab13.py` trên môi trường máy thứ hai (Windows), xác nhận ba phép thử đáp án biết trước ĐẠT và in đầy đủ tới "Xong.", xuất `report/team/output_kiem_so.txt`.
*   Tính tay bằng máy tính bỏ túi chi phí mỗi việc thành công (4.472 đ \[simulated\]) và cỡ mẫu D1e (m ≥ 299), đối chiếu khớp hoàn toàn với code và ghi vào `report/team/bang_chi_phi.md`.
*   Rà soát độ nhạy B1–B4 và các kết luận kinh tế cho hồ sơ launch.

### Bằng chứng

*   Output `report/team/output_kiem_so.txt`, mục Kiểm số tay trong `report/team/bang_chi_phi.md`, báo cáo `report/team/2A202603470_LeQuangHuy.md`.

## NguyenHaiAnh-2A202603484

### Phần việc phụ trách

*   Người gắn nhãn 1: theo dõi checklist "Xong khi", gắn nhãn độc lập 20 ca lỗi ở CP3, đối chiếu tỷ lệ đồng thuận và hoàn thiện phần lỗi.

### Đóng góp cụ thể

*   Đọc đề bài và thực hiện gắn nhãn độc lập 20 ca lỗi vào cột "Nhãn người 1" trong `report/team/bang_loi.md` theo 5 loại lỗi Google PAIR (4 ca Do người dùng, 5 ca Hệ thống, 4 ca Ngữ cảnh, 4 ca Giới hạn hệ thống, 3 ca Ngầm).
*   Chuẩn bị rà soát ca không trùng với người gắn nhãn 2 để đạt tỷ lệ đồng thuận ≥ 80% (≥ 16/20 ca) và xây dựng bảng biện pháp khắc phục đo lường được.

### Bằng chứng

*   Cột "Nhãn người 1" trong `report/team/bang_loi.md`, báo cáo cá nhân `report/team/2A202603484_NguyenHaiAnh.md`.