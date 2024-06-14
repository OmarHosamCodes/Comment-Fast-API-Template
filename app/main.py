import fastapi

from app.routers import example

app = fastapi.FastAPI()

app.include_router(example.router)


@app.get("/")
async def read_root():
    return {"message": "Hello World"}
