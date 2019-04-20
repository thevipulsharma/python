# How to apply same operation to all rows of pandas series.

*Creating the series*
```python
import pandas as pd
import numpy as np

data = np.array([2, 4, 6, 8, 10])
series = pd.Series(data)
```

*Applying the operation*
```python
new_series = series.apply(lambda x: x**2)
```
