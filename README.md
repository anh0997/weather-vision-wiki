# 惡劣天氣影像辨識 LLM Wiki ＋ 教學 HTML 簡報

第十週作業｜丁國英（勤益科大 電機碩一乙）

- **教學簡報**：https://anh0997.github.io/weather-vision-wiki/slides/
- **LLM Wiki**：[wiki/index.md](wiki/index.md)（6 篇來源、6 個概念頁、術語表、log）
- **Wiki 規則**：[CLAUDE.md](CLAUDE.md)
- **Loop / Graph 設計**：[workflow/graph.md](workflow/graph.md)
- **實際執行紀錄**：[workflow/run-log.md](workflow/run-log.md)
- **反思**：[workflow/reflection.md](workflow/reflection.md)

## 檢查工具
```bash
python workflow/lint_wiki.py      # Wiki：引用、連結、孤兒頁、數字回溯
python workflow/check_slides.py   # 簡報：數字可追溯、術語已定義、字數
```
