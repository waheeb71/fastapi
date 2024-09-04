from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
import os

app = FastAPI()

# تحديد مسار المجلد الذي يحتوي على ملفات PDF
PDF_FOLDER = "folder"

@app.get("/")
def read_root():
    return {"message": "Welcome to the PDF viewer"}

@app.get("/pdfs/")
def list_pdfs():
    try:
        pdf_files = [f for f in os.listdir(PDF_FOLDER) if f.endswith(".pdf")]
        return {"pdf_files": pdf_files}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/pdfs/{filename}")
def get_pdf(filename: str):
    file_path = os.path.join(PDF_FOLDER, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(file_path, media_type="application/pdf")

