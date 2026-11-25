"""Wiki lint：檢查引用、連結、孤兒頁、待查證項目，以及「概念頁的數字是否真的出現在它引用的來源頁」。
用法：python workflow/lint_wiki.py
"""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent / "wiki"
pages = {p: p.read_text(encoding="utf-8") for p in ROOT.rglob("*.md")}
src_text = {}
for p, t in pages.items():
    m = re.search(r"^id:\s*(S\d+)", t, re.M)
    if m:
        src_text[m.group(1)] = t

problems, warns = [], []
linked = set()

for p, t in pages.items():
    rel = p.relative_to(ROOT)
    # 1) 引用的來源必須存在
    for sid in set(re.findall(r"\[(S\d+)\]", t)):
        if sid not in src_text:
            problems.append(f"{rel}: 引用不存在的來源 {sid}")
    # 2) 相對連結必須存在
    for link in re.findall(r"\]\(([^)#]+\.md)\)", t):
        target = (p.parent / link).resolve()
        if not target.exists():
            problems.append(f"{rel}: 連結失效 {link}")
        linked.add(target)
    # 3) 待查證項目
    for line in t.splitlines():
        if "⚠" in line:
            warns.append(f"{rel}: {line.strip()[:70]}")
    # 4) 概念頁：每一行帶 [S#] 的數字，必須出現在其中至少一個被引用來源頁
    if rel.parts[0] == "concepts":
        body = t.split("---", 2)[-1]                     # 跳過 frontmatter
        section, own = [], False                         # 標題上的引用，往下繼承
        for line in body.splitlines():
            if line.startswith("#"):
                section = re.findall(r"\[(S\d+)\]", line)
                own = "自己的實驗" in line
                continue
            if "[自己的實驗]" in line or own:
                continue
            cites = re.findall(r"\[(S\d+)\]", line) or section
            if not cites:
                continue
            clean = re.sub(r"\[S\d+\]|S\d+|C\d+|YOLOv\d+|\d+×\d+", "", line).replace(",", "")
            nums = re.findall(r"\d+\.\d+|\d{2,}", clean)
            for n in nums:
                if not any(n in src_text.get(c, "").replace(",", "") for c in cites):
                    problems.append(f"{rel}: 數字 {n} 不在引用來源 {cites} 中 → 「{line.strip()[:50]}…」")

# 5) 孤兒頁（沒有任何頁面連到它）
for p in pages:
    if p.name not in ("index.md", "log.md") and p.resolve() not in linked:
        problems.append(f"{p.relative_to(ROOT)}: 孤兒頁（沒有被連結）")

print(f"檢查 {len(pages)} 頁")
print(f"\n❌ 問題 {len(problems)} 項")
for x in problems: print("  -", x)
print(f"\n⚠ 待查證 {len(warns)} 項")
for x in warns: print("  -", x)
sys.exit(1 if problems else 0)
