"""AKShare 宏观数据采集：CPI/PPI/M2/LPR/社融
输出到 data/latest/macro_*.csv
每个接口独立 try/except，失败不影响其他。
"""
import os
import sys
import traceback

try:
    import akshare as ak
    import pandas as pd
except ImportError as e:
    print(f"[macro] 依赖缺失: {e}，请 pip install akshare")
    sys.exit(1)

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "latest")


def save(df, filename):
    path = os.path.join(OUTPUT_DIR, filename)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if df is not None and not df.empty:
        df.to_csv(path, index=False, encoding="utf-8-sig")
        print(f"  ✅ {filename} ({len(df)} 行)")
    else:
        pd.DataFrame().to_csv(path, index=False, encoding="utf-8-sig")
        print(f"  ⚠️  {filename} (空数据)")


def fetch_cpi():
    """月度CPI同比/环比"""
    df = ak.macro_china_cpi_monthly()
    save(df, "macro_cpi.csv")


def fetch_ppi():
    """月度PPI同比/环比"""
    df = ak.macro_china_ppi_monthly()
    save(df, "macro_ppi.csv")


def fetch_money_supply():
    """M0/M1/M2 货币供应量"""
    df = ak.macro_china_money_supply()
    save(df, "macro_money_supply.csv")


def fetch_lpr():
    """LPR 利率"""
    df = ak.macro_china_lpr()
    save(df, "macro_lpr.csv")


def fetch_shibor():
    """Shibor 利率"""
    df = ak.rate_interbank(market="上海银行间同业拆放利率", symbol="Shibor", indicator="隔夜")
    save(df, "macro_shibor.csv")


def fetch_gdp():
    """GDP 数据"""
    df = ak.macro_china_gdp_yearly()
    save(df, "macro_gdp.csv")


def fetch_nonfarm():
    """美国非农数据"""
    df = ak.macro_usa_non_farm()
    save(df, "macro_usa_nonfarm.csv")


FETCHERS = [
    ("CPI", fetch_cpi),
    ("PPI", fetch_ppi),
    ("M2", fetch_money_supply),
    ("LPR", fetch_lpr),
    ("Shibor", fetch_shibor),
    ("GDP", fetch_gdp),
    ("美国非农", fetch_nonfarm),
]


def main():
    print("=== 宏观数据采集 ===")
    ok = 0
    for name, fn in FETCHERS:
        try:
            fn()
            ok += 1
        except Exception as e:
            print(f"  ❌ {name}: {e}")
            traceback.print_exc()
    print(f"结果: {ok}/{len(FETCHERS)} 成功\n")


if __name__ == "__main__":
    main()
