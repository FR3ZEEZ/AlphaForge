"""AKShare 板块数据采集：资金流向排名、涨幅跌幅排名、成分股
输出到 data/latest/sector_*.csv
"""
import os
import sys
import traceback

try:
    import akshare as ak
    import pandas as pd
except ImportError as e:
    print(f"[sectors] 依赖缺失: {e}")
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


def fetch_industry_flow():
    """行业板块资金流向排名（今日）"""
    df = ak.stock_sector_fund_flow_rank(indicator="今日", sector_type="行业")
    if df is not None and not df.empty:
        cols = [c for c in ["名称", "主力净流入-净额", "主力净流入-占比", "今日涨跌幅"] if c in df.columns]
        save(df[cols], "sector_flow_industry.csv")
    else:
        save(df, "sector_flow_industry.csv")


def fetch_concept_flow():
    """概念板块资金流向排名（今日）"""
    df = ak.stock_sector_fund_flow_rank(indicator="今日", sector_type="概念")
    if df is not None and not df.empty:
        cols = [c for c in ["名称", "主力净流入-净额", "主力净流入-占比", "今日涨跌幅"] if c in df.columns]
        save(df[cols], "sector_flow_concept.csv")
    else:
        save(df, "sector_flow_concept.csv")


def fetch_industry_top_gainers():
    """行业板块涨幅排名"""
    try:
        df = ak.stock_board_industry_name_em()
        if df is not None and not df.empty and "涨跌幅" in df.columns:
            df = df.sort_values("涨跌幅", ascending=False).head(30)
            cols = [c for c in ["板块名称", "涨跌幅", "上涨家数", "下跌家数"] if c in df.columns]
            save(df[cols], "sector_top_gainers.csv")
        else:
            save(df, "sector_top_gainers.csv")
    except Exception:
        raise


def fetch_industry_top_losers():
    """行业板块跌幅排名"""
    try:
        df = ak.stock_board_industry_name_em()
        if df is not None and not df.empty and "涨跌幅" in df.columns:
            df = df.sort_values("涨跌幅", ascending=True).head(30)
            cols = [c for c in ["板块名称", "涨跌幅", "上涨家数", "下跌家数"] if c in df.columns]
            save(df[cols], "sector_top_losers.csv")
        else:
            save(df, "sector_top_losers.csv")
    except Exception:
        raise


def fetch_north_flow():
    """北向资金流向"""
    try:
        df = ak.stock_hsgt_fund_flow_summary_em()
        save(df, "sector_north_flow.csv")
    except Exception:
        print("  ⚠️  北向资金接口异常（可能是非交易时段）")


FETCHERS = [
    ("行业资金流向", fetch_industry_flow),
    ("概念资金流向", fetch_concept_flow),
    ("板块涨幅TOP30", fetch_industry_top_gainers),
    ("板块跌幅TOP30", fetch_industry_top_losers),
    ("北向资金", fetch_north_flow),
]


def main():
    print("=== 板块数据采集 ===")
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
