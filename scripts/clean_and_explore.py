"""
Exploratory audit of the SECOM semiconductor manufacturing dataset.

Purpose:
- Load and verify alignment of raw process measurements and labels
- Assess data quality (missingness, variance, redundancy)
- Identify candidate features for removal or special handling
- Summarize dataset characteristics prior to preprocessing and modeling

Notes:
- This script is exploratory and diagnostic only.
- No modeling or feature selection for prediction is performed here.
- All decisions made here are reported, not applied irreversibly.

Outputs:
- Summary tables and reports used to justify downstream preprocessing choices.
"""

# only time something should be printed is when you can answer im printing this because I want to know: 