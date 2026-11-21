"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm nhóm botusieudang (L3A).

Chạy trong thư mục src/:  python3 lab13.py
Cần: pandas, numpy, statsmodels, pyyaml (src/requirements.txt)
Đọc logix_runs.csv và logix_requests.csv trong src/. Bản gốc chưa sửa: lab13_starter.py.

Mọi con số tính từ cột *_simulated (phút xem lại, phút làm lại) là SỐ GIẢ LẬP
và được in kèm nhãn [simulated].
"""
import math
import os
from statistics import NormalDist

import pandas as pd

# ---------- Bảng giá GIẢ ĐỊNH của lab ----------
GIA_VAO = 26        # đ / 1.000 token đầu vào
GIA_RA = 130        # đ / 1.000 token đầu ra
GIA_TOOL = 15       # đ / lần gọi tool
LUONG_PHUT = 2000   # đ / phút nhân viên
BASELINE = 12000    # đ / yêu cầu khi nhân viên tự làm (6 phút)
CHI_PHI_CO_DINH_THANG = 40_000_000
YEU_CAU_THANG = 45_000

PHAM_VI_PILOT = ['noi_dia', 'hang_nang']
SIM = '[simulated]'


# ======================= Nhiệm vụ A1 =======================
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình; k=None nghĩa là chạy lại đến khi đúng."""
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, theo bội số giá một lần chạy (luôn = 1/p)."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9
    print(f'  so_lan_chay_ky_vong(0.8, 2)            = {so_lan_chay_ky_vong(0.8, 2):.2f}')
    print(f'  so_lan_chay_ky_vong(0.8)               = {so_lan_chay_ky_vong(0.8):.2f}')
    print(f'  he_so_chi_phi_moi_viec_thanh_cong(0.8,3)= {he_so_chi_phi_moi_viec_thanh_cong(0.8, 3):.2f}')
    print('  Ba phép thử đáp án biết trước: ĐẠT')


