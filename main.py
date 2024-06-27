from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"fact": "Half-Life 2 is the best game ever made"}
