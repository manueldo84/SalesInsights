from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
import shutil

from src.backend.data_processing import process_sales_data
from src.backend.insight_generator import generate_ai_insights

app = FastAPI()
app.mount("/charts", StaticFiles(directory="outputs"), name="charts")


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
                "product_chart": "http://127.0.0.1:8000/charts/product_sales_chart.png",
                "region_chart": "http://127.0.0.1:8000/charts/region_sales_chart.png"
            },

            "ai_report": ai_report
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }