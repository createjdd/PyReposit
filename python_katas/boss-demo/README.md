# BOSS 直聘爬虫脚本

这是一个用于抓取 BOSS 直聘网站职位信息的爬虫脚本，可以自动抓取职位描述、公司介绍、工商信息和工作地址。

## 功能特点

- ✅ 自动滚动加载更多职位（最多 100 个）
- ✅ 模拟人类操作行为，降低被检测风险
- ✅ 随机延迟，模拟真实浏览
- ✅ 支持多种元素选择器，提高兼容性
- ✅ 自动保存数据到 Excel 和 CSV 文件

## 安装依赖

```bash
pip install -r requirements.txt
```

## 安装 ChromeDriver

脚本使用 Selenium 控制 Chrome 浏览器，需要安装 ChromeDriver：

### macOS (使用 Homebrew)

```bash
brew install chromedriver
```

### 或者手动下载

1. 访问 https://chromedriver.chromium.org/
2. 下载与你的 Chrome 版本匹配的 ChromeDriver
3. 将可执行文件放到 PATH 路径中

## 使用方法

```bash
python get_el_develop.py
```

脚本会自动：

1. 打开 BOSS 直聘职位列表页
2. 滚动加载更多职位
3. 逐个点击职位进入详情页
4. 提取职位描述、公司介绍、工商信息、工作地址
5. 保存数据到 `boss_jobs.xlsx` 和 `boss_jobs.csv`

## 配置说明

在 `main()` 函数中可以修改：

- `start_url`: 起始 URL（默认是 Python 开发职位列表）
- `target_count`: 要抓取的职位数量（默认 100 个）

## 注意事项

1. **反爬虫机制**: BOSS 直聘有反爬虫机制，建议：

   - 适当增加延迟时间
   - 不要频繁运行脚本
   - 遵守网站的 robots.txt 协议

2. **登录要求**: 某些页面可能需要登录才能访问，如果遇到问题，可能需要先手动登录。

3. **元素选择器**: 如果网站结构发生变化，可能需要更新 CSS 选择器。

4. **调试模式**: 默认会显示浏览器窗口，如果需要在后台运行，可以取消注释无头模式选项。

## 输出文件

- `boss_jobs.xlsx`: Excel 格式的数据文件
- `boss_jobs.csv`: CSV 格式的数据文件

## 数据字段

- 职位描述
- 公司介绍
- 工商信息
- 工作地址
- 职位链接
