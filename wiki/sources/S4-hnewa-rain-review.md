---
id: S4
title: 雨天物件偵測回顧：去雨反而讓偵測變差
status: verified
updated: 2026-11-13
---

# S4 Object Detection Under Rainy Conditions for Autonomous Vehicles: A Review of State-of-the-Art and Emerging Techniques

**書目**：M. Hnewa, H. Radha, IEEE Signal Processing Magazine, 2021. DOI 10.1109/MSP.2020.2984801（arXiv:2006.16471）
**原文**：<https://arxiv.org/abs/2006.16471>

## 雨如何讓影像變差
- **雨絲**：降低對比、讓畫面變白（low contrast and elevated whiteness）。
- 雨滴擋住部分光線，造成亮度變化；擋風玻璃上的雨滴形狀多變，雨刷會讓情況一直改變。
- 結果：遮蔽並扭曲偵測器依賴的視覺特徵。

## 三類對策
| 類別 | 做法 | 例子 |
|---|---|---|
| 去雨 (deraining) | 偵測前先把雨移除 | DDN、DeRaindrop、PReNet |
| 影像轉換 (image translation) | 把晴天訓練圖轉成雨天風格 | UNIT |
| 領域適應 (domain adaptation) | 讓特徵在晴／雨之間不變 | Domain Adaptive Faster R-CNN |

## 實驗設定
資料：BDD100K，分為晴天訓練、晴天測試、**人工確認過的真實雨天測試**；4 類：vehicle、pedestrian、traffic light、traffic sign。偵測器：Faster R-CNN、YOLOv3。

## 數字結果（mAP）

| 條件 | Faster R-CNN | YOLOv3 |
|---|---|---|
| 晴天 | 44.45 | 52.62 |
| 雨天（不處理） | 39.00 | 49.39 |
| 雨天 + DDN 去雨 | 37.78 | 47.94 |
| 雨天 + DeRaindrop | 36.32 | 46.66 |
| 雨天 + PReNet | 34.29 | 44.36 |
| 雨天 + UNIT 影像轉換 | 39.07 | 49.48 |
| 雨天 + 領域適應 | 39.24 | 不適用 |

- **所有去雨方法都讓 mAP 下降**。推測原因：去雨會把物體邊緣磨平、移除有用特徵；且去雨模型多用合成雨與靜態場景訓練。
- 小物件受影響最大：行人與紅綠燈的 AP 下降比車輛與交通標誌多。

## 作者結論
1. 最根本的問題是**缺少有標註的雨天資料**。
2. 生成模型（如 UNIT）可望補充訓練資料。
3. 需要新的偵測架構；**單靠去雨不可行**。
