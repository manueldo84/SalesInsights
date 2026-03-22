from fastapi import FastAPI, UploadFile, File
import shutil
from src.backend.data_processing import process_sales_data
from src.backend.insight_generator import generate_insights

app = FastAPI()

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    try:
        file_location = f"temp_{file.filename}"

        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        processed_data = process_sales_data(file_location)
        insights = generate_insights(processed_data)

        return {
            "status": "success",
            "insights": insights
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }