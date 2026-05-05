# QWeather Forecast - 和风天气预报查询

基于和风天气 API 的城市天气预报查询工具，支持获取全球城市的 7 天天气预报。

[English Version](./README_EN.md)

## 功能特性

- 🌍 **全球城市查询** - 支持中文和英文城市名搜索
- 📅 **7 天天气预报** - 获取未来一周的天气信息
- 🌡️ **详细天气数据** - 包含天气状况、最高最低温度
- 🚀 **简单易用** - 命令行一行命令即可查询

## 安装依赖

项目依赖 `requests` 库，可选依赖 `python-dotenv` 用于加载环境变量：

```bash
pip install requests python-dotenv
```

## 配置

### 1. 获取 API 凭证

访问 [和风天气开发平台](https://dev.qweather.com/) 注册账号并创建项目，获取：
- API Key
- 定制的 API Host

### 2. 配置环境变量

有两种方式配置：

#### 方式一：使用 .env 文件（推荐）

复制 `.env.example` 为 `.env`：

```bash
cp .env.example .env
```

编辑 `.env` 文件，填入你的 API 密钥和定制的 API Host：

```env
QWEATHER_API_KEY=your_actual_api_key_here
QWEATHER_API_HOST=your_custom_api_host_here
```

#### 方式二：设置环境变量

Windows:
```cmd
set QWEATHER_API_KEY=your_actual_api_key_here
set QWEATHER_API_HOST=your_custom_api_host_here
```

Linux/Mac:
```bash
export QWEATHER_API_KEY=your_actual_api_key_here
export QWEATHER_API_HOST=your_custom_api_host_here
```

## 使用方法

运行脚本并传入城市名称作为参数：

```bash
python qweather_forecast.py <city_name>
```

### 使用示例

查询北京天气：

```bash
python qweather_forecast.py beijing
```

或使用中文：

```bash
python qweather_forecast.py 北京
```

查询其他城市：

```bash
python qweather_forecast.py shanghai
python qweather_forecast.py 深圳
```

### 输出示例

```
7-Day Weather Forecast for beijing:
2026-05-05: 晴, 17-29°C
2026-05-06: 多云, 13-26°C
2026-05-07: 晴, 10-24°C
2026-05-08: 晴, 12-25°C
2026-05-09: 晴, 15-27°C
2026-05-10: 多云, 17-30°C
2026-05-11: 多云, 18-29°C
```

## 项目结构

```
codex/
├── qweather_forecast.py    # 主程序脚本
├── .env.example            # 环境变量配置模板
├── .gitignore              # Git 忽略文件配置
├── README.md               # 项目说明文档 (中文)
├── README_EN.md            # 项目说明文档 (英文)
└── LICENSE                 # MIT 许可证
```

## 和风天气定价说明

和风天气开发服务采用按量计费模式，每月享有免费额度。

### 天气和基础服务

包括：天气预报、分钟预报、预警、天气指数、空气质量、时光机、GeoAPI、天文、控制台API

| 请求量(每月) | 价格(每次请求) |
|---|---|
| 0~5万 | **免费** |
| 之后的 95万 | CNY 0.0007 |
| 之后的 400万 | CNY 0.0005 |
| 之后的 500万 | CNY 0.00035 |
| 之后的 4000万 | CNY 0.00015 |
| 之后的 5000万 | CNY 0.0001 |
| 超过 1亿 | 联系我们 |

### 其他服务

- **台风和海洋**：0~100万次，CNY 0.003/次
- **太阳辐照**：0~10万次，CNY 0.3/次

详细定价请参考：[和风天气定价页面](https://dev.qweather.com/docs/finance/pricing/)

## 技术说明

### API 端点

- **城市查询**: `/geo/v2/city/lookup` - 搜索城市并获取 Location ID
- **天气预报**: `/v7/weather/7d` - 获取 7 天天气预报

### 工作流程

1. 根据城市名称查询 Location ID
2. 使用 Location ID 查询天气预报数据
3. 格式化并输出天气信息

## 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## 安全提示

- ⚠️ **永远不要将 `.env` 文件提交到 Git** - 它包含你的 API 密钥
- `.gitignore` 已配置为自动忽略 `.env` 文件
- 如需使用自己的 API 凭证，请访问 [和风天气开发平台](https://dev.qweather.com/) 注册申请
- 复制 `.env.example` 为 `.env` 并填入你的凭证
