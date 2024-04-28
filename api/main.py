from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def good_luck():
    return {
        "Good": "Luck!",
    }
