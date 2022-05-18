from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import team, regalia_pass, scan, home, search, verify, guest, participant


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(team.route)
app.include_router(regalia_pass.route)
app.include_router(scan.route)
app.include_router(home.route)
app.include_router(verify.route)
app.include_router(search.route)
app.include_router(guest.route)
app.include_router(participant.route)


@app.get("/")
def root():
    return {"message": "Welcome to Regalia'22"}
