from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
from typing import Optional
from helpers import generate_image
from PIL import Image
import numpy as np
from io import BytesIO
import uvicorn
import os
import shutil

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/{name}')
def index(name):
    return {"name":name}

# Useless Pydantic Model and routes just to test API
class Blog(BaseModel):
    title : str
    body : str
    published_at : Optional[bool]

def load_image_into_numpy_array(data):
    return np.array(Image.open(BytesIO(data)))

@app.post('/blog')
def new_blog(request: Blog):
    return {"data_recieved": request}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    with open(os.path.join(f"images/input/", file.filename), 'wb+') as buffer:
        shutil.copyfileobj(file.file, buffer)
    input_file_path = f"images/input/{file.filename}"
    output_file_name = generate_image(input_file_path)
    output_file_path = f"images/output/{output_file_name}"
    return FileResponse(output_file_path)


if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=9000)