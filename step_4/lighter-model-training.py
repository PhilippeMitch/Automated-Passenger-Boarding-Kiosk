import requests
from urllib.parse import urlparse
from io import BytesIO
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import os, time, uuid

from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region
from msrest.authentication import ApiKeyCredentials


TRAINING_ENDPOINT = "https://eastus.api.cognitive.microsoft.com/"
training_key = "f4381dc99b5247c3a5fb8b28994f3ae7"
training_resource_id = '/subscriptions/21c53bc7-9f96-4753-9901-99cd641ad4e7/resourceGroups/ODL-AIND-213226/providers/Microsoft.CognitiveServices/accounts/custom-vision-training'

training_credentials = ApiKeyCredentials(in_headers={"Training-key": training_key})
trainer = CustomVisionTrainingClient(TRAINING_ENDPOINT, training_credentials)

print(f"API Version: {trainer.api_version}")

# Find the object detection domain
obj_detection_domain = next(domain for domain in trainer.get_domains() if domain.type == "ObjectDetection" and domain.name == "General")

# Create a new project
print ("Your Object Detection Training project has been created. Please move on.")
project_name = "Lighter detection"
project = trainer.create_project(project_name, domain_id=obj_detection_domain.id)


print(f"Project creation: {project.status}")

lighter_tag = trainer.create_tag(project.id, "Lighter")


iteration = trainer.train_project(project.id)
while (iteration.status != "Completed"):
    iteration = trainer.get_iteration(project.id, iteration.id)
    print ("Training status: " + iteration.status)
    print ("Waiting 10 seconds...")
    time.sleep(10)


print(iteration.as_dict())



# 

iteration_list = trainer.get_iterations(project.id)
train_iteration = []
for iteration_item in iteration_list:
    print(iteration_item)
    train_iteration.append(iteration_item)
    print("=====================================")


print(train_iteration[0].id, iteration_list[0].id)

model_perf = trainer.get_iteration_performance(project.id, iteration_list[0].id)

print(model_perf.as_dict())


### Publish the model


# iteration_id = model_perf.as_dict()['per_tag_performance'][0]['id']
iteration_id = iteration_list[0].id
print("Iteration ID ", iteration_id)


publish_iteration_name = "lighter-object-detection-custom"

trainer.publish_iteration(project.id, iteration_id, publish_iteration_name, prediction_resource_id)
print ("Done!")

### Perform Prediction

PREDICTION_ENDPOINT = 'https://eastus.api.cognitive.microsoft.com/'
prediction_key = "a1da0e1ce0ed4c20ade39f6d810e5c2e"
prediction_resource_id = "/subscriptions/21c53bc7-9f96-4753-9901-99cd641ad4e7/resourceGroups/ODL-AIND-213226/providers/Microsoft.CognitiveServices/accounts/custom-vision-prediction"


prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(PREDICTION_ENDPOINT, prediction_credentials)


local_image_path = 'lighter_test_images'



def perform_prediction(image_file_name):
    with open(os.path.join (local_image_path,  image_file_name), "rb") as image_contents:
        results = predictor.detect_image(project.id, publish_iteration_name, image_contents.read())
        # Display the results.
        for prediction in results.predictions:
            print("\t" + prediction.tag_name +
                  ": {0:.2f}%".format(prediction.probability * 100))


file_name = "lighter_test_set_1of5.jpg"

perform_prediction(file_name)



import glob, os, sys, time, uuid

human_face_images = os.listdir('lighter_test_images')
print(human_face_images)


def perform_prediction_on_multiple_images(image_folder):
    image_list = os.listdir(image_folder)
    for image_file_name in image_list:
        with open(os.path.join (image_folder,  image_file_name), "rb") as image_contents:
            results = predictor.detect_image(project.id, publish_iteration_name, image_contents.read())
            # Display the results.
            for prediction in results.predictions:
                print("\t" + prediction.tag_name + ": {0:.2f}% bbox.left = {1:.2f}, bbox.top = {2:.2f}, bbox.width = {3:.2f}, bbox.height = {4:.2f}".format(prediction.probability * 100, prediction.bounding_box.left, prediction.bounding_box.top, prediction.bounding_box.width, prediction.bounding_box.height))
            print(f"=================== Image name => {image_file_name} ======================================================")



perform_prediction_on_multiple_images(local_image_path)