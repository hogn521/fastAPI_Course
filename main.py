from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
@app.get("/profile")
async def profile():
    return {"code":"A001",
            "name":"wjf",
            "email":['126.com','163.com'],}