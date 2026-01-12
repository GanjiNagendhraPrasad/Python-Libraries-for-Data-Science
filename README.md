<!DOCTYPE html>
<html lang="en">

<body>

<h1>NumPy Detailed Explanation</h1>

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




<h2>1️⃣ Introduction to Pandas</h2>

<h3>What is Pandas?</h3>
<p>
Pandas is a <b>Python library</b> used for:
</p>
<ul>
  <li>Data analysis</li>
  <li>Data manipulation</li>
  <li>Data cleaning</li>
  <li>Handling structured data (tables)</li>
</ul>

<h3>Why Pandas?</h3>
<ul>
  <li>Fast and efficient</li>
  <li>Easy handling of missing data</li>
  <li>Works well with NumPy, Matplotlib, and Seaborn</li>
</ul>

<pre><code>import pandas as pd</code></pre>

<hr>

<h2>2️⃣ Pandas Series</h2>

<h3>What is a Series?</h3>
<p>
A <b>Series</b> is a <b>one-dimensional labeled array</b>.
</p>

<h3>Creating a Series from a List</h3>
<pre><code>
s = pd.Series([10, 20, 30, 40])
print(s)
</code></pre>

<p>✔ Automatically assigns index<br>✔ Data type inferred</p>

<h3>Creating Series with Custom Index</h3>
<pre><code>
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
</code></pre>

<h3>Series from Dictionary</h3>
<pre><code>
data = {'Math': 90, 'Science': 85, 'English': 88}
s = pd.Series(data)
</code></pre>

<p>✔ Keys → Index<br>✔ Values → Data</p>

<h3>Accessing Series Data</h3>
<pre><code>
s['Math']
s[0]
</code></pre>

<hr>

<h2>3️⃣ Pandas DataFrame</h2>

<h3>What is a DataFrame?</h3>
<p>
A <b>2-dimensional table-like structure</b> with:
</p>
<ul>
  <li>Rows</li>
  <li>Columns</li>
  <li>Index</li>
  <li>Column names</li>
</ul>

<h3>Creating DataFrame from Dictionary</h3>
<pre><code>
data = {
    'Name': ['A', 'B', 'C'],
    'Age': [20, 21, 22],
    'Marks': [85, 90, 88]
}

df = pd.DataFrame(data)
print(df)
</code></pre>

<h3>Creating DataFrame with Custom Index</h3>
<pre><code>
df = pd.DataFrame(data, index=['s1', 's2', 's3'])
</code></pre>

<hr>

<h2>4️⃣ DataFrame Attributes</h2>
<pre><code>
df.shape
df.size
df.ndim
df.columns
df.index
df.dtypes
</code></pre>

<hr>

<h2>5️⃣ Viewing Data</h2>
<pre><code>
df.head()
df.head(2)
df.tail()
df.tail(3)
</code></pre>

<hr>

<h2>6️⃣ Selecting Data</h2>

<h3>Column Selection</h3>
<pre><code>
df['Name']
df[['Name', 'Marks']]
</code></pre>

<h3>Row Selection using loc (Label-based)</h3>
<pre><code>
df.loc['s1']
df.loc['s1', 'Marks']
</code></pre>

<h3>Row Selection using iloc (Index-based)</h3>
<pre><code>
df.iloc[0]
df.iloc[0, 2]
</code></pre>

<hr>

<h2>7️⃣ Adding Columns</h2>
<pre><code>
df['Result'] = ['Pass', 'Pass', 'Pass']
</code></pre>

<hr>

<h2>8️⃣ Modifying Data</h2>
<pre><code>
df['Marks'] = df['Marks'] + 5
</code></pre>

<hr>

<h2>9️⃣ Dropping Rows and Columns</h2>

<h3>Drop Column</h3>
<pre><code>
df.drop('Age', axis=1)
</code></pre>

<h3>Drop Row</h3>
<pre><code>
df.drop('s1', axis=0)
</code></pre>

<p><b>⚠ Note:</b> Use <code>inplace=True</code> to modify original DataFrame</p>

<hr>

<h2>🔟 Handling Missing Values (NaN)</h2>

<h3>Creating Missing Data</h3>
<pre><code>
import numpy as np
df.loc['s2', 'Marks'] = np.nan
</code></pre>

<h3>Checking Missing Values</h3>
<pre><code>
df.isnull()
df.isnull().sum()
</code></pre>

