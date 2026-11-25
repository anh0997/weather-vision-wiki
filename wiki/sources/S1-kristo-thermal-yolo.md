---
id: S1
title: 熱成像 + YOLO：惡劣天氣下的人員偵測
status: needs-check
updated: 2026-11-13
---

# S1 Thermal Object Detection in Difficult Weather Conditions Using YOLO

**書目**：M. Kristo, M. Ivasic-Kos, M. Pobar, IEEE Access, vol. 8, 2020. DOI 10.1109/ACCESS.2020.3007481
**原文**：<https://airi.uniri.hr/wp-content/uploads/2020/07/ACCESS3007481_final.pdf>

## 研究問題
為 RGB 影像設計的 CNN 偵測器，能不能在**夜間熱成像（LWIR）監視影像**中，於晴天、濃霧、大雨下偵測行人？

## 資料
- 攝影機：FLIR ThermaCAM P10（感測器 320×240），冬季夜間拍攝。
- 自建資料集 UNIRI-TID；天氣：晴天（約 2 °C）、濃霧（能見度 < 5 m）、大雨。
- 標註影格：晴天 2,663、霧 1,135、雨 2,313，共 6,111。⚠ 前言寫的是「7412 張」，兩處不一致。
- 類別：Person（另有加入 Dog 的子資料集）。

## 方法
先比較 Faster R-CNN、SSD、FCOS、Cascade R-CNN、YOLOv3，因 YOLOv3 速度最快（約 27.5 FPS）而選用，再以熱影像微調。

## 數字結果

| 模型 | 說明 | AP |
|---|---|---|
| bY | 原始 COCO 預訓練 YOLOv3 | 19.63% |
| tY | 用熱影像訓練 | 97.93% |
| tY（晴／霧／雨） | 依天氣分開測 | 97.85% / 97.85% / 98.08% |
| tY_clear | 只用晴天資料訓練 | 79.39% |

- 只用 10% 晴天資料訓練，結果與 80% 相近（作者用語：comparative）。
- 換到其他公開熱影像資料集：Terravic Motion 約 97% mAP；KAIST 等拍攝條件差很多的資料集約 35% mAP。

## 作者結論
- 用熱影像微調後，偵測效果遠勝 RGB 預訓練模型。
- 晴天訓練的模型轉到雨天尚可，但**霧的影響遠大於雨**。

## 限制
- 單一地點、單一攝影機、只有冬季夜晚；只測人與狗。
- ⚠ 文中數字有多處不一致（總張數 7412 vs 6111；訓練張數 4270 vs 約 3000；結論說 tY_clear「接近 100%」但結果表是 79.39%）。本 Wiki 一律採用**結果章節的表格數字**。
