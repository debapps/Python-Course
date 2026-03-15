# NumPy

-   **NumPy** is a Python library, which supports efficient handling of various numerical operations on arrays holding numeric data.

-   These arrays are known as **N-dimensional arrays** or **ndarrays**.

-   Ndarrays are capable of holding data elements in multiple dimensions.

-   Each data element of a ndarray is of fixed size.

-   All elements of a ndarray are of same data type.

## N-dimensional array (ndarray)

-   **N-dimensional array** is an object, capable of holding data elements of same type and of a fixed size in multiple dimensions.

-   Creation of a 1-D array of five elements, from a list is shown in **Example 1**.

###### Example 1

```
import numpy as np
x = np.array([5, 8,
              9, 10,
              11]) # using 'array' method

type(x)   # Displays type of array 'x'
```

###### Output

`numpy.ndarray`

-   Creation of a 2-D array from a list of lists is shown in **Example 2**.

###### Example 2

```
y = np.array([[6, 9, 5],
              [10, 82, 34]])
print(y)
```

###### Output

```
array([[ 6,  9,  5],
       [10, 82, 34]])
```

### ndarray Attributes

Some of the important attributes of a ndarray are

-   **ndim** : Returns number of dimensions.

-   **shape** : Returns Shape in tuple.

-   **size** : Total number of elements.

-   **dtype** : Type of each element.

-   **itemsize** : Size of each element in Bytes.

-   **nbytes** : Total bytes consumed by all elements.

-   **flags** : Information about the memory layout of the array.

###### Example 3

```
print(y.ndim, y.shape, y.size, y.dtype, y.itemsize, y.nbytes)
```

###### Output

`2 (2, 3) 6 int32 4 24`

### Numpy dtypes

-   **Numpy** supports various data types based on number of bytes required by the data elements.

-   Data type can be explicitly specified with **dtype** argument.

-   A ndarray, holding float values is defined in **Example 4**.

###### Example 4

```
y = np.array([[6, 9, 5],
              [10, 82, 34]],
             dtype=np.float64)
print(y)
print(y.dtype)
```

###### Output

```
array([[  6.,   9.,   5.],
       [ 10.,  82.,  34.]])
float64
```

## Numpy Array creation

N-dimensional arrays or ndarray can be created in multiple ways in numpy.

-   From Python built-in datatypes : **lists or tuples**.

-   Using Numpy array creation methods like **ones, ones_like, zeros, zeros_like**.

-   Using Numpy numeric sequence generators.

-   Using Numpy **random** module.

-   By reading data from a file.

### ndarrays from Lists

-   Data available in lists, or tuples can be converted into numpy arrays using **array** method.

-   Creating a 3-Dimensional array from a list of list of lists is shown in **Example 5**.

###### Example 5

```
import numpy as np
a = [[[4.1, 2.5], [1.1, 2.3], [9.1, 2.5]],
     [[8.6, 9.9],[3.6, 4.3], [6.6, 0.3]]]

x = np.array(a, dtype='float64')

type(x), x.ndim, x.shape
```

###### Output

`numpy.ndarray, 3, (2, 3, 2)`

### Array Creation Methods

Numpy allows creation of arrays with default values like **0, 1**, or another value.

###### Example 6: Using **zeros** method

```
x = np.zeros(shape=(2,4))
print(x)
```

###### Output

```
[[ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]]
```

###### Example 7: Using **ones** method

```
x = np.ones(shape=(3,2))
print(x)
print(type(x), x.ndim, x.shape)
```

###### Output

```
[[1. 1.]
 [1. 1.]
 [1. 1.]]
<class 'numpy.ndarray'> 2 (3, 2)
```

###### Example 8: Using **full** method

```
y = np.full(shape=(2,3), fill_value=10.5)
print(y)
```

###### Output

```
[[ 10.5  10.5  10.5]
 [ 10.5  10.5  10.5]]
```

###### Example 9: Using **eye** method

```
# np.eye(n, m) defines a 2D identity matrix.
# The elements where i=j (row index and column index are equal) are 1 and the rest are 0.
x = np.eye(3)
x
```

###### Output

```
array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])
```

### Numeric Sequence Generators

