---
id: S3
title: DAWN：真實惡劣天氣車輛偵測資料集
status: verified
updated: 2026-11-13
---

# S3 DAWN: Vehicle Detection in Adverse Weather Nature Dataset

**書目**：M. A. Kenk, M. Hassaballah, arXiv:2008.05402, 2020.
**原文**：<https://arxiv.org/abs/2008.05402>

## 為什麼做這個資料集
多數駕駛場景演算法都在合成影像或少量真實影像上測試，在低能見度下的真實表現並不清楚。DAWN 提供**真實**惡劣天氣交通影像作為基準。

## 資料內容
- **1,000 張**真實交通影像，四種天氣：霧、雪、雨、沙塵暴。⚠ 原文未列出各類別張數。
- 場景：市區、公路、高速公路。
- 來源：用關鍵字（如 foggy、sleet rain、sandstorm）在 Google、Bing 搜尋，再由人工挑選；授權需為可自由分享使用。
- 標註：LabelMe 標框，共 **7,845** 個框；類別：car、bus、truck、motorcycle/bicycle、person。
- 類別分布：car 82.21%、truck 8.22%、person 6.07%、bus 2.05%、motorcycle+bicycle 1.36%。

## 數字結果
原文本身**沒有**提供偵測器在 DAWN 上的結果（後續論文如 [S6](S6-erup-yolo.md) 有使用 DAWN 評估）。

## 限制
- 只有 1,000 張，規模小；類別極度偏向汽車（82.21%）。
- 多樣性受限於搜尋引擎找得到的照片。
