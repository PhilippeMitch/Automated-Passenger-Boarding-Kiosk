# Project Description

The objective of this project is to develop a prototype of an automated passenger boarding kiosk
to assist with pre-flight boarding procedures. The automated system have multiple functions
that can be used in a wide variety of business processes like airline boarding operations,
specifically identity verification to board the flight and automated customer feedback collection.

We used Azure Vision services as Custom Vision, Form Recognizer, Face API and Video indexer.
* We store all of our data at the Azure Blob Storage
* The manifest table is a spreadsheet that lists the flight information for each passenger.
* Custom vision service have been used to build a custom lighter detection model first and use the custom model to detect lighter probability in given test images.
* Video Indexer was used to match a given passenger's face from digital ID with the face extracted 30-second video.
* Azure Form Recognizer was used to train a model to extract information from identification cards and boarding passes.

The "Project Problem Description.pdf" is a brief explaination about the problem, the data sources and the strategy to solve this problem. It also include the Azure service that will be used and how to validate the data and the performance metrics and threshold that will used when performing data validation.

The "DataFlow Diagram.pdf" is a data flow diagram that showing all the relevant components involved in the project and how they interact with each other.

![best](https://github.com/PedroToto/Automated-Passenger-Boarding-Kiosk/blob/main/step_1/Sample%20DataFlow%20Diagram.png)

The "Architecture Diagram.pdf" contains the architecture diagram showing the list of Azure services applied to your project.

![best](https://github.com/PedroToto/Automated-Passenger-Boarding-Kiosk/blob/main/step_1/Architecture-Guideline.png)


### Note:
* Each step folder have a readme file that give an overview of what that have been done to this step.
* The secret key should not be display directly in the code, there are other method to manage the secret key. 
* You can have all your key in a config file. 
* This connfig file should not have the key display on it. They other method to do that.
* You can use Key Vault to manage your secret key
