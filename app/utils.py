import os
import time
import boto3
from dotenv import load_dotenv
from google import genai

load_dotenv()

# Load config
GEMINI_KEY = os.getenv("GOOGLE_API_KEY")
AWS_REGION = os.getenv("AWS_REGION")
S3_BUCKET = os.getenv("S3_BUCKET_NAME")

# Clients (no keys needed, boto3 uses IAM role)
genai_client = genai.Client(api_key=GEMINI_KEY)
s3 = boto3.client("s3", region_name=AWS_REGION)

def generate_and_upload(prompt: str) -> str:
    """Generates a video with Veo-3 and uploads to S3. Returns public link."""

    # 1. Generate video
    operation = genai_client.models.generate_videos(
        model="veo-3.0-generate-preview",
        prompt=prompt,
    )

    while not operation.done:
        print("Waiting for video generation...")
        time.sleep(10)
        operation = genai_client.operations.get(operation)

    generated_video = operation.response.generated_videos[0]

    # 2. Save locally
    filename = f"video_{int(time.time())}.mp4"
    genai_client.files.download(file=generated_video.video)
    generated_video.video.save(filename)

    # 3. Upload to S3
    s3.upload_file(
        Filename=filename,
        Bucket=S3_BUCKET,
        Key=filename,
        ExtraArgs={"ContentType": "video/mp4"},
    )

    # 4. Public URL
    url = f"https://{S3_BUCKET}.s3.{AWS_REGION}.amazonaws.com/{filename}"
    return url