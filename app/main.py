from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl
from typing import List

app = FastAPI()

class ImageRequest(BaseModel):
    urls: List[HttpUrl]

@app.post("/process-images/")
async def process_images(request: ImageRequest):
    # Assuming the response should be the same URL for all images
    processed_image_url = "https://learn.microsoft.com/en-us/azure/storage/blobs/media/storage-quickstart-blobs-portal/create-container-lrg.png#lightbox"
    return {"processed_urls": [processed_image_url for _ in request.urls]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
