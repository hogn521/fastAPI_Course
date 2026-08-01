# FastAPI 学习仓库

这是我学习 [FastAPI](https://fastapi.tiangolo.com/) 的练习项目，所有练习代码都会放在这里。

## 课程资料

跟随黑马程序员《PythonWeb开发：FastAPI从入门到实战》视频教程学习：

- B 站链接：<https://www.bilibili.com/video/BV1zV2QBtE39/>
- 课程涵盖：路由、依赖注入、Pydantic、异步编程、ORM、项目拆分、模型训练、部署、接口测试

## 环境要求

- Python 3.8+
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)（ASGI 服务器）

安装依赖：

```bash
pip install fastapi uvicorn
```

## 运行项目

在项目根目录执行：

```bash
uvicorn main:app --reload
```

启动成功后访问：

- 接口文档（Swagger UI）：<http://127.0.0.1:8000/docs>
- 接口文档（ReDoc）：<http://127.0.0.1:8000/redoc>

## 项目结构

```
.
├── main.py          # FastAPI 应用入口
├── test_main.http   # IDE HTTP 客户端测试请求（可在 PyCharm 中直接运行）
├── README.md
└── .gitignore
```

## 当前接口

| 方法 | 路径          | 说明                   |
| ---- | ------------- | ---------------------- |
| GET  | `/`           | 返回 Hello World       |
| GET  | `/hello/{name}` | 返回带名字的问候语   |

## 学习进度

- [x] 创建第一个 FastAPI 应用
- [ ] 路由（路径参数、查询参数）
- [ ] Pydantic 数据模型
- [ ] 依赖注入
- [ ] 异步编程
- [ ] ORM 数据库集成
- [ ] 项目拆分
- [ ] 模型训练
- [ ] 部署
- [ ] 接口测试