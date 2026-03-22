import gradio as gr
import requests

API_URL = "http://127.0.0.1:8000/analyze"

def analyze_sales(file):

    response = requests.post(
        API_URL,
        files={"file": open(file.name, "rb")}
    )

    result = response.json()

    return result["insights"]

interface = gr.Interface(
    fn=analyze_sales,
    inputs=gr.File(label="Upload Sales CSV"),
    outputs=gr.Textbox(label="AI Generated Insights"),
    title="AI Sales Report Interpreter",
    description="Upload a sales dataset and generate business insights automatically."
)

interface.launch()