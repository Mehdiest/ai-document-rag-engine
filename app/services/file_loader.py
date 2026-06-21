# app/services/file_loader.py

from fastapi import UploadFile
import os

async def save_file(file: UploadFile, destination: str = "temp") -> str:
    os.makedirs(destination, exist_ok=True)

    file_path = os.path.join(destination, file.filename)

    content = await file.read()
    with open(file_path, "wb") as f:
        f.write(content)

    return file_path