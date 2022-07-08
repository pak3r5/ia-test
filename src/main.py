import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.api.api_v1.api import api_router


def create_app() -> FastAPI:
    app = FastAPI(
        title='IA - Python Test',
        description=""" Exam """,
        version="0.0.1",
        contact={"name": "Pake Valencia", "email": "pak3r5@gmail.com"}
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    app.include_router(api_router, prefix='')

    return app


if __name__ == '__main__':
    uvicorn.run("main:create_app", host="127.0.0.0", port=8000, reload=True, factory=True)

