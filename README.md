# Order Params Coupling

### To get symmetry
To use *read_symmetry_from_file* from *utils.py* like this:
```python
from utils import read_symmetry_from_file
symmetry = read_symmetry_from_file("sample.xcl")
```
which calls the function provided by *spglib*.

### To get order params
```python
from utils import read_orders_from_file
orders = read_orders_from_file("sample.xcl")
```

### To render 3D image
```python
from utils import display
display(order)
```
