from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import FormRecognizerClient
from azure.ai.formrecognizer import FormTrainingClient


AZURE_FORM_RECOGNIZER_ENDPOINT = "https://udacity-student-form-recognizer.cognitiveservices.azure.com/"
AZURE_FORM_RECOGNIZER_KEY = "6dd4ec8b9eeb48b1b44b441d132c6043"

endpoint = AZURE_FORM_RECOGNIZER_ENDPOINT
key = AZURE_FORM_RECOGNIZER_KEY

form_training_client = FormTrainingClient(endpoint=endpoint, credential=AzureKeyCredential(key))
saved_model_list = form_training_client.list_custom_models()
trainingDataUrl = "https://udacitymicthstorage.blob.core.windows.net/container-1?sp=racwdl&st=2022-10-31T11:56:17Z&se=2022-10-31T19:56:17Z&spr=https&sv=2021-06-08&sr=c&sig=WquV4gSqjaU3OwZSWxbYoATrd3C50AwK6%2FIYZRwgZiw%3D"


training_process = form_training_client.begin_training(trainingDataUrl, use_training_labels=False)
custom_model = training_process.result()

print(custom_model)

print(f"Custom Model ID's: {custom_model.model_id}")
print(f"Custom Model status: {custom_model.status}")