# ======================= Nhiệm vụ A2 =======================
def mo_hinh(runs, reqs, gia_vao=GIA_VAO, gia_ra=GIA_RA, gia_tool=GIA_TOOL,
            luong_phut=LUONG_PHUT, he_so_xem_lai=1.0, he_so_lam_lai=1.0,
            max_lan_chay=None):
    """Chi phí mỗi việc thành công (cps).
    Tử số: token + tool của MỌI lần chạy (kể cả lỗi) + tiền xem lại + tiền làm lại.
    Mẫu số: số yêu cầu có ket_qua == 'thanh_cong'.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    return dict(
        so_yeu_cau=len(reqs), so_lan_chay=len(runs),
        token=tien_token.sum(), tool=tien_tool.sum(), so_lan_goi_tool=int(runs['tool_calls'].sum()),
        chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
        phut_xem_lai=reqs['phut_xem_lai_simulated'].sum(),
        phut_lam_lai=reqs['phut_lam_lai_simulated'].sum(),
        xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
        thanh_cong=thanh_cong, khong_thanh_cong=len(reqs) - thanh_cong,
        cps=tong / thanh_cong,
        hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs),
    )


# ======================= Nhiệm vụ D1 =======================
def co_mau(p1, p2, alpha=0.05, power=0.8):
    za, zb = NormalDist().inv_cdf(1 - alpha / 2), NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                      + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)


def he_so_thiet_ke(m, icc):
    return 1 + (m - 1) * icc


def n_hieu_dung(c, m, icc):
    return c * m / he_so_thiet_ke(m, icc)


def tim_m_toi_thieu(n_can, c, icc):
    """m nhỏ nhất để c·m/DE ≥ n_can. Không tồn tại nếu n_can ≥ c/ICC."""
    if n_can >= c / icc:
        return None
    return math.ceil(n_can * (1 - icc) / (c - n_can * icc))


def doc_csv(ten):
    for thu_muc in ('.', '..'):
        duong_dan = os.path.join(thu_muc, ten)
        if os.path.exists(duong_dan):
            return duong_dan
    raise FileNotFoundError(f'Không thấy {ten} ở thư mục hiện tại hoặc thư mục cha')


def tieu_de(chu):
    print('\n' + '=' * 78 + f'\n{chu}\n' + '=' * 78)


def main():
    runs = pd.read_csv(doc_csv('logix_runs.csv'))
    reqs = pd.read_csv(doc_csv('logix_requests.csv'), keep_default_na=False)

    # ---------------- A1 ----------------
    tieu_de('A1 · Ba phép thử đáp án biết trước (p = 0,8)')
    kiem_tra_dap_an_biet_truoc()

    # ---------------- A2 ----------------
    tieu_de('A2 · Chi phí mỗi việc thành công, tính từ trace (1.200 yêu cầu)')
    g = mo_hinh(runs, reqs)
    dong = [
        ('Token (mọi lần chạy)', g['token'], 'đo từ trace'),
        (f"Tool ({g['so_lan_goi_tool']:,} lần gọi)", g['tool'], 'đo từ trace'),
        ('  Trong đó lần chạy thứ 2 và 3', g['chay_lai'], 'đo từ trace'),
        (f"Xem lại ({g['phut_xem_lai']:,.0f} phút)", g['xem_lai'], 'simulated'),
        (f"Làm lại ({g['phut_lam_lai']:,.0f} phút)", g['lam_lai'], 'simulated'),
        ('Tổng chi phí', g['tong'], 'có phần simulated'),
        ('Số việc thành công', g['thanh_cong'], ''),
        ('Chi phí mỗi việc thành công', g['cps'], 'simulated'),
        ('Hoá đơn token+tool / số yêu cầu', g['hoa_don_moi_yc'], 'đo từ trace'),
    ]
    for ten, gt, nhan in dong:
        print(f'  {ten:36s} {gt:>14,.1f}  {nhan}')
    boi = g['cps'] / g['hoa_don_moi_yc']
    print(f"\n  CPS gấp {boi:.1f} lần hoá đơn chia số yêu cầu {SIM}")
    for ten in ('token', 'tool', 'xem_lai', 'lam_lai'):
        print(f"  Tỉ trọng {ten:8s}: {g[ten] / g['tong'] * 100:5.1f}%")
    print(f"  Giờ nhân viên (xem lại + làm lại): {(g['xem_lai'] + g['lam_lai']) / g['tong'] * 100:.1f}% {SIM}")
    ht = g['tong'] + BASELINE * g['khong_thanh_cong']
    print(f"  So với 12.000 đ phải tính cả {g['khong_thanh_cong']} yêu cầu nhân viên làm thay: "
          f"({g['tong']:,.0f} + {g['khong_thanh_cong']} × 12.000) / {g['so_yeu_cau']} = "
          f"{ht / g['so_yeu_cau']:,.0f} đ/yêu cầu = {ht / g['so_yeu_cau'] / BASELINE:.2f}× {SIM}")

    # ---------------- A3 ----------------
    tieu_de('A3 · Tách theo loại yêu cầu')
    print(f"  {'loai':10s} {'n':>5s} {'TL t.công':>9s} {'chạy/yc':>8s} {'CPS [sim]':>10s} {'so 12k':>7s}")
    a3 = {}
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        r = reqs[reqs['loai'] == loai]
        m = mo_hinh(runs, r)
        a3[loai] = m
        print(f"  {loai:10s} {len(r):5d} {m['thanh_cong'] / len(r) * 100:8.1f}% "
              f"{m['so_lan_chay'] / len(r):8.2f} {m['cps']:10,.0f} {m['cps'] / BASELINE:6.2f}x")
    pv = reqs[reqs['loai'].isin(PHAM_VI_PILOT)]
    m_pv = mo_hinh(runs, pv)
    print(f"  {'pham_vi':10s} {len(pv):5d} {m_pv['thanh_cong'] / len(pv) * 100:8.1f}% "
          f"{m_pv['so_lan_chay'] / len(pv):8.2f} {m_pv['cps']:10,.0f} {m_pv['cps'] / BASELINE:6.2f}x"
          '   (noi_dia + hang_nang)')

    print('\n  Tỉ lệ status = ok theo từng lần thử (chạy lại có giúp không?):')
    rr = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    rr['ok'] = (rr['status'] == 'ok').astype(float)
    bang_ok = rr.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean')
    bang_n = rr.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='count')
    for loai in bang_ok.index:
        o = '  '.join(f"lần {a}: {bang_ok.loc[loai, a] * 100:5.1f}% (n={int(bang_n.loc[loai, a])})"
                      for a in bang_ok.columns if not pd.isna(bang_ok.loc[loai, a]))
        print(f'  {loai:10s} {o}')

    # ---------------- A4 ----------------
    tieu_de(f'A4 · Cộng chi phí cố định 40 triệu đ/tháng (phạm vi noi_dia + hang_nang) {SIM}')
    tc_mau = m_pv['thanh_cong']
    for nhan, he_so in (('45.000 yêu cầu/tháng', 1.0), ('Một nửa khối lượng', 0.5)):
        viec_thang = YEU_CAU_THANG * he_so * tc_mau / len(reqs)
        co_dinh = CHI_PHI_CO_DINH_THANG / viec_thang
        tong_viec = m_pv['cps'] + co_dinh
        print(f"  {nhan:22s} việc t.công/tháng {viec_thang:8,.0f} | cố định/việc {co_dinh:6,.0f} đ | "
              f"CPS + cố định {tong_viec:6,.0f} đ = {tong_viec / BASELINE:.2f}×")
    print(f"  (CPS phạm vi = {m_pv['tong']:,.0f} / {tc_mau} = {m_pv['cps']:,.0f} đ; "
          f"số việc/tháng = 45.000 × {tc_mau}/{len(reqs)})")

    # ---------------- B1 ----------------
    tieu_de(f'B1 · Bảng độ nhạy (đổi từng yếu tố) {SIM}')
    kich_ban = {
        'Giá token gấp đôi': dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
        'Tỉ lệ xem lại gấp đôi': dict(he_so_xem_lai=2),
        'Tỉ lệ xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Số ca làm lại gấp đôi': dict(he_so_lam_lai=2),
        'Số ca làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương nhân viên tăng 25%': dict(luong_phut=2500),
        'Chỉ cho chạy tối đa 2 lần': dict(max_lan_chay=2),
        'Chỉ cho chạy 1 lần': dict(max_lan_chay=1),
    }
    goc = g['cps']
    print(f"  {'Gốc (A2)':30s} {goc:8,.0f} đ")
    for ten, kw in kich_ban.items():
        c = mo_hinh(runs, reqs, **kw)['cps']
        print(f'  {ten:30s} {c:8,.0f} đ  {(c / goc - 1) * 100:+6.1f}%')

    # ---------------- B2 ----------------
    tieu_de('B2 · Đổi một cặp: giá token ×2 và xem lại ×2')
    c2 = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    print(f'  {c2:,.0f} đ ({(c2 / goc - 1) * 100:+.1f}%) {SIM}')
    print('  Xếp hạng (theo kịch bản gấp đôi / +25%): 1. số ca làm lại (+51,8%)'
          ' · 2. tỉ lệ xem lại (+40,7%) · 3. lương nhân viên (+23,1%) · giá token chỉ +5,6%')

    # ---------------- B3 ----------------
    tieu_de(f'B3 · Chi phí cả hệ thống theo giới hạn chạy lại {SIM}')
    for k in (1, 2, 3):
        m = mo_hinh(runs, reqs, max_lan_chay=k)
        he_thong = m['tong'] + BASELINE * m['khong_thanh_cong']
        print(f"  Tối đa {k} lần: trợ lý {m['tong']:12,.0f} đ | không t.công {m['khong_thanh_cong']:4d} | "
              f"cả hệ thống {he_thong:12,.0f} đ | CPS {m['cps']:6,.0f} đ")

    # ---------------- B4 ----------------
    tieu_de(f'B4 · Xem lại 100% trong phạm vi noi_dia + hang_nang {SIM}')
    pv_ids = pv['request_id']
    runs_pv = runs[runs['request_id'].isin(pv_ids)]
    co_ok = runs_pv.loc[runs_pv['status'] == 'ok', 'request_id'].nunique()
    so_lam_lai = int((pv['ket_qua'] == 'lam_lai').sum())
    tien_xem = co_ok * 5 * LUONG_PHUT
    tien_lam = so_lam_lai * 9 * LUONG_PHUT
    tien_tt = (runs_pv['tokens_in'] / 1000 * GIA_VAO + runs_pv['tokens_out'] / 1000 * GIA_RA
               + runs_pv['tool_calls'] * GIA_TOOL).sum()
    tc_pv = int((pv['ket_qua'] == 'thanh_cong').sum())
    tong_b4 = tien_xem + tien_lam + tien_tt
    print(f'  Yêu cầu có ≥1 lần chạy ok: {co_ok} × 5 phút = {tien_xem:,.0f} đ')
    print(f'  Ca làm lại: {so_lam_lai} × 9 phút = {tien_lam:,.0f} đ')
    print(f'  Token + tool ({len(pv)} yêu cầu): {tien_tt:,.0f} đ')
    print(f'  Tổng {tong_b4:,.0f} đ / {tc_pv} việc thành công = {tong_b4 / tc_pv:,.0f} đ '
          f'= {tong_b4 / tc_pv / BASELINE:.2f}× của 12.000 đ; xem lại chiếm {tien_xem / tong_b4 * 100:.0f}%')

    # Độ nhạy B4 theo phút làm lại thật trong dữ liệu
    tb_lam_lai = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated']
    p_ll = round(tb_lam_lai.mean(), 1)
    tong_b4b = tien_xem + so_lam_lai * p_ll * LUONG_PHUT + tien_tt
    print(f'  Độ nhạy: phút làm lại trong dữ liệu TB {tb_lam_lai.mean():.1f} (trung vị {tb_lam_lai.median():.1f}) '
          f'→ dùng {p_ll}: tổng {tong_b4b:,.0f} đ → {tong_b4b / tc_pv:,.0f} đ = {tong_b4b / tc_pv / BASELINE:.2f}×')
    for p in (9, p_ll):
        hv = (BASELINE * tc_pv - so_lam_lai * p * LUONG_PHUT - tien_tt) / (co_ok * LUONG_PHUT)
        print(f'  Hoà vốn: mỗi lần xem lại ≤ {hv:.1f} phút (làm lại {p} phút/ca)')

    # ---------------- D1 ----------------
    tieu_de('D1 · Cỡ mẫu (baseline 0,70; alpha 0,05; power 0,8; ICC 0,02)')
    ICC = 0.02
    n5 = co_mau(0.70, 0.75)
    n6 = co_mau(0.70, 0.76)
    de75 = he_so_thiet_ke(75, ICC)
    n_b = math.ceil(n5 * de75)
    nv_b = math.ceil(n_b / 75)
    m_e = tim_m_toi_thieu(n6, 20, ICC)
    print(f'  a. Chia theo yêu cầu: {n5:,} yêu cầu mỗi nhóm (mức chênh 5 điểm)')
    print(f'  b. Theo nhân viên, m=75: DE = {de75:.2f}; n = {n_b:,} mỗi nhóm; {nv_b} nhân viên mỗi nhóm '
          f'→ tổng {2 * nv_b} > 40: KHÔNG ĐỦ NGƯỜI')
    print(f'  c. 20 nhân viên mỗi nhóm: n hiệu dụng tối đa = 20/0,02 = {20 / ICC:,.0f} < {n5:,}: KHÔNG ĐẠT')
    print(f'  d. 6 depot mỗi nhóm: n hiệu dụng tối đa = 6/0,02 = {6 / ICC:,.0f}')
    print(f'  e. Mức chênh 6 điểm: cần {n6} mỗi nhóm; 20 người mỗi nhóm → m ≥ {m_e} yêu cầu/người '
          f'(DE = {he_so_thiet_ke(m_e, ICC):.2f}, n hiệu dụng = {n_hieu_dung(20, m_e, ICC):.0f})')
    try:
        from statsmodels.stats.power import NormalIndPower
        from statsmodels.stats.proportion import proportion_effectsize
        es5 = proportion_effectsize(0.75, 0.70)
        es6 = proportion_effectsize(0.76, 0.70)
        print(f'  statsmodels (Cohen h): n cho 5 điểm = '
              f'{math.ceil(NormalIndPower().solve_power(es5, alpha=0.05, power=0.8)):,}; '
              f'n cho 6 điểm = {math.ceil(NormalIndPower().solve_power(es6, alpha=0.05, power=0.8)):,}')
        pw = NormalIndPower().power(es5, nobs1=n6, alpha=0.05)
        print(f'  Con số bất lợi: thiết kế cho 6 điểm, nếu tác động thật chỉ 5 điểm thì power ≈ {pw:.2f}')
    except ImportError:
        print('  (Chưa cài statsmodels, bỏ qua phần kiểm tra chéo)')
    yc_nv_ngay = 1500 / 40 * reqs['loai'].isin(PHAM_VI_PILOT).mean()
    print(f'  Khả thi câu e: mỗi nhân viên nhận ~{yc_nv_ngay:.1f} yêu cầu trong phạm vi/ngày '
          f'→ cần ~{math.ceil(m_e / yc_nv_ngay)} ngày làm việc ở bước 0.50 để đạt m = {m_e}')

    # ---------------- D3 · ngưỡng an toàn ----------------
    tieu_de('D3 · Tỉ lệ mở lại hiện tại (trước khi chốt luật an toàn)')
    print(f"  Toàn bộ: {reqs.mo_lai_trong_7_ngay.mean() * 100:.2f}% ({reqs.mo_lai_trong_7_ngay.sum()}/{len(reqs)})")
    print(f"  Phạm vi noi_dia + hang_nang: {pv.mo_lai_trong_7_ngay.mean() * 100:.2f}% "
          f"({pv.mo_lai_trong_7_ngay.sum()}/{len(pv)})")
    for loai, r in reqs.groupby('loai'):
        print(f"    {loai:10s} {r.mo_lai_trong_7_ngay.mean() * 100:5.2f}%")
    print(f"  Tỉ lệ làm lại trong phạm vi: {(pv.ket_qua == 'lam_lai').mean() * 100:.1f}%")

    # ---------------- E1 ----------------
    tieu_de('E1 · Ba chỉ số tính thử trên 1.200 yêu cầu')
    chinh = (reqs.dong_trong_24h == 1) & (reqs.mo_lai_trong_7_ngay == 0)
    xem = reqs[reqs.duoc_xem_lai == 1]
    bo_qua = xem.quyet_dinh_xem_lai.isin(['sua', 'bo'])
    an_toan = reqs.mo_lai_trong_7_ngay == 1
    print(f'  Chính  : đóng 24h & không mở lại 7 ngày = {chinh.mean() * 100:.2f}% ({chinh.sum()}/{len(reqs)})')
    print(f'  Dùng   : bỏ qua gợi ý (sua+bo)/được xem lại = {bo_qua.mean() * 100:.2f}% ({bo_qua.sum()}/{len(xem)})')
    print(f'  An toàn: mở lại trong 7 ngày = {an_toan.mean() * 100:.2f}% ({an_toan.sum()}/{len(reqs)})')
    print(f"  Phân bố quyết định xem lại: {xem.quyet_dinh_xem_lai.value_counts().to_dict()}")
    print(f"  Tỉ lệ được xem lại: {reqs.duoc_xem_lai.mean() * 100:.1f}% ({len(xem)}/{len(reqs)})")
    chinh_pv = ((pv.dong_trong_24h == 1) & (pv.mo_lai_trong_7_ngay == 0))
    print(f'  Chỉ số chính trong phạm vi: {chinh_pv.mean() * 100:.2f}% ({chinh_pv.sum()}/{len(pv)})')

    # ---------------- Kiểm tra pilot_plan.yaml ----------------
    YAML = os.path.join('..', 'report', 'team', 'pilot_plan.yaml')
    if os.path.exists(YAML):
        tieu_de('Kiểm tra pilot_plan.yaml')
        try:
            import yaml
            with open(YAML, encoding='utf-8') as f:
                noi_dung = f.read()
            plan = yaml.safe_load(noi_dung)['pilot']
            print(f"  yaml.safe_load: OK · {len(plan['stop_rules'])} luật dừng · "
                  f"còn dấu '?': {'CÓ' if '?' in noi_dung else 'không'}")
        except ImportError:
            print('  (Chưa cài pyyaml, bỏ qua)')
    print('\nXong.')


if __name__ == '__main__':
    main()