Two major methods used in numpy for generating number sequences are:

-   **arange** : Numbers created based on step value.

Syntax - `numpy.arange([start, ]stop, [step, ]dtype=None)`

-   **linspace** : Numbers created based on size value.

Syntax - `numpy.linspace(start, stop, #num of elements, endpoint=True, retstep=False, dtype=None)`

###### Example 10

```
x = np.arange(3, 15, 2.5) # 2.5 is step
print(x)
```

###### Output

`[ 3. 5.5 8. 10.5 13. ]`

###### Example 11

```
y = np.linspace(3, 15, 5) # 5 is size of array 'y'
print(y)
```

###### Output

`[  3.   6.   9.  12.  15.]`

### Random Numbers Generator

-   **random** module of numpy is used to generate various random sequences.

-   The **numpy.random** module implements pseudo-random number generators (PRNGs or RNGs, for short) with the ability to draw samples from a variety of probability distributions.

-   The method **default_rng()** is used to create a random number generator that is used to obtain samples from different distributions.

###### Example 12: Generate one random float uniformly distributed over the range [0, 1).

```
import numpy as np
rng = np.random.default_rng()
rng.random()
```

###### Output

`0.3887124566072844`

###### Example 13: Generate random 1-D array where each element is in range [0, 1).

```
import numpy as np
rng = np.random.default_rng()
rng.random(size=5)
```

###### Output

```
array([0.14305195, 0.71664228, 0.90514551, 0.03610985, 0.00190964])
```

###### Example 14: Generate random 2-D array where each element is in range [0, 1).

```
import numpy as np
rng = np.random.default_rng()
rand_arr1 = rng.random(size=(3, 4))
rand_arr1
```

###### Output

```
array([[0.76922946, 0.11442958, 0.88711608, 0.41428929],
       [0.61415785, 0.30272748, 0.13502465, 0.59005234],
       [0.70494709, 0.78416928, 0.49687105, 0.05108679]])
```

###### Example 15: Generate random 2-D array where each element is integer and in range 5-60.

```
import numpy as np
rng = np.random.default_rng()
rand_arr2 = rng.integers(5, 60, size=(4, 5))
rand_arr2
```

###### Output

```
array([[41, 16, 16, 26, 25],
       [25, 27, 42, 38,  5],
       [35, 55, 20, 56, 11],
       [38, 36,  7, 50,  6]])
```

###### Example 16: Generate an array of 10 numbers according to a unit Gaussian distribution.

```
import numpy as np
rng = np.random.default_rng()
rand_arr3 = rng.standard_normal(10)
rand_arr3
```

###### Output

```
array([ 0.33444614, -1.02642213, -0.91890124, -0.83186843,  0.89411245,
       -0.93327722,  1.83670347,  1.05883785, -0.58726627,  0.11031023])
```

###### Example 17: Generate an array of 10 numbers in normal distribution with mean 10 and standard deviation 2.

```
import numpy as np
rng = np.random.default_rng()

# Generate an array of 10 numbers in normal distribution with mean 10 and standard deviation 2.
rand_arr4 = 10 + 2 * rng.standard_normal(10)
print(rand_arr4)

# Calculate Mean and Standard Deviation.
print(f'Mean: {rand_arr4.mean()}\nSTD: {rand_arr4.std()}')
```

###### Output

```
[10.04838881  8.75430363 10.29402119 13.93189795  9.89016015 12.38768006
 13.51551117 11.88511442 11.07772433  8.06116479]
Mean: 10.984596649256368
STD: 1.8426120868182372
```

### Reading Data from a file

**loadtxt** is used to read data from a text file or any input data stream.

###### Example 18:

```
from io import StringIO
import numpy as np

x = StringIO('''88.25 93.45 72.60 90.90
72.3 78.85 92.15 65.75
90.5 92.45 89.25 94.50
''')

d = np.loadtxt(x,delimiter=' ')

print(d)

print(d.ndim, d.shape)
```

###### Output

```
[[ 88.25  93.45  72.6   90.9 ]
 [ 72.3   78.85  92.15  65.75]
 [ 90.5   92.45  89.25  94.5 ]]
2 (3, 4)
```