<h3>Filling Missing Values</h3>
<pre><code>
df.fillna(0)
df.fillna(df.mean())
</code></pre>

<h3>Dropping Missing Values</h3>
<pre><code>
df.dropna()
</code></pre>

<hr>

<h2>1️⃣1️⃣ Filtering Data</h2>

<h3>Conditional Filtering</h3>
<pre><code>
df[df['Marks'] > 85]
</code></pre>

<h3>Multiple Conditions</h3>
<pre><code>
df[(df['Marks'] > 80) & (df['Age'] > 20)]
</code></pre>

<hr>

<h2>1️⃣2️⃣ Sorting Data</h2>
<pre><code>
df.sort_values(by='Marks')
df.sort_values(by='Marks', ascending=False)
</code></pre>

<hr>

<h2>1️⃣3️⃣ Statistical Functions</h2>
<pre><code>
df['Marks'].mean()
df['Marks'].sum()
df['Marks'].min()
df['Marks'].max()
df['Marks'].count()
</code></pre>

<hr>

<h2>1️⃣4️⃣ Descriptive Statistics</h2>
<pre><code>
df.describe()
</code></pre>

<hr>

<h2>1️⃣5️⃣ Reading Data from Files</h2>

<h3>CSV File</h3>
<pre><code>
df = pd.read_csv('data.csv')
</code></pre>

<h3>Excel File</h3>
<pre><code>
df = pd.read_excel('data.xlsx')
</code></pre>

<hr>

<h2>1️⃣6️⃣ Writing Data to Files</h2>
<pre><code>
df.to_csv('output.csv', index=False)
df.to_excel('output.xlsx', index=False)
</code></pre>

<hr>

<h2>1️⃣7️⃣ Index Operations</h2>
<pre><code>
df.set_index('Name')
df.reset_index()
</code></pre>

<hr>

<h2>1️⃣8️⃣ Applying Functions</h2>
<pre><code>
df['Marks'].apply(lambda x: x + 2)
</code></pre>

<hr>

<h2>1️⃣9️⃣ Value Counts</h2>
<pre><code>
df['Result'].value_counts()
</code></pre>

<hr>

<h2>2️⃣0️⃣ Unique Values</h2>
<pre><code>
df['Result'].unique()
df['Result'].nunique()
</code></pre>

<hr>

<h2>2️⃣1️⃣ Renaming Columns</h2>
<pre><code>
df.rename(columns={'Marks': 'Score'})
</code></pre>

<hr>

<h2>2️⃣2️⃣ Data Type Conversion</h2>
<pre><code>
df['Age'] = df['Age'].astype(float)
</code></pre>

<hr>

<h2>2️⃣3️⃣ Pandas with NumPy</h2>
<pre><code>
import numpy as np
df['Marks'] = np.sqrt(df['Marks'])
</code></pre>



<h1>📊 Matplotlib Complete Explanation</h1>

<h2>1️⃣ Importing Matplotlib</h2>

<pre><code>import matplotlib.pyplot as plt</code></pre>

<h3>What is Matplotlib?</h3>
<ul>
    <li>Matplotlib is a Python library used for data visualization</li>
    <li>It helps create graphs like line charts, bar charts, histograms, pie charts, etc.</li>
</ul>

<h3>Why pyplot?</h3>
<ul>
    <li><code>pyplot</code> provides MATLAB-style plotting functions</li>
    <li>Imported as <code>plt</code> to keep code short and readable</li>
</ul>

<hr>

<h2>2️⃣ Scatter Plot</h2>

<pre><code>
india = [1,5,6,2,7,4]
usa = [5,4,1,3,2,6]

plt.figure(figsize=(5,3))
plt.title('scatterplot')
plt.xlabel('india')
plt.ylabel('usa')

plt.scatter(x=india, y=usa, color='r', marker='*')
plt.show()
</code></pre>

<h3>What is a Scatter Plot?</h3>
<ul>
    <li>Displays the relationship between two variables</li>
    <li>Each point represents an (x, y) value</li>
    <li>Used in data analysis and machine learning</li>
</ul>

<h3>figure(figsize)</h3>
<p>Creates a plotting area and controls its size in inches.</p>

<h3>Title and Axis Labels</h3>
<ul>
    <li><code>plt.title()</code> sets the graph title</li>
    <li><code>plt.xlabel()</code> sets x-axis label</li>
    <li><code>plt.ylabel()</code> sets y-axis label</li>
</ul>

