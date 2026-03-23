import gradio as gr
import requests
import os
 
API_URL = os.environ.get("BACKEND_URL", "http://127.0.0.1:8000") + "/analyze"
 
def analyze_sales(file):
 
    response = requests.post(
        API_URL,
        files={"file": (file.name, open(file.name, "rb"))}
    )
 
    result = response.json()
 
    return result["ai_report"]
 
interface = gr.Interface(
    fn=analyze_sales,
    inputs=gr.File(label="Upload Sales CSV"),
    outputs=gr.Textbox(label="AI Generated Business Report"),
    title="AI Sales Report Interpreter",
    description="Upload a sales dataset and generate AI-powered business insights."
)
 
interface.launch()