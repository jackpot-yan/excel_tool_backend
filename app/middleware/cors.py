from fastapi.middleware.cors import CORSMiddleware


def cors(app):
    origins = [
        "http://localhost.tiangolo.com",
        "https://localhost.tiangolo.com",
        "http://localhost",
        "http://localhost:8080",
        "http://127.0.0.1:8081"
    ]

    # 3、配置 CORSMiddleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )
    return app
