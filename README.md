# QWeather Forecast - 和风天气预报查询

基于和风天气 API 的城市天气预报查询工具，支持获取全球城市的 7 天天气预报。

## 功能特性

- 🌍 **全球城市查询** - 支持中文和英文城市名搜索
- 📅 **7 天天气预报** - 获取未来一周的天气信息
- 🌡️ **详细天气数据** - 包含天气状况、最高最低温度
- 🚀 **简单易用** - 命令行一行命令即可查询

## 安装依赖

项目依赖 `requests` 库，使用前请安装：

```bash
pip install requests
```

## 使用方法

运行脚本并传入城市名称作为参数：

```bash
python qweather_forecast.py <城市名称>
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
├── README.md               # 项目说明文档
└── LICENSE                 # MIT 许可证
```

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

## 注意事项

- 当前使用预配置的 API 密钥和自定义 API 主机
- 如需使用自己的 API 密钥，请访问 [和风天气开发平台](https://dev.qweather.com/) 注册申请
