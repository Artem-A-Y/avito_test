from fastapi import FastAPI
import uvicorn

from settings import settings


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == '__main__':
    uvicorn.run(
        'app:app',
        reload=True,
        host=settings.server_host,
        port=settings.server_port,
    )

