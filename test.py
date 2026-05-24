# 1. Import your library file (make sure you are in the 'outlier' folder)
import pandas as pd
import outlier

data = pd.DataFrame({
    'ID'    : ['A', 'B', 'C', 'D', 'E', 'F'],
    'Name'  : ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Income': [50000, 60000, 55000, 70000, 65000, 1000000],
    'Score' : [10, 20, 300, 40, 50, 60]
})

# Default — all numeric columns
cleaned1 = outlier(data)

# Specific column
cleaned2 = outlier(data, columns=['Income'])

# Custom threshold
cleaned3 = outlier(data, columns=['Income'], threshold_iqr=1.0)

print(cleaned1)
print('---')
print(cleaned2)
print('---')
print(cleaned3)