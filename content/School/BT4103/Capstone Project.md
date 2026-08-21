---
class: project
tags:
  - y4s1
source:
related:
  - "[[BT4103]]"
author:
date: 2026-08-20
updated: 2026-08-20
aliases:
  - CFTC Positioning Nowcast
---
# BT4103 Business Analytics Capstone Project Proposal
*Industry Partner: Dymon Asia*

## Part 1: Project Information
### Project Name
CFTC Positioning Nowcast and Price-Action Crowding Dashboard
### Project Description
- Develop a cross-asset analytics platform that combines weekly CFTC Commitments of Traders data with daily price action to estimate how speculative positioning evolves between official releases.
- Create a standardized data pipeline across FX, rates, equity indices, energy, metals and agricultural futures, mapping relevant participant categories such as Managed Money and Leveraged Funds.
- Engineer features from returns, momentum, volume, open interest, volatility, futures-curve structure and cross-asset macro variables; compare regularized regression and tree-based models using time-series cross-validation.
- Produce interpretable positioning and crowding indicators, including historical percentile/z-score, new-long versus short-covering classification, long-liquidation versus new-short classification, price-positioning divergence and squeeze/reversal-risk scores.
- The platform will be a research and decision-support tool, not an autonomous trading or execution system.
### Total Workload
Approximately 16 hours per week per student for 12 weeks (team of 3-5 students).
### Project Data Sources
Public CFTC historical Commitments of Traders data; Price/Volume per instrument yfinance api.
### Platform and Tools
Python (pandas, NumPy, scikit-learn, statsmodels, XGBoost/LightGBM, SHAP), SQL, Git, Jupyter, and Streamlit or Power BI for dashboard development.

### Project Deliverables
- Automated and reusable data ingestion, cleaning and contract-mapping pipeline.
- Validated positioning-nowcast models with walk-forward testing, confidence ranges and feature interpretation.
- Interactive cross-asset dashboard showing reported positions, estimated current positions, crowding scores, divergences and regime classifications.
- Reusable codebase, technical documentation, model evaluation report and final presentation.