<h3>scatter()</h3>

<table>
    <tr><th>Parameter</th><th>Description</th></tr>
    <tr><td>x</td><td>Values for x-axis</td></tr>
    <tr><td>y</td><td>Values for y-axis</td></tr>
    <tr><td>color</td><td>Point color</td></tr>
    <tr><td>marker</td><td>Shape of points</td></tr>
</table>

<hr>

<h2>3️⃣ Line Chart</h2>

<pre><code>
plt.plot(india, usa, color='r', marker='*')
</code></pre>

<h3>What is a Line Chart?</h3>
<ul>
    <li>Shows trends over time or sequence</li>
    <li>Connects data points with lines</li>
</ul>

<hr>

<h2>4️⃣ Multiple Line Chart</h2>

<pre><code>
plt.plot(india, usa, color='r', marker='*')
plt.plot(india, uk, color='g', marker='*')
</code></pre>

<h3>Purpose</h3>
<ul>
    <li>Used to compare multiple datasets</li>
    <li>Each line represents a different dataset</li>
</ul>

<hr>

<h2>5️⃣ Legend</h2>

<pre><code>
plt.plot(india, usa, marker='*', label='india-usa')
plt.plot(india, uk, marker='*', label='india-uk')
plt.legend()
</code></pre>

<h3>Legend Explanation</h3>
<ul>
    <li>Explains what each line represents</li>
    <li><code>label</code> is passed inside plot</li>
    <li><code>plt.legend()</code> displays it</li>
</ul>

<hr>

<h2>6️⃣ Subplots</h2>

<h3>Row-wise Subplot</h3>

<pre><code>
plt.subplot(1,2,1)
plt.subplot(1,2,2)
</code></pre>

<h3>Column-wise Subplot</h3>

<pre><code>
plt.subplot(2,1,1)
plt.subplot(2,1,2)
</code></pre>

<h3>Why Subplots?</h3>
<ul>
    <li>Multiple graphs in one window</li>
    <li>Better comparison</li>
    <li>Used in dashboards</li>
</ul>

<hr>

<h2>7️⃣ Histogram</h2>

<pre><code>
plt.hist(x=age, color='r')
</code></pre>

<h3>What is a Histogram?</h3>
<ul>
    <li>Shows frequency distribution</li>
    <li>Data is divided into bins</li>
</ul>

<h3>Histogram with Bins</h3>

<pre><code>
plt.hist(x=age, color='b', bins=4)
</code></pre>

<hr>

<h2>8️⃣ Vertical Bar Chart</h2>

<pre><code>
plt.bar(company_names, revenue)
</code></pre>

<h3>Bar Chart Explanation</h3>
<ul>
    <li>Used to compare categories</li>
    <li>Height represents value</li>
</ul>

<hr>

<h2>9️⃣ Horizontal Bar Chart</h2>

<pre><code>
plt.barh(company_names, revenue)
</code></pre>

<table>
    <tr><th>Vertical</th><th>Horizontal</th></tr>
    <tr><td>bar()</td><td>barh()</td></tr>
    <tr><td>Categories on X</td><td>Categories on Y</td></tr>
</table>

<hr>

<h2>🔟 Pie Chart</h2>

<pre><code>
plt.pie(revenue, labels=company_names)
</code></pre>

<h3>Pie Chart Usage</h3>
<ul>
    <li>Shows percentage contribution</li>
    <li>Used for market share and distribution</li>
</ul>

<h3>Advanced Pie Chart</h3>

<pre><code>
plt.pie(
    revenue,
    labels=company_names,
    shadow=True,
    autopct='%.2f',
    explode=[0,0,0.2,0]
)
</code></pre>

<table>
    <tr><th>Parameter</th><th>Description</th></tr>
    <tr><td>labels</td><td>Names for slices</td></tr>
    <tr><td>shadow</td><td>3D shadow effect</td></tr>
    <tr><td>autopct</td><td>Shows percentage</td></tr>
    <tr><td>explode</td><td>Separates slices</td></tr>
</table>

<hr>

<h2>✅ Final Summary</h2>

<ul>
    <li>Scatter Plot</li>
    <li>Line Plot</li>
    <li>Multiple Line Plot</li>
    <li>Legends</li>
    <li>Subplots</li>
    <li>Histogram</li>
    <li>Vertical & Horizontal Bar Charts</li>
    <li>Pie Chart with explode</li>
</ul>

</body>
</html>
