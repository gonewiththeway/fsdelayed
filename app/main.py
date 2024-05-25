import time
import random
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl
from typing import List

app = FastAPI()

class ImageRequest(BaseModel):
    urls: List[HttpUrl]

@app.post("/process-images/", summary="Process Image URLs", description="This endpoint accepts a list of image URLs and returns a list of processed image URLs with a random delay of 3 to 10 seconds.")
async def process_images(request: ImageRequest):
    # Introduce a random delay between 3 to 10 seconds
    delay = random.randint(3, 10)
    time.sleep(delay)
    
    # Assuming the response should be the same URL for all images
    processed_image_url = "https://learn.microsoft.com/en-us/azure/storage/blobs/media/storage-quickstart-blobs-portal/create-container-lrg.png#lightbox"
    return {"processed_urls": [processed_image_url for _ in request.urls]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
