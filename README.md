<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>NumPy Detailed Explanation</title>
</head>
<body>

<h1>NumPy File – Complete Detailed Explanation</h1>

<hr>

<h2>1. Importing NumPy Library</h2>
<pre>
import numpy as np
</pre>

<p>
NumPy is a powerful Python library used for numerical and scientific computing.
It provides support for multi-dimensional arrays, mathematical functions,
linear algebra, statistics, and much more.
The alias <b>np</b> is used to make function calls shorter and readable.
</p>

<hr>

<h2>2. Exploring NumPy Built-in Functions</h2>
<pre>
dir(np)
len(dir(np))
</pre>

<p>
<b>dir(np)</b> displays all built-in functions, attributes, and methods available in NumPy.
This helps in understanding how extensive the NumPy library is.
</p>

<p>
<b>len(dir(np))</b> returns the total number of available functions and attributes in NumPy,
showing the size and capability of the library.
</p>

<hr>

<h2>3. Creating a One-Dimensional (1D) Array</h2>
<pre>
a = np.array([10, 14, 24, 35, 60])
print(a)
print(a.ndim)
print(a.shape)
</pre>

<p>
<b>np.array()</b> converts a Python list into a NumPy array.
</p>

<ul>
    <li><b>a.ndim</b> → Returns the number of dimensions (1D array)</li>
    <li><b>a.shape</b> → Returns the structure of the array (5 elements)</li>
</ul>

<hr>

<h2>4. Indexing in 1D Array</h2>
<pre>
print(a[2])
</pre>

<p>
NumPy uses zero-based indexing. Accessing index <b>2</b> returns the third element in the array.
</p>

<hr>

<h2>5. Creating NumPy Array Using Loop</h2>
<pre>
t = []
for i in range(1, 11):
    t.append(i)
a = np.array(t)
</pre>

<p>
A Python list is first created using a loop and then converted into a NumPy array
using <b>np.array()</b>.
</p>

<hr>

<h2>6. Creating a Two-Dimensional (2D) Array</h2>
<pre>
a = np.array([[10,3,6],[4,5,8],[9,2,6]])
print(a)
print(a.ndim)
print(a.shape)
print(a.size)
</pre>

<ul>
    <li><b>ndim</b> → 2 (2D array)</li>
    <li><b>shape</b> → (3, 3) → 3 rows and 3 columns</li>
    <li><b>size</b> → Total number of elements (9)</li>
</ul>

<hr>

<h2>7. Indexing in 2D Array</h2>
<pre>
print(a[1][2])
</pre>

<p>
Accesses the element in second row and third column.
</p>

<hr>

<h2>8. Reshaping 1D Array into 2D Array</h2>
<pre>
a = np.array([10,3,4,6,8,54])
b = a.reshape(2,3)
</pre>

<p>
<b>reshape()</b> changes the shape of the array without changing the data.
The total number of elements must remain the same.
</p>

<hr>

<h2>9. Creating Arrays Using arange()</h2>
<pre>
a = np.arange(1, 11)
</pre>

<p>
<b>np.arange()</b> generates evenly spaced values within a given range
and returns them as a NumPy array.
</p>

<hr>

<h2>10. Reshape Using -1</h2>
<pre>
b = a.reshape(2, -1)
</pre>

<p>
Using <b>-1</b> allows NumPy to automatically calculate the appropriate dimension.
</p>

<hr>

<h2>11. Creating Large 2D Array</h2>
<pre>
a = np.arange(1, 61).reshape(10, 6)
</pre>

<p>
Creates numbers from 1 to 60 and reshapes them into 10 rows and 6 columns.
</p>

<hr>

<h2>12. Creating a Three-Dimensional (3D) Array</h2>
<pre>
b = a.reshape(5, 2, 6)
</pre>

<p>
The array is reshaped into 3D format containing depth, rows, and columns.
</p>

<hr>

<h2>13. Statistical Functions</h2>
<pre>
np.sum(a)
np.mean(a)
np.max(a)
np.min(a)
</pre>

<ul>
    <li><b>np.sum()</b> → Returns sum of all elements</li>
    <li><b>np.mean()</b> → Returns average value</li>
    <li><b>np.max()</b> → Returns maximum value</li>
    <li><b>np.min()</b> → Returns minimum value</li>
</ul>

<hr>

<h2>14. Axis-Based Operations</h2>
<pre>
np.sum(a, axis=1)
np.sum(a, axis=0)
</pre>

<p>
<b>axis=0</b> performs column-wise operations<br>
<b>axis=1</b> performs row-wise operations
</p>

<hr>

<h2>15. Finding Index Positions</h2>
<pre>
np.argmax(a)
np.argmin(a)
</pre>

<p>
<b>argmax()</b> returns index of maximum value and
<b>argmin()</b> returns index of minimum value.
</p>

<hr>

<h2>16. Repeat Function</h2>
<pre>
b = a.reshape(1, -1)
c = np.repeat(b, 5, axis=0)
</pre>

<p>
<b>np.repeat()</b> repeats array elements along a specified axis.
</p>

<hr>

<h2>17. Arithmetic Operations on Arrays</h2>
<pre>
np.add(a, b)
np.subtract(a, b)
np.multiply(a, b)
</pre>

<p>
These functions perform element-wise arithmetic operations efficiently.
</p>

<hr>

<h2>18. Matrix Multiplication</h2>
<pre>
np.matmul(a, b)
</pre>

<p>
<b>np.matmul()</b> performs matrix multiplication following linear algebra rules.
</p>

<hr>

<h2>19. Conditional Logic with NumPy Arrays</h2>
<pre>
for i in a:
    for j in i:
        if j % 2 == 0:
            print(j)
</pre>

<p>
This loop demonstrates how NumPy arrays can be iterated using Python loops
to apply conditions like checking even numbers.
</p>

<hr>

<h2>20. Summary of NumPy Built-in Functions Used</h2>

<table border="1" cellpadding="8">
    <tr>
        <th>Function</th>
        <th>Description</th>
    </tr>
    <tr><td>np.array()</td><td>Create NumPy array</td></tr>
    <tr><td>np.arange()</td><td>Generate range values</td></tr>
    <tr><td>reshape()</td><td>Change array shape</td></tr>
    <tr><td>ndim</td><td>Number of dimensions</td></tr>
    <tr><td>shape</td><td>Array structure</td></tr>
    <tr><td>size</td><td>Total elements</td></tr>
    <tr><td>np.sum()</td><td>Sum of elements</td></tr>
    <tr><td>np.mean()</td><td>Average</td></tr>
    <tr><td>np.max()</td><td>Maximum value</td></tr>
    <tr><td>np.min()</td><td>Minimum value</td></tr>
    <tr><td>np.argmax()</td><td>Index of maximum value</td></tr>
    <tr><td>np.argmin()</td><td>Index of minimum value</td></tr>
    <tr><td>np.repeat()</td><td>Repeat elements</td></tr>
    <tr><td>np.add()</td><td>Addition</td></tr>
    <tr><td>np.subtract()</td><td>Subtraction</td></tr>
    <tr><td>np.multiply()</td><td>Multiplication</td></tr>
    <tr><td>np.matmul()</td><td>Matrix multiplication</td></tr>
</table>

<hr>

<h3>Conclusion</h3>
<p>
This file demonstrates the core concepts of NumPy including array creation,
reshaping, indexing, statistical operations, arithmetic operations, and
multi-dimensional array handling, which are essential for data science,
machine learning, and scientific computing.
</p>

</body>
</html>
