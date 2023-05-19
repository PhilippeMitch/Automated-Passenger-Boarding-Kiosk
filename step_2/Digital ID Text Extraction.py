from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import FormRecognizerClient

AZURE_FORM_RECOGNIZER_ENDPOINT = "https://udacity-student-form-recognizer.cognitiveservices.azure.com/"
AZURE_FORM_RECOGNIZER_KEY = "6dd4ec8b9eeb48b1b44b441d132c6043"

endpoint = AZURE_FORM_RECOGNIZER_ENDPOINT
key = AZURE_FORM_RECOGNIZER_KEY

form_recognizer_client = FormRecognizerClient(endpoint=endpoint, credential=AzureKeyCredential(key))

id_path = "../../digital_id_template/junior-arnold.jpg"

with open(id_path, "rb") as f:
       poller = form_recognizer_client.begin_recognize_identity_documents(identity_document=f)
id_documents = poller.result()

for idx, id_document in enumerate(id_documents):
    print("--------Recognizing ID document #{}--------".format(idx+1))
    first_name = id_document.fields.get("FirstName")
    if first_name:
        print("First Name: {} has confidence: {}".format(first_name.value[2:], first_name.confidence))
        last_name = id_document.fields.get("LastName")
    last_name = id_document.fields.get("LastName")
    if last_name:
        print("Last Name: {} has confidence: {}".format(last_name.value[2:], last_name.confidence))
    document_number = id_document.fields.get("DocumentNumber")
    if document_number:
        print("Document Number: {} has confidence: {}".format(document_number.value[2:], document_number.confidence))
    dob = id_document.fields.get("DateOfBirth")
    if dob:
        print("Date of Birth: {} has confidence: {}".format(dob.value, dob.confidence))
    doe = id_document.fields.get("DateOfExpiration")
    if doe:
        print("Date of Expiration: {} has confidence: {}".format(doe.value, doe.confidence))
    sex = id_document.fields.get("Sex")
    if sex:
        print("Sex: {} has confidence: {}".format(sex.value[2:], sex.confidence))
    address = id_document.fields.get("Address")
    if address:
        print("Address: {} has confidence: {}".format(address.value[2:], address.confidence))
    country_region = id_document.fields.get("CountryRegion")
    if country_region:
        print("Country/Region: {} has confidence: {}".format(country_region.value[2:], country_region.confidence))
    region = id_document.fields.get("Region")
    if region:
        print("Region: {} has confidence: {}".format(region.value[2:], region.confidence))