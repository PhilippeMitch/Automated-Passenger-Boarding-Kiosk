The boarding-pass contains some sample boarding passes for the passengers listed in the manifest file. All these boarding passes are in PDF format, six (6) of them have been used to develop a custom recognizer model in subsequent steps.
The id-cards contains some sample digital IDs (California Driver License) for the passengers that is in the manifest file, they will be used to perform face verification by comparing the face image on the ID card with the face shown in a 30-second video.

The FlightManifest file contains the flight-specific details which are:

* Carrier
* Flight Number
* Class
* Flight Origin (From)
* Destination (To)
* Flight Date
* Baggage
* Seat
* Gate Number
* Boarding Time
* Ticket No.

Some of the ID card information

* First Name
* Last Name
* Date of Birth
* Sex

And other columns that indicates the status of the 5 types of validation: 

* NameValidation
* DoBValidation
* PersonValidation
* BoardingPassValidation
* LuggageValidation

In the image bellow we have all the required Azure Resources for this project.
![best](https://github.com/PedroToto/Automated-Passenger-Boarding-Kiosk/blob/main/material_preparation_step/resource_requirements.png)

In the second image bellow we are showing that manifest table is stored in Azure Blob Storage.
![best](https://github.com/PedroToto/Automated-Passenger-Boarding-Kiosk/blob/main/material_preparation_step/manifestTableInBlobStorage.png)
