# DR-Screening

AI-assisted diabetic retinopathy screening / decision-support system for
rural India (MathWorks Problem Statement 26038).

> This is a screening support prototype, **not a medical diagnosis**.
> Final decisions rest with a qualified ophthalmologist.

## Pipeline
Fundus image -> Quality check -> Preprocessing -> DR model (grade 0-4)
-> Confidence -> Referable DR? -> Grad-CAM -> Report -> MATLAB app

## Setup
1. py -3.11 -m venv .venv
2. .\.venv\Scripts\Activate.ps1
3. pip install -r requirements.txt
4. python tests/test_env.py

## Not in this repo
Datasets, API keys, and model weights (*.pth). Model weights are shared
via Google Drive; ask the ML owner.

## Team
M1 ML/Data | M2 Frontend (MATLAB) | M3 Backend/Integration | M4 Research/XAI/Docs
