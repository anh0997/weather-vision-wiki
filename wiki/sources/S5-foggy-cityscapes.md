---
id: S5
title: 用合成霧訓練：Foggy Cityscapes
status: needs-check
updated: 2026-11-13
---

# S5 Semantic Foggy Scene Understanding with Synthetic Data

**書目**：C. Sakaridis, D. Dai, L. Van Gool, arXiv:1708.07819（v3, 2019）。⚠ PDF 未註明期刊（一般引用為 IJCV 2018，待查證）。
**原文**：<https://arxiv.org/abs/1708.07819>

## 研究問題
真實霧天影像很少、很難標註。能不能把**晴天影像加上物理上合理的霧**，拿來訓練模型？

## 合成霧的方法
- Koschmieder 光學模型：I(x) = R(x)·t(x) + L·(1 − t(x))；R 為清晰場景、L 為大氣光。
- 透射率 t(x) = exp(−β·ℓ(x))，ℓ 為與相機的距離（由雙眼視差估計，再修補雜訊）。
- β 越大霧越濃；能見度 MOR = 2.996 / β。
- 使用 5 種 β：0.005、0.01、0.02、0.03、0.06，對應能見度約 600、300、150、100、50 m。

## 資料集
| 名稱 | 內容 |
|---|---|
| Foggy Cityscapes-refined | 550 張高品質合成霧影像（498 訓練、52 驗證），沿用 Cityscapes 標註 |
| Foggy Cityscapes-coarse | 約 20,000 張合成霧影像，標籤由模型產生 |
| Foggy Driving | 101 張**真實**霧天駕駛影像，作為測試基準 |

## 數字結果
- 語意分割：在真實霧天（Foggy Driving）mIoU 由 34.9% 提升到 37.8%。
- 物件偵測（Fast R-CNN）：用輕霧（β = 0.005）微調後，car AP 由 30.5% 升到 35.3%；person AP 維持 10.3%。
- **先去霧再辨識沒有明顯幫助**：MSCNN、DCP 等去霧前處理沒有一致的進步。

## 作者結論
用合成霧微調可以提升真實霧天的表現；合成資料是補足真實資料不足的可行方法。
