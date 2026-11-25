---
id: G
title: 術語表（給初學者）
status: verified
updated: 2026-11-13
---

# 術語表

> v2 新增：簡報大綱階段就要列出每頁會用到的術語，術語必須先在這裡有白話定義，
> 投影片第一次出現時用 `<dfn>` 引用這裡的說法（由 `check_slides.py` 檢查）。

| 術語 | 白話解釋 | 相關頁 |
|---|---|---|
| 物件偵測 | 在影像中框出物體位置，並說出它是什麼 | [C1](concepts/weather-effects.md) |
| mAP | 同時考慮「框得準不準」與「有沒有漏掉」的綜合分數，越高越好 | [C6](concepts/evaluation.md) |
| AP | 單一類別的偵測分數；多個類別平均就是 mAP | [C6](concepts/evaluation.md) |
| mIoU | 預測區域和正確區域重疊的平均比例（用於影像分割） | [C4](concepts/synthetic-vs-real.md) |
| β | 霧的衰減係數，數字越大霧越濃；能見度約 2.996 ÷ β | [C1](concepts/weather-effects.md) |
| 熱成像 | 拍攝物體自身發出的熱（長波紅外線），不需要光 | [C5](concepts/thermal-sensing.md) |
| DIP | 可以和神經網路一起訓練的修圖濾鏡（去霧、白平衡、對比…） | [C3](concepts/adaptive-enhancement.md) |
| CNN-PP | 一個小型 CNN，看縮圖後決定每個濾鏡要開多強 | [C3](concepts/adaptive-enhancement.md) |
| RTTS | 收集真實霧天照片的測試資料集 | [C4](concepts/synthetic-vs-real.md) |
| OCR | 把影像中的文字讀成文字（車牌字元辨識） | [C6](concepts/evaluation.md) |
