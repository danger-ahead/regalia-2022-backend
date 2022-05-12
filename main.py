from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from routes import (
    team
)


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(team.route)


@app.get("/")
def root():
    return {"message": "Welcome to Regalia'22"}
