from fastapi import APIRouter, UploadFile, File
from app.services.file_loader import save_file
from app.services.text_extractor import extract_text
from app.services.ai_processor import process_text

router = APIRouter()


@router.post("/upload-document")
async def upload_document(file: UploadFile = File(...)):
    file_path = await save_file(file)

    text = extract_text(file_path)

    ai_result = process_text(text)

    return {
        "summary": ai_result.get("summary", ""),
        "key_points": ai_result.get("key_points", []),
        "raw_text_length": len(text),
        "mode": ai_result.get("mode", "ai")
    }


@router.get("/")
def root():
    return {"status": "running"}