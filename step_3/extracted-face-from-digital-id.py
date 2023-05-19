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

### Create Face Recognition Model

images = []
#img_raw = []
img_strs = []
for each_thumb in info['videos'][0]['insights']['faces'][0]['thumbnails']:
    if 'fileName' in each_thumb and 'id' in each_thumb:
        file_name = each_thumb['fileName']
        thumb_id = each_thumb['id']
        img_code = video_analysis.get_thumbnail_from_video_indexer(uploaded_video_id,  thumb_id)
        img_strs.append(img_code)
        img_stream = io.BytesIO(img_code)
        #img_raw.append(img_stream)
        img = Image.open(img_stream)
        images.append(img)

i = 1
for img in images:
    print(type(img))
    img.save('faces/human-face' + str(i) + '.jpg')
    i= i+ 1

DOMINIC_FACE_KEY = "15c1923c980b4909bbd516912d605c2a"
DOMINIC_FACE_ENDPOINT = "YOUR_ENDPOINT"

# Create a client
face_client = FaceClient(DOMINIC_FACE_ENDPOINT, CognitiveServicesCredentials(DOMINIC_FACE_KEY))

PERSON_GROUP_ID = str(uuid.uuid4())
person_group_name = 'dominic-santini-video-2'

## This code is taken from Azure Face SDK 
def build_person_group(client, person_group_id, pgp_name):
    print('Create and build a person group...')
    # Create empty Person Group. Person Group ID must be lower case, alphanumeric, and/or with '-', '_'.
    print('Person group ID:', person_group_id)
    client.person_group.create(person_group_id = person_group_id, name=person_group_id)

    # Create a person group person.
    human_person = client.person_group_person.create(person_group_id, pgp_name)
    # Find all jpeg human images in working directory.
    human_face_images = [file for file in glob.glob('*.jpg') if file.startswith("human-face")]
    # Add images to a Person object
    for image_p in human_face_images:
        with open(image_p, 'rb') as w:
            client.person_group_person.add_face_from_stream(person_group_id, human_person.person_id, w)

    # Train the person group, after a Person object with many images were added to it.
    client.person_group.train(person_group_id)

    # Wait for training to finish.
    while (True):
        training_status = client.person_group.get_training_status(person_group_id)
        print("Training status: {}.".format(training_status.status))
        if (training_status.status is TrainingStatusType.succeeded):
            break
        elif (training_status.status is TrainingStatusType.failed):
            client.person_group.delete(person_group_id=PERSON_GROUP_ID)
            sys.exit('Training the person group has failed.')
        time.sleep(5)

build_person_group(face_client, PERSON_GROUP_ID, person_group_name)

### Face Extraction From Digital ID

face_id_path = "dominic-santini.png"

def show_image_in_cell(face_url):
    img = Image.open(face_url)
    plt.figure(figsize=(10,5))
    plt.imshow(img)
    plt.show()

show_image_in_cell(face_id_path)

img = Image.open(face_id_path)

with open(face_id_path, mode="rb") as image_data:
    faces = face_client.face.detect_with_stream(
        image_data, 
        detection_model='detection_03', 
        recognition_model='recognition_04', 
        return_face_attributes=['qualityForRecognition']
    ) 

print(f"First face extracted: {faces[0].face_rectangle.as_dict()}")

print(f"Second face extracted: {faces[1].face_rectangle.as_dict()}")

# TAKEN FROM THE Azure SDK Sample
# Convert width height to a point in a rectangle
def getRectangle(faceDictionary):
    rect = faceDictionary.face_rectangle
    left = rect.left
    top = rect.top
    right = left + rect.width
    bottom = top + rect.height
    
    return ((left, top), (right, bottom))

def drawFaceRectangles(source_file, detected_face_object) :
    # Download the image from the url
    #response = requests.get(source_file)
    img = Image.open(source_file)
    # Draw a red box around every detected faces
    draw = ImageDraw.Draw(img)
    for face in detected_face_object:
        draw.rectangle(getRectangle(face), outline='red', width = 10)
    return img

drawFaceRectangles(face_id_path, faces)