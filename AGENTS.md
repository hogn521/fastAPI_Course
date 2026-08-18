# AGENTS.md

This file provides guidance to Codex (Codex.ai/code) when working with code in this repository.

## 项目定位

这是一个 **FastAPI 学习仓库**，代码随用户的课程进度逐步增加。当前是最小可运行的应用（两个 GET 接口）。

## 常用命令

```bash
# 启动开发服务器（带热重载）
uvicorn main:app --reload

# 安装依赖
pip install fastapi uvicorn

# 交互式 API 文档（启动后访问）
# http://127.0.0.1:8000/docs  (Swagger UI)
# http://127.0.0.1:8000/redoc  (ReDoc)

# 测试接口：直接运行 PyCharm/IDE 打开 test_main.http，点击请求行发送
```

项目目前没有测试框架，验证接口用 `test_main.http` 或 `/docs` 页面。

## 架构

单文件应用：所有代码都在 `main.py`，以 `app = FastAPI()` 为入口，用 `@app.get(...)` 等装饰器注册路由。将来拆分路由/模型时会重构为包结构。

## 协作约定

- **教学性质**：用户是 FastAPI 初学者，写代码或讲解时以教学口吻为主——先讲原理再给示例，代码保持简单清晰、注释适度，不要引入超出学习进度的高级技巧。
- **学习进度**：新增功能后，同步更新 README.md 中的"接口清单"和"学习进度"勾选列表。
- **Git**：提交信息用中文，简洁描述改动。
- **.gitignore**：已忽略 `.idea` 和 `.mcp.json`，新增依赖或 IDE 配置文件时注意补充。