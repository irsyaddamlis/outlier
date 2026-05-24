# outlier

A lightweight Python library for automatically detecting and removing outliers from pandas DataFrames. It selects the best method (IQR or Z-Score) per column based on data distribution.

---

## Installation

```bash
pip install git+https://github.com/yourname/outlier.git
```

---

---

## Update

```bash
pip3 install --force-reinstall --user --no-cache-dir git+https://github.com/irsyaddamlis/outlier.git
```

---

## Requirements

- Python >= 3.8
- pandas
- numpy
- scipy

---

## Quick Start

```python
import pandas as pd
import outlier

data = pd.DataFrame({
    'ID'    : ['A', 'B', 'C', 'D', 'E', 'F'],
    'Name'  : ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Income': [50000, 60000, 55000, 70000, 65000, 1000000],
    'Score' : [10, 20, 300, 40, 50, 60]
})

cleaned = outlier(data)
print(cleaned)
```

**Output:**
```
  ID     Name  Income  Score
0  A    Alice   50000     10
1  B      Bob   60000     20
2  C  Charlie   55000     30
3  D    David   70000     40
4  E      Eve   65000     50
```

---

## How It Works

For each numeric column, the library runs a **Shapiro-Wilk normality test** to decide which method to use:

| p-value | Distribution | Method Selected |
|---------|-------------|-----------------|
| > 0.05  | Normal      | Z-Score         |
| ≤ 0.05  | Skewed      | IQR             |

### IQR Method
```
IQR        = Q3 - Q1
Lower Bound = Q1 - (threshold × IQR)
Upper Bound = Q3 + (threshold × IQR)
```

### Z-Score Method
```
Z = (X - mean) / std_dev
Outlier if |Z| > threshold
```

---

## Usage

### Default — Clean All Numeric Columns

```python
import pandas as pd
import outlier

data = pd.DataFrame({
    'ID'    : ['A', 'B', 'C', 'D', 'E', 'F'],
    'Name'  : ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Income': [50000, 60000, 55000, 70000, 65000, 1000000],
    'Score' : [10, 20, 300, 40, 50, 60]
})

cleaned = outlier(data)
```

Non-numeric columns (`ID`, `Name`) are automatically skipped.

---

### Specific Column Only

```python
cleaned = outlier(data, columns=['Income'])
```

Only `Income` is cleaned — `Score` outliers are kept.

---

### Multiple Specific Columns

```python
cleaned = outlier(data, columns=['Income', 'Score'])
```

---

### Custom Threshold

```python
# Stricter IQR (default: 1.5)
cleaned = outlier(data, threshold_iqr=1.0)

# Stricter Z-Score (default: 3.0)
cleaned = outlier(data, threshold_z=2.0)

# Combined
cleaned = outlier(data, columns=['Income'], threshold_iqr=1.0)
```

---

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `df` | `pd.DataFrame` | required | Input DataFrame |
| `columns` | `List[str]` | `None` | Columns to clean. `None` = all numeric columns |
| `threshold_iqr` | `float` | `1.5` | Multiplier for IQR bounds |
| `threshold_z` | `float` | `3.0` | Max allowed Z-Score |

---

## Project Structure

```
outlier-project/
├── pyproject.toml         # package metadata & dependencies
├── .gitignore
├── README.md
├── outlier/               # library package
│   ├── __init__.py        # entry point, makes module callable
│   └── detector.py        # core logic
└── test.py                # usage example
```

---

## Version

```python
import outlier
print(outlier.__version__)
```

---

## License

Arch-Notions
