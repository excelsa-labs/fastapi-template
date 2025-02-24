import fastapi

app = fastapi.FastAPI()


@app.get("/")
async def root(message: str = "Hello World"):
    return {"message": message}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
