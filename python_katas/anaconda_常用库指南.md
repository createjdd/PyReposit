# Anaconda 常用库和函数指南

## 📚 核心科学计算库

### 1. NumPy - 数值计算基础库

**用途**：多维数组操作、数学运算、线性代数

**常用函数**：

```python
import numpy as np

# 创建数组
arr = np.array([1, 2, 3, 4, 5])
zeros = np.zeros((3, 4))          # 创建全零数组
ones = np.ones((2, 3))             # 创建全一数组
arange = np.arange(0, 10, 2)       # 类似 range，但返回数组
linspace = np.linspace(0, 1, 5)   # 等间距数组

# 数组操作
arr.shape                          # 查看形状
arr.reshape(2, 3)                  # 改变形状
arr.sum()                          # 求和
arr.mean()                         # 平均值
arr.max() / arr.min()              # 最大值/最小值
arr.std()                          # 标准差

# 数学运算
np.sqrt(arr)                       # 平方根
np.sin(arr)                        # 三角函数
np.exp(arr)                        # 指数
np.log(arr)                        # 对数

# 线性代数
np.dot(a, b)                       # 矩阵乘法
np.linalg.inv(matrix)              # 矩阵求逆
np.linalg.det(matrix)              # 行列式
```

---

### 2. Pandas - 数据分析库

**用途**：数据处理、CSV/Excel 读写、数据清洗

**常用函数**：

```python
import pandas as pd

# 创建数据结构
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
series = pd.Series([1, 2, 3, 4, 5])

# 读取数据
df = pd.read_csv('data.csv')       # 读取 CSV
df = pd.read_excel('data.xlsx')    # 读取 Excel
df = pd.read_json('data.json')     # 读取 JSON

# 数据查看
df.head()                          # 查看前5行
df.tail()                          # 查看后5行
df.info()                          # 数据信息
df.describe()                      # 统计描述
df.shape                           # 形状
df.columns                         # 列名
df.index                           # 索引

# 数据选择
df['column_name']                  # 选择列
df[['col1', 'col2']]               # 选择多列
df.loc[0]                          # 按标签选择行
df.iloc[0]                         # 按位置选择行
df.loc[df['A'] > 2]               # 条件筛选

# 数据操作
df.dropna()                        # 删除空值
df.fillna(0)                       # 填充空值
df.sort_values('column')           # 排序
df.groupby('column').sum()         # 分组聚合
df.merge(df2, on='key')           # 合并数据

# 数据保存
df.to_csv('output.csv')            # 保存为 CSV
df.to_excel('output.xlsx')         # 保存为 Excel
```

---

### 3. Matplotlib - 数据可视化库

**用途**：绘制图表、数据可视化

**常用函数**：

```python
import matplotlib.pyplot as plt
import numpy as np

# 基本绘图
plt.plot(x, y)                     # 折线图
plt.scatter(x, y)                  # 散点图
plt.bar(x, y)                      # 柱状图
plt.hist(data)                     # 直方图
plt.pie(sizes)                     # 饼图

# 图表设置
plt.title('标题')                  # 设置标题
plt.xlabel('X轴标签')              # X轴标签
plt.ylabel('Y轴标签')              # Y轴标签
plt.legend()                       # 显示图例
plt.grid(True)                     # 显示网格
plt.xlim(0, 10)                    # 设置X轴范围
plt.ylim(0, 10)                    # 设置Y轴范围

# 子图
fig, axes = plt.subplots(2, 2)    # 创建2x2子图
axes[0, 0].plot(x, y)              # 在子图中绘图

# 显示和保存
plt.show()                         # 显示图表
plt.savefig('plot.png')            # 保存图表
plt.close()                        # 关闭图表
```

---

### 4. SciPy - 科学计算库

**用途**：科学计算、优化、统计、信号处理

**常用模块**：

```python
from scipy import stats, optimize, integrate, linalg

# 统计
stats.mean(data)                   # 均值
stats.median(data)                 # 中位数
stats.mode(data)                   # 众数
stats.ttest_1samp(data, mean)      # t检验

# 优化
optimize.minimize(func, x0)       # 最小化函数
optimize.curve_fit(func, x, y)     # 曲线拟合

# 积分
integrate.quad(func, a, b)         # 定积分
integrate.dblquad(func, a, b, c, d) # 二重积分

# 线性代数
linalg.solve(A, b)                 # 解线性方程组
linalg.eig(A)                      # 特征值和特征向量
```

---

## 🤖 机器学习库

### 5. Scikit-learn - 机器学习库

**用途**：分类、回归、聚类、降维

**常用模块**：

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, mean_squared_error

# 数据分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 线性回归
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

# 逻辑回归（分类）
clf = LogisticRegression()
clf.fit(X_train, y_train)
accuracy = accuracy_score(y_test, clf.predict(X_test))

# K-means 聚类
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
labels = kmeans.labels_
```

---

## 🌐 网络和数据处理

### 6. Requests - HTTP 请求库

**用途**：发送 HTTP 请求、API 调用

**常用函数**：

```python
import requests

# GET 请求
response = requests.get('https://api.example.com/data')
response.json()                    # 解析 JSON
response.text                      # 获取文本
response.status_code               # 状态码

