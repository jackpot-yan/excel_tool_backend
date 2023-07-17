import uvicorn
from fastapi import FastAPI
from app.router.users import user_router
from app.router.tables import table_router
from app.middleware.cors import cors


def main():
    app = FastAPI()
    app = cors(app)
    app.include_router(user_router(), prefix='/users')
    app.include_router(table_router(), prefix='/tables')
    uvicorn.run(app, host='0.0.0.0', port=8085)


if __name__ == '__main__':
    main()
