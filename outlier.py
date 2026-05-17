import pandas as pd
import numpy as np
from scipy import stats
from typing import Optional, List

class _OutlierDetector:
    """Internal class — use OutlierDetector() function instead."""

    def __init__(self, threshold_iqr: float = 1.5, threshold_z: float = 3.0):
        self.threshold_iqr = threshold_iqr
        self.threshold_z = threshold_z

    def _detect_method(self, series: pd.Series) -> str:
        _, p_value = stats.shapiro(series)
        return "z_score" if p_value > 0.05 else "iqr"

    def _get_mask(self, series: pd.Series, method: str) -> pd.Series:
        if method == "iqr":
            q1, q3 = series.quantile(0.25), series.quantile(0.75)
            iqr = q3 - q1
            return series.between(q1 - self.threshold_iqr * iqr, q3 + self.threshold_iqr * iqr)
        else:
            return np.abs(stats.zscore(series)) <= self.threshold_z

    def clean(self, df: pd.DataFrame, columns: Optional[List[str]] = None) -> pd.DataFrame:
        result = df.copy()
        target_cols = columns if columns else result.select_dtypes(include=[np.number]).columns.tolist()

        invalid = [col for col in target_cols if col not in result.columns]
        if invalid:
            raise ValueError(f"Columns not found in DataFrame: {invalid}")

        for col in target_cols:
            method = self._detect_method(result[col])
            mask = self._get_mask(result[col], method)
            print(f"Column '{col}': {method.upper()} → {(~mask).sum()} outlier(s) removed")
            result = result[mask]

        return result.reset_index(drop=True)


def OutlierDetector(
    df: pd.DataFrame,
    columns: Optional[List[str]] = None,
    threshold_iqr: float = 1.5,
    threshold_z: float = 3.0
) -> pd.DataFrame:
    """
    Auto-detect and remove outliers from a DataFrame.

    - columns=None          → clean all numeric columns (default)
    - columns=['Income']    → clean specific column(s) only
    """
    return _OutlierDetector(threshold_iqr, threshold_z).clean(df, columns)