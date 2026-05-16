import numpy as np
from typing import Union, List, Tuple

class OutlierDetector:
    """A library for detecting and filtering outliers in numerical data."""
    
    def __init__(self, data: Union[List[float], np.ndarray]):
        """Initialize with a list or numpy array of numbers."""
        self.data = np.array(data, dtype=float)

    def IQR_method(self, threshold: float = 1.5) -> Tuple[np.ndarray, np.ndarray]:
        """
        Detect outliers using the Interquartile Range (IQR) method.
        
        Formula: 
        IQR = Q3 - Q1
        Lower Bound = Q1 - (threshold * IQR)
        Upper Bound = Q3 + (threshold * IQR)
        """
        q1 = np.percentile(self.data, 25)
        q3 = np.percentile(self.data, 75)
        iqr = q3 - q1
        
        lower_bound = q1 - (threshold * iqr)
        upper_bound = q3 + (threshold * iqr)
        
        # Mask to find outliers
        outliers = self.data[(self.data < lower_bound) | (self.data > upper_bound)]
        cleaned_data = self.data[(self.data >= lower_bound) & (self.data <= upper_bound)]
        
        return outliers, cleaned_data

    def z_score_method(self, threshold: float = 3.0) -> Tuple[np.ndarray, np.ndarray]:
        """
        Detect outliers using the Z-Score method.
        
        Formula:
        Z = (X - mean) / std_dev
        An outlier is any point where |Z| > threshold.
        """
        mean = np.mean(self.data)
        std_dev = np.std(self.data)
        
        # Handle edge case where std_dev is 0 to avoid division by zero
        if std_dev == 0:
            return np.array([]), self.data
            
        z_scores = (self.data - mean) / std_dev
        
        outliers = self.data[np.abs(z_scores) > threshold]
        cleaned_data = self.data[np.abs(z_scores) <= threshold]
        
        return outliers, cleaned_data