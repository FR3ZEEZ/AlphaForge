"""AKShare 候选股数据采集：业绩报表、个股基本面
输出到 data/latest/candidate_*.csv
"""
import os
import sys
import traceback

try:
    import akshare as ak
    import pandas as pd
except ImportError as e:
    print(f"[candidates] 依赖缺失: {e}")
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


def fetch_yjbb():
    """业绩报表：营收/净利润/同比增速等"""
    df = ak.stock_yjbb_em(date="20260331")  # 最新一季报
    if df is not None and not df.empty:
        keep = [c for c in ["股票代码", "股票简称", "营业收入-同比增长", "净利润-同比增长",
                             "营业收入", "净利润", "每股净资产", "每股经营现金流"] if c in df.columns]
        df = df[keep] if keep else df
    save(df, "candidate_yjbb.csv")


def fetch_zygc():
    """主营构成（用于判断行业地位）"""
    # 这个接口需要个股代码，在综投时按需调用，全量采集意义不大
    # 留空placeholder，综投时按需用ak.stock_zygc_em(symbol)获取
    pass


FETCHERS = [
    ("业绩报表", fetch_yjbb),
]


def main():
    print("=== 候选股数据采集 ===")
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
