"""一键执行所有 AKShare 数据采集脚本"""
import os
import sys
import subprocess

SCRIPTS_DIR = os.path.dirname(__file__)

SCRIPTS = [
    ("宏观数据", "fetch_macro.py"),
    ("板块数据", "fetch_sectors.py"),
    ("候选股数据", "fetch_candidates.py"),
]


def main():
    print("=" * 40)
    print("  AKShare 数据采集 — 一键执行")
    print("=" * 40)
    print()

    results = []
    for name, script in SCRIPTS:
        print(f">>> [{name}] 采集开始...")
        path = os.path.join(SCRIPTS_DIR, script)
        ret = subprocess.run([sys.executable, path], capture_output=False)
        if ret.returncode == 0:
            results.append((name, "✅"))
        else:
            results.append((name, "❌"))
        print()

    print("=" * 40)
    print("  汇总")
    print("=" * 40)
    for name, status in results:
        print(f"  {status} {name}")
    print()
    print("数据已保存到: data/latest/")
    print("运行 `综投` 即可使用最新数据。")


if __name__ == "__main__":
    main()
