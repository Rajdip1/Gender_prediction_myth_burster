# Gender Prediction Myth Buster

Short project that hosts a trained model to (de)validate pregnancy gender myths. The repository contains a FastAPI server that serves a simple web UI and an API endpoint which uses a serialized model to predict a baby gender label.

**Repository layout**
- `server/` — FastAPI app and templates (`server.py`, `templates/app.html`).
- `static/` — frontend assets: `app.js`, `app.css`.
- `model/` — model artifact, dataset and helper files:
  - `gender_prediction_myth_burster` — serialized model (joblib binary).
  - `columns.json` — column names / schema used for inference.
  - `pregnancy_gender_myth_dataset.csv` and `pregnancy_gender_myth.ipynb` — data and notebook used during development.

**What this server does**
- Serves a frontend at `/` (templates `app.html`).
- Exposes a POST `/predict` endpoint that accepts a JSON body with the medical features and returns the predicted label ("Girl"/"Boy") and raw numeric prediction.

Example JSON body for `/predict` (fields are floats):

```
{
  "mother_age": 28.0,
  "delivery_week": 39.0,
  "health_score": 7.5,
  "stress_level": 3.0,
  "work_hours": 40.0,
  "sleep_hours": 7.0
}
```

**Detected Python dependencies**
- `fastapi`, `uvicorn`, `pandas`, `joblib`, `scikit-learn`, `numpy`, `Jinja2`.
- A `requirements.txt` is included in the repo root for convenience.

**Install and run (recommended)**
1. Create and activate a virtual environment (PowerShell example):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run the FastAPI app (run from the repository root so relative paths resolve):

```powershell
cd server
uvicorn server:app --reload --host 0.0.0.0 --port 8000
```

Open `http://127.0.0.1:8000/` in your browser to view the app.

**Notes & troubleshooting**
- The model artifact `model/gender_prediction_myth_burster` is a binary joblib file; keep it in place relative to the repository root. The server code loads the model using a path computed from the server file's parent directory.
- If you move or run `server/server.py` from a different working directory, update the `MODEL_PATH` in `server/server.py` to point to the correct model file.
- The web UI expects the server to serve static files from a `static/` directory next to the repository root; run the server from the repo root to ensure these are served correctly.

**Development**
- The notebook `model/pregnancy_gender_myth.ipynb` contains the exploratory work and model training steps. Re-train or inspect there if you want to rebuild the serialized model.

**License / Attribution**
- No license file included. Check with the project owner before redistributing.
