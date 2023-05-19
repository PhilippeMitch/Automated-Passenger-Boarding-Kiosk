import io
import datetime
import pandas as pd
from PIL import Image
import requests
import io
import glob, os, sys, time, uuid

from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt
%matplotlib inline

from urllib.parse import urlparse
from io import BytesIO
from PIL import Image, ImageDraw

from video_indexer import VideoIndexer
from azure.cognitiveservices.vision.face import FaceClient
from azure.cognitiveservices.vision.face.models import TrainingStatusType
from msrest.authentication import CognitiveServicesCredentials

CONFIG = {
    'SUBSCRIPTION_KEY': 'YOUR_SUBSCRIPTION_KEY',
    'LOCATION': 'trial',
    'ACCOUNT_ID': 'YOUR_ACCOUNT_ID'
}

video_analysis = VideoIndexer(
    vi_subscription_key=CONFIG['SUBSCRIPTION_KEY'],
    vi_location=CONFIG['LOCATION'],
    vi_account_id=CONFIG['ACCOUNT_ID']
)

print(video_analysis.check_access_token())

### Upload Video to Video Indexer

uploaded_video_id = video_analysis.upload_to_video_indexer(
   input_filename='junior.mp4',
   video_name='junior-11-second',  # unique identifier for video in Video Indexer platform
   video_language='English'
)

print(f"Uploaded video id's: {uploaded_video_id}")

### Extract face thumbnail

info = video_analysis.get_video_info(uploaded_video_id, video_language='English')

keyframes = []
for shot in info["videos"][0]["insights"]["shots"]:
    for keyframe in shot["keyFrames"]:
        keyframes.append(keyframe["instances"][0]['thumbnailId'])


for keyframe in keyframes:
    img_str = video_analysis.get_thumbnail_from_video_indexer(uploaded_video_id,  keyframe)

thumbnail_id ="504218c6-7d5c-413a-a444-5bd2368c0b3c"

img_code = video_analysis.get_thumbnail_from_video_indexer(uploaded_video_id,  thumbnail_id)
img_stream = io.BytesIO(img_code)
img = Image.open(img_stream)
imshow(img)