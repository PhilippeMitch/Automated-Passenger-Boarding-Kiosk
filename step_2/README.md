In this step, we have used the boarding passes and digital ID as input data and extract personal information using Form Recognizer's prebuilt ID API.

**The Screeshots folder contains:**
* Screenshot proving the extracted data from the digital ID does match with the information on the ID (digital-ID-and-extracted-information.png)
* Screeshot showing the boarding passes are used to generate labels using label layout (boarding-pass-use-to-generate-labels) and label contents are uploaded to Azure Blob storage ()
* Screenshot proving the extracted data match with the boarding pass (boarding-pass-with-extracted-data.png)
* Screeshot proving the boarding pass and their training labels are stored (boarding-pass-uploaded-to-azure-blob-storage)

We used the boarding pass template to generate more boarding pass PDF files first.

![best](https://github.com/PedroToto/Automated-Passenger-Boarding-Kiosk/blob/main/step_2/Screeshots/boarding-pass.png)

We generated the label layout from the boarding passes using the "https://fott-2-1.azurewebsites.net/".

![best](https://github.com/PedroToto/Automated-Passenger-Boarding-Kiosk/blob/main/step_2/Screeshots/boarding-pass-use-to-generate-labels.png)

And use them to train a custom boarding pass recognizer model.
![best](https://github.com/PedroToto/Automated-Passenger-Boarding-Kiosk/blob/main/step_2/Screeshots/custom-boarding-pass-model-training.png)
