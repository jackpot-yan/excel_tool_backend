import os
import sys
import uvicorn
from fastapi import FastAPI

# sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))[0])
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from router.users import user_router
from router.tables import table_router
from middleware.cors import cors


def main():
    app = FastAPI()
    app = cors(app)
    app.include_router(user_router(), prefix='/users')
    app.include_router(table_router(), prefix='/tables')
    uvicorn.run(app, host='0.0.0.0', port=8085)


if __name__ == '__main__':
    main()
