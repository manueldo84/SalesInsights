from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
import shutil
import os
 
from src.backend.data_processing import process_sales_data
from src.backend.insight_generator import generate_ai_insights
 
app = FastAPI()
 
os.makedirs("outputs", exist_ok=True)
app.mount("/charts", StaticFiles(directory="outputs"), name="charts")
 
BASE_URL = os.environ.get("BACKEND_URL", "http://127.0.0.1:8000")
 
 
@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    try:
        file_location = f"temp_{file.filename}"
 
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
 
        processed_data = process_sales_data(file_location)
 
        ai_report = generate_ai_insights(processed_data)
 
        return {
            "status": "success",
 
            "summary": processed_data,
 
            "charts": {
                "product_chart": f"{BASE_URL}/charts/product_sales_chart.png",
                "region_chart": f"{BASE_URL}/charts/region_sales_chart.png"
            },
 
            "ai_report": ai_report
        }
 
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }
 