from fastapi import FastAPI
from routes.data_routes import router

app = FastAPI()
app.include_router(router)
