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