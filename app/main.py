import time
import random
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl
from typing import List
from fastapi.staticfiles import StaticFiles

app = FastAPI()

class ImageRequest(BaseModel):
    target_urls: List[HttpUrl]
    source_url: HttpUrl

# Mount the images directory to serve images
app.mount("/images", StaticFiles(directory="app/images"), name="images")

@app.post("/process-images/", summary="Process Image URLs", description="This endpoint accepts a list of target image URLs and a source image URL and returns a list of processed image URLs with a random delay of 3 to 10 seconds.")
async def process_images(request: ImageRequest):
    """
    Process a list of target image URLs and a source image URL.

    - **target_urls**: A list of target image URLs to be processed.
    - **source_url**: A source image URL.
    """
    # Introduce a random delay between 3 to 10 seconds
    delay = random.randint(3, 10)
    time.sleep(delay)

    # List all images in the images directory
    image_files = os.listdir("app/images")
    if not image_files:
        raise HTTPException(status_code=404, detail="No images found")

    # Shuffle the images
    random.shuffle(image_files)

    # Generate URLs for the images
    server_url = "https://fsdelayed.onrender.com"
    processed_urls = [f"{server_url}/images/{image_files[i % len(image_files)]}" for i in range(len(request.target_urls))]

    return {"processed_urls": processed_urls}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)