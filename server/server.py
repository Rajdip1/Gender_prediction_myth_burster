from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import joblib
import pandas as pd
from pathlib import Path

app = FastAPI(title="Gender Prediction Myth Buster API")

# Serve CSS & JS
app.mount("/static", StaticFiles(directory="./static"), name="static")

# Serve HTML files
templates = Jinja2Templates(directory="./server/templates")

# Load model
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "model" / "gender_prediction_myth_burster"
model = joblib.load(MODEL_PATH)

class MedicalFeature(BaseModel):
    mother_age: float
    delivery_week: float
    health_score: float
    stress_level: float
    work_hours: float
    sleep_hours: float


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("app.html", {"request": request})


@app.post("/predict")
async def predict_gender(features: MedicalFeature):
    df = pd.DataFrame([features.model_dump()])
    pred = int(model.predict(df)[0])
    label = "Girl" if pred == 1 else "Boy"
    return {"predicted_gender": label, "raw": pred}
