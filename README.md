# SM4 Encryption Tool

基于 SM4 国密标准（GB/T 32907-2016）的文件加密/解密桌面工具。提供图形界面和 Web 后端双重操作方式。

## 功能

- **SM4 文件加密** — 支持 CBC 等分组模式
- **SM4 文件解密** — 支持密钥文件加载
- **密钥管理** — 密钥生成、导入、数据库管理
- **Web 界面** — 内置 Flask 服务，支持浏览器操作
- **桌面 GUI** — Python Tkinter 自定义 UI

## 技术栈

| 层 | 技术 |
|---|---|
| 加密核心 | C 语言 SM4 国密算法实现 |
| Python 绑定 | ctypes 调用 DLL |
| 桌面 GUI | Tkinter 自定义组件 |
| Web 后端 | Flask + CORS |
| 密钥存储 | SQLite |

## 快速开始

```bash
pip install flask flask-cors
python app.py
```

启动后桌面 GUI 自动打开，Web 界面访问 http://localhost:5000

## 项目结构

```
SM4_Tool/
├── app.py                  # 启动入口
├── c_sm4/                  # C 语言 SM4 算法
│   ├── sm4.c / sm4.h       # 核心加密算法
│   ├── main.c              # CLI 入口
│   └── sm4_file.c          # 文件加解密接口
├── src/
│   ├── config/             # 应用配置
│   ├── routes/             # Flask 路由
│   ├── services/           # 业务逻辑
│   ├── utils/              # 工具（SM4 调用、数据库、文件）
│   ├── static/             # Web 前端 JS
│   ├── templates/          # HTML 模板
│   └── ui/                 # Tkinter GUI
│       ├── pages/          # 功能页面
│       └── widgets/        # 自定义控件
├── README.md
└── LICENSE
```

## 许可

MIT
