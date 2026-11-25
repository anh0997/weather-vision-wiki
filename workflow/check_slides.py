"""簡報檢查節點：每張投影片
  (1) data-wiki 指到的 Wiki 頁面必須存在
  (2) 數字檢查：投影片上的數字必須出現在它引用的 Wiki 頁面
  (3) 初學者檢查：專有名詞第一次出現時必須用 <dfn> 解釋；每頁文字量不可過多
用法：python workflow/check_slides.py   （有錯誤時回傳 1，代表要重新生成該頁）
"""
import re, sys, html, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
deck = (ROOT / "slides" / "index.html").read_text(encoding="utf-8")
slides = re.findall(r'<section class="slide[^"]*" data-wiki="([^"]*)" data-src="([^"]*)">(.*?)</section>', deck, re.S)

# v2：術語清單改由 Wiki 的 glossary.md 提供（檢查往前移到 Wiki 階段）
GLOSS = (ROOT / "wiki" / "glossary.md").read_text(encoding="utf-8")
JARGON = re.findall(r"^\| ([^|]+?) \| [^|]+ \| \[C", GLOSS, re.M)
MAX_CHARS = 330          # 每頁可見文字上限（不含頁尾）
NUM = re.compile(r"\d[\d,]*\.\d+|\d[\d,]{2,}|\d+(?=\s?(?:%|m\b|ms\b|張|個框))")
IGNORE = {"2.996"}       # 公式常數，已在 S5/C1 出現，這裡僅示範可加白名單

def visible(s):
    s = re.sub(r'<div class="src">.*?</div>', " ", s, flags=re.S)          # 頁尾
    attrs = " ".join(re.findall(r'data-(?:v|why)="([^"]*)"', s))            # 長條圖數值與解析也算
    s = re.sub(r"<[^>]+>", " ", s)
    return html.unescape(s + " " + attrs)

seen, errors, rows = set(), [], []
for n, (wiki, src, body) in enumerate(slides, 1):
    errs = []
    pages = [p for p in wiki.split() if p]
    text_wiki = ""
    for p in pages:
        f = ROOT / "wiki" / p
        if not f.exists():
            errs.append(f"Wiki 頁面不存在：{p}")
        else:
            text_wiki += f.read_text(encoding="utf-8").replace(",", "")
    text = visible(body)
    # (2) 數字
    for num in NUM.findall(text):
        k = num.replace(",", "")
        # 用邊界比對，避免「20」因為「2020」而誤判通過
        if k in IGNORE or re.search(r"(?<![\d.])" + re.escape(k) + r"(?![\d])", text_wiki):
            continue
        errs.append(f"數字 {num} 不在引用的 Wiki 頁 {pages}")
    # (3a) 術語第一次出現要有 <dfn>
    dfns = " ".join(re.findall(r"<dfn[^>]*>(.*?)</dfn>", body))
    for term in JARGON:
        pat = r"(?<![A-Za-z])" + re.escape(term) + r"(?![A-Za-z])"
        if term not in seen and re.search(pat, text):
            if term not in dfns:
                errs.append(f"術語「{term}」第一次出現但沒有解釋（<dfn>）")
            seen.add(term)
    # (3b) 文字量
    chars = len(re.sub(r"\s", "", text))
    if chars > MAX_CHARS:
        errs.append(f"文字太多：{chars} 字（上限 {MAX_CHARS}）")
    rows.append((n, pages, chars, errs))
    errors += [f"第 {n} 頁：{e}" for e in errs]

for n, pages, chars, errs in rows:
    print(f"{'✓' if not errs else '✗'} 第 {n:2d} 頁｜{chars:3d} 字｜Wiki: {', '.join(pages)}")
    for e in errs:
        print(f"      - {e}")
print(f"\n共 {len(slides)} 頁，{len(errors)} 個問題")
sys.exit(1 if errors else 0)
