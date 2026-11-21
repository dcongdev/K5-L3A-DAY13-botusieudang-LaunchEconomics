# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): botusieudang · L3A
- Nhóm được chấm: Huong (Nhóm 4) · K5-L3A · https://github.com/nhtng0212/K5-L3A-DAY13-Huong-LaunchEconomics

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 5 | Hồ sơ nêu nhiều số bất lợi kèm cách xử lý: xem lại 100% = 11.743–12.414 đ (0,98–1,03×), quoc_te 1,88×, power 0,64 ở mức 5 điểm, so với 12.000 đ có cả hệ thống 5.865 đ (0,49×). Nhưng bỏ qua hang_nang mở lại 8,23%: nhóm giữ hang_nang trong phạm vi mà trần an toàn tuyệt đối 6% (pilot_plan.yaml) sẽ dừng pilot ngay tuần đầu; con số 8,23% không xuất hiện trong hồ sơ. Ngoài ra chi_so.md (E2) viết làm lại gấp đôi "triệt tiêu hơn nửa phần tiết kiệm", trong khi chi phí tăng 2.315 đ trên phần tiết kiệm 7.528 đ, tức khoảng 31%. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Mọi số từ phút xem lại/làm lại (4.472 đ, 5.865 đ, B1–B4, A4) đều có nhãn [simulated]. Nêu rõ số đã cộng cố định 40 triệu/tháng (4.599 đ ở 45.000 đơn, 0,38×; 5.784 đ ở một nửa, 0,48×). Phạm vi thu hẹp về noi_dia (0,22×) và hang_nang (0,69×), loại quoc_te (1,88×, thành công 27,3%) bằng số. |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Đối chứng đồng thời, phân ngẫu nhiên theo nhân viên có seed, 20 cụm mỗi nhóm, n = 859 mỗi nhóm (m ≥ 299), nêu đánh đổi MDE 6 điểm và power 0,64. Ngưỡng an toàn tính theo 4,25% hiện tại nên không dừng oan tuần 1 (≥ 2 điểm so với đối chứng hoặc trần 6%). Luật dừng đủ NẾU–TRONG–THÌ–KHÔNG THÌ, người dừng là Giám đốc vận hành, hạn 30 phút, quyết định 2027-01-05. Điểm yếu nhỏ: luật dừng thứ 3 thực chất là phỏng vấn 5 nhân viên, và chống lan tỏa trong cùng depot chỉ dựa vào phân quyền staff_id. |
| **Tổng** | | | | **25 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Đề xuất khớp số của nhóm: chi phí 4.472 đ [simulated] (0,37×; 0,49× nếu tính cả hệ thống), phạm vi noi_dia + hang_nang, pilot đủ cỡ mẫu (859 mỗi nhóm, 20 cụm mỗi nhóm). Điều kiện hội đồng nêu: (1) xử lý hang_nang mở lại 8,23% so với trần an toàn 6%; (2) điều kiện tiên quyết số 3 hạn 2026-12-08 muộn hơn ngày khởi động pilot 2026-12-01 và nội dung là thu số liệu thật sau tuần đầu, cần chuyển thành việc sau khởi động hoặc dời hạn; (3) sửa nhận định "hơn nửa phần tiết kiệm" trong E2 (thực tế khoảng 31%). Ghi chú ngoài ba tiêu chí: bang_loi.md ghi cột TV4 do Codex chốt có tham chiếu hướng dẫn Lab, trái với yêu cầu gắn nhãn độc lập nên đồng thuận 18/20 = 90% chưa đáng tin.

**Một câu hỏi cho đội trình:** "hang_nang có tỉ lệ mở lại 8,23%, cao hơn trần an toàn tuyệt đối 6% của nhóm. Luật dừng xử lý thế nào ở tuần đầu?"

**Câu trả lời của đội trình (ghi lại tại buổi):** ...

---

## Danh sách soát khi đọc hồ sơ nhóm được chấm

- [ ] Chi phí mỗi việc thành công ≈ 4.472 đ (tử số có giờ nhân viên, mẫu số 978)? Chỉ ~275 đ là quên xem lại / làm lại.
- [ ] So với 12.000 đ có dùng chi phí cả hệ thống (≈ 5.865 đ = 0,49×) không, hay viết 0,37×?
- [ ] Có nhãn simulated ở mọi số từ phút xem lại / làm lại? Có nói số đã cộng chi phí cố định 40 triệu/tháng chưa (A4)?
- [ ] Phạm vi có loại quoc_te (1,88×) không? Có nhắc xem lại 100% (0,98×, hoặc 1,03× với phút làm lại thật) không?
- [ ] Cách chia có ≥ 20 cụm mỗi nhóm? Chia theo depot thì tối đa 300 → không đủ mẫu.
- [ ] Chọn MDE 6 điểm thì có nêu power ≈ 0,64 ở mức 5 điểm không?
- [ ] Ngưỡng an toàn so với tỉ lệ mở lại hiện tại 4,25% (3,97% trong phạm vi) có làm pilot dừng ngay tuần đầu không?
- [ ] Luật dừng đủ 4 vế NẾU – TRONG – THÌ – KHÔNG THÌ, người dừng là một vai trò?
- [ ] Đề xuất là Go / Go có điều kiện / No-go; không viết như thể đã duyệt chạy chính thức.

Câu hỏi gợi ý: "Chi phí mỗi việc thành công là bao nhiêu nếu tuần đầu phải xem lại 100%?" · "Cách chia của nhóm có ít nhất 20 cụm mỗi nhóm không?" · "hang_nang có tỉ lệ mở lại 8,23%; luật an toàn của nhóm xử lý thế nào?"

## Nhóm tự chấm hồ sơ của mình (trước khi gửi hội đồng)

| Tiêu chí | Tự chấm | Lý do |
|---|:---:|---|
| Đề xuất khớp bằng chứng | 10 | Go có điều kiện; nêu các con số bất lợi (xem lại 100%: 0,98–1,03×; quoc_te 1,88×; power 0,64 ở mức 5 điểm; hang_nang mở lại 8,23%) và cách xử lý, mỗi điều kiện có người phụ trách và ngày kiểm tra |
| Số giả lập và phạm vi | 10 | Mọi số từ phút giả lập có nhãn [simulated]; phạm vi noi_dia + hang_nang có lý do bằng số từ A3; so với 12.000 đ bằng chi phí cả hệ thống (0,49×) và có cộng cố định (A4) |
| Pilot ra được quyết định | 10 | Đối chứng đồng thời, bốc thăm có seed, 20 cụm mỗi nhóm, n hiệu dụng 859; 4 luật dừng có ngưỡng, thời hạn, người có quyền dừng. Điểm yếu tự nêu: MDE 6 điểm thay vì 5 |
