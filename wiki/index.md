# 惡劣天氣影像辨識 LLM Wiki — 目錄

> 主題：雨、霧、雪、低光、沙塵下，電腦視覺（物件偵測）為什麼會變差、有哪些對策、怎麼評估。
> 用途：碩士論文第 2.4 節文獻整理；第十週教學簡報的唯一知識來源。
> 規則見 [../CLAUDE.md](../CLAUDE.md)；變更紀錄見 [log.md](log.md)。

## 概念頁（concepts）

| ID | 頁面 | 一句話摘要 | 來源 |
|---|---|---|---|
| C1 | [天氣如何讓影像變差](concepts/weather-effects.md) | 對比下降、細節被遮、亮度失真；霧可用物理公式描述 | S1 S2 S4 S5 S6 |
| C2 | [路線一：先修圖再偵測](concepts/restoration-first.md) | 去雨／去霧後再偵測，常常沒幫助甚至更差 | S2 S4 S5 |
| C3 | [路線二：讓偵測器自己學修圖](concepts/adaptive-enhancement.md) | IA-YOLO、ERUP-YOLO：修圖模組和偵測器一起訓練 | S2 S6 |
| C4 | [路線三：合成 vs 真實資料](concepts/synthetic-vs-real.md) | 合成霧可幫助訓練，但測試一定要用真實資料 | S2 S3 S4 S5 S6 |
| C5 | [路線四：換一種眼睛（熱成像）](concepts/thermal-sensing.md) | 熱影像在夜間、霧、雨中仍看得到人 | S1 |
| C6 | [如何評估](concepts/evaluation.md) | 依天氣分組報告、晴天也要測、用真實測試集 | S1 S2 S4 S6 |

## 來源頁（sources）

| ID | 頁面 | 類型 | 狀態 |
|---|---|---|---|
| S1 | [Kristo et al. 2020 — 熱成像 + YOLO](sources/S1-kristo-thermal-yolo.md) | 期刊 IEEE Access | ⚠ 原文數字不一致 |
| S2 | [Liu et al. — IA-YOLO](sources/S2-ia-yolo.md) | arXiv | ⚠ 發表場合待查證 |
| S3 | [Kenk & Hassaballah 2020 — DAWN 資料集](sources/S3-dawn-dataset.md) | arXiv 資料集 | ✓ |
| S4 | [Hnewa & Radha — 雨天偵測回顧](sources/S4-hnewa-rain-review.md) | 期刊 IEEE SPM | ✓ |
| S5 | [Sakaridis et al. — Foggy Cityscapes](sources/S5-foggy-cityscapes.md) | arXiv | ⚠ 發表場合待查證 |
| S6 | [Ogino et al. 2024 — ERUP-YOLO](sources/S6-erup-yolo.md) | arXiv | ⚠ 發表場合待查證 |

## 術語表
[glossary.md](glossary.md) — 10 個初學者術語的白話定義（簡報第一次使用術語時必須引用）。

## 對應的教學簡報
[slides/index.html](../slides/index.html) — 「惡劣天氣下，AI 為什麼看不清楚？」每張投影片都標註它取材的 Wiki 頁面。
