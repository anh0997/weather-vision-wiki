---
id: S6
title: ERUP-YOLO：一種濾鏡應付多種天氣
status: needs-check
updated: 2026-11-13
---

# S6 ERUP-YOLO: Enhancing Object Detection Robustness for Adverse Weather Condition by Unified Image-Adaptive Processing

**書目**：Y. Ogino, Y. Shoji, T. Toizumi, A. Ito（NEC），arXiv:2411.02799, 2024。⚠ 未註明正式發表場合。
**原文**：<https://arxiv.org/abs/2411.02799>

## 和 IA-YOLO（[S2](S2-ia-yolo.md)）的差別
| | IA-YOLO | ERUP-YOLO |
|---|---|---|
| 濾鏡 | 6 個傳統濾鏡（去霧、白平衡、Gamma…） | 2 個可微分濾鏡：Bézier 曲線像素濾鏡 (BPW)、核心式局部濾鏡 (KBL) |
| 調整 | 依天氣手動挑濾鏡與參數範圍 | 不需客製化 |
| 資料增強 | 針對霧／低光的專用增強 | 一種不分天氣的增強 |

## 資料與設定
- 訓練：只用晴天 PASCAL VOC + 模擬惡劣增強，**沒有用真實惡劣天氣資料訓練**。
- 測試：RTTS（真實霧）、ExDark（真實低光）、DAWN（霧、沙、雨、雪，見 [S3](S3-dawn-dataset.md)）。偵測器一律 YOLOv3。

## 數字結果（mAP50 %）

| 條件（資料集） | YOLOv3 | ERUP-YOLO |
|---|---|---|
| 正常（VOC） | 76.38 | 77.89 |
| 低光（ExDark） | 47.95 | 49.54 |
| 霧（RTTS） | 49.01 | 49.81 |
| 沙（DAWN） | 31.18 | 27.82 |
| 雨（DAWN） | 31.35 | 32.00 |
| 霧（DAWN） | 32.26 | 32.55 |
| 雪（DAWN） | 48.82 | 59.82 |

- 霧天 5 類模型在 RTTS：ERUP-YOLO 49.81，IA-YOLO 37.08。⚠ 與上表 YOLOv3 在 RTTS 的 49.01 來自不同實驗設定，不可直接互比。

## 限制
- **沙塵是唯一比原始 YOLOv3 差的條件**（27.82 vs 31.18）。
- 全域提亮會讓霧、沙中原本就亮的遠處區域過曝，造成漏偵測。
- 只在 YOLOv3 上驗證。
