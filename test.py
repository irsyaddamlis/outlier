# 1. Import your library file (make sure you are in the 'outlier' folder)
from outlier import OutlierDetector

# 2. Define the sample data
sample_data = [10, 12, 12, 13, 12, 11, 14, 13, 100, 12, 11, -50, 13]

# 3. Create the detector instance
detector = OutlierDetector(sample_data)

# 4. Calculate the z-scores (This creates the 'z_cleaned' variable!)
z_outliers, z_cleaned = detector.z_score_method(threshold=1.5)
iqr_outliers, iqr_cleaned = detector.IQR_method(threshold=1.5)

# 5. Now this line will work perfectly
print(f"Cleaned Data:      {z_cleaned}")
print(f"IQR Outliers:     {iqr_cleaned}")