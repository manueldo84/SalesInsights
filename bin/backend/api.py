from fastapi import FastAPI, UploadFile
import shutil
import os

from src.backend.data_processing import process_sales_data
from src.backend.insight_generator import generate_insights

app = FastAPI()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.post("/analyze")
async def analyze(file: UploadFile):

    file_location = f"{UPLOAD_FOLDER}/{file.filename}"

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    processed_data = process_sales_data(file_location)
    insights = generate_insights(processed_data)

    return {"insights": insights}