# POST 请求
requests.post('https://api.example.com', data={'key': 'value'})

# 带参数的请求
requests.get('https://api.example.com', params={'q': 'python'})

# 设置请求头
headers = {'Authorization': 'Bearer token'}
requests.get('https://api.example.com', headers=headers)
```

---

### 7. BeautifulSoup4 - HTML/XML 解析库

**用途**：网页解析、数据抓取

**常用函数**：

```python
from bs4 import BeautifulSoup
import requests

html = requests.get('https://example.com').text
soup = BeautifulSoup(html, 'html.parser')

# 查找元素
soup.find('div')                   # 查找第一个 div
soup.find_all('a')                 # 查找所有 a 标签
soup.select('.class-name')         # CSS 选择器
soup.select('#id-name')            # ID 选择器

# 获取内容
element.text                       # 获取文本
element.get('href')                # 获取属性
```

---

## 📊 高级可视化

### 8. Seaborn - 统计可视化库

**用途**：基于 Matplotlib 的高级统计图表

**常用函数**：

```python
import seaborn as sns

sns.scatterplot(x='x', y='y', data=df)    # 散点图
sns.lineplot(x='x', y='y', data=df)       # 折线图
sns.barplot(x='x', y='y', data=df)        # 柱状图
sns.boxplot(x='x', y='y', data=df)        # 箱线图
sns.heatmap(data)                          # 热力图
sns.pairplot(df)                           # 成对关系图
```

---

### 9. Plotly - 交互式可视化库

**用途**：创建交互式图表

**常用函数**：

```python
import plotly.express as px
import plotly.graph_objects as go

# 简单图表
fig = px.scatter(df, x='x', y='y')
fig = px.line(df, x='x', y='y')
fig.show()

# 复杂图表
fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y))
fig.show()
```

---

## 🖼️ 图像处理

### 10. Pillow (PIL) - 图像处理库

**用途**：图像打开、编辑、保存

**常用函数**：

```python
from PIL import Image

# 打开和保存
img = Image.open('image.jpg')
img.save('output.png')

# 图像操作
img.resize((800, 600))             # 调整大小
img.rotate(90)                      # 旋转
img.crop((0, 0, 100, 100))         # 裁剪
img.convert('RGB')                  # 转换模式

# 图像信息
img.size                           # 尺寸
img.format                         # 格式
img.mode                           # 模式
```

---

## 📓 Jupyter 相关

### 11. Jupyter / JupyterLab - 交互式笔记本

**用途**：交互式编程、数据分析、文档编写

**常用命令**：

```bash
jupyter notebook                   # 启动 Jupyter Notebook
jupyter lab                        # 启动 JupyterLab
jupyter notebook --port 8888       # 指定端口
```

**常用魔法命令**（在 Jupyter 中使用）：

```python
%matplotlib inline                 # 内联显示图表
%timeit code                       # 测量代码执行时间
%run script.py                     # 运行 Python 脚本
!ls                                # 执行 shell 命令
```

---

## 🔧 其他常用库

### 12. IPython - 增强的 Python 交互式 shell

**用途**：更好的交互式体验

**特性**：

- Tab 自动补全
- 命令历史
- 魔法命令
- 更好的错误提示

---

### 13. SymPy - 符号数学库

**用途**：符号计算、代数运算

**常用函数**：

```python
from sympy import symbols, solve, diff, integrate

x, y = symbols('x y')
expr = x**2 + 2*x + 1
solve(expr, x)                     # 解方程
diff(expr, x)                      # 求导
integrate(expr, x)                 # 积分
```

---

## 📦 安装和导入示例

```python
# 如果某个库未安装，使用 conda 安装
# conda install numpy pandas matplotlib

# 标准导入方式
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import requests
from bs4 import BeautifulSoup
import seaborn as sns
from PIL import Image
```

---

## 🎯 常用组合使用场景

### 数据分析流程

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. 读取数据
df = pd.read_csv('data.csv')

# 2. 数据清洗
df = df.dropna()
df = df[df['value'] > 0]

# 3. 数据分析
summary = df.describe()
correlation = df.corr()

# 4. 可视化
sns.heatmap(correlation)
plt.show()
```

### 机器学习流程

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 1. 准备数据
X = df[['feature1', 'feature2']]
y = df['target']

# 2. 分割数据
X_train, X_test, y_train, y_test = train_test_split(X, y)

# 3. 训练模型
model = LinearRegression()
model.fit(X_train, y_train)

# 4. 评估
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
```

---

## 📚 学习资源

- **NumPy**: https://numpy.org/doc/
- **Pandas**: https://pandas.pydata.org/docs/
- **Matplotlib**: https://matplotlib.org/stable/contents.html
- **Scikit-learn**: https://scikit-learn.org/stable/
- **Jupyter**: https://jupyter.org/documentation

---

## 💡 提示

1. **查看库文档**：使用 `help()` 函数，如 `help(np.array)`
2. **查看版本**：`import numpy; print(numpy.__version__)`
3. **查看所有函数**：`dir(numpy)` 或 `numpy.__all__`
4. **交互式学习**：在 Jupyter Notebook 中尝试这些函数
