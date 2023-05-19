# Project Description

The objective of this project is to develop a prototype of an automated passenger boarding kiosk
to assist with pre-flight boarding procedures. The automated system will have multiple functions
that can be used in a wide variety of business processes like airline boarding operations,
specifically identity verification to board the flight and automated customer feedback collection.

We are using Azure Vision services as Custom Vision, Form Recognizer, Face API and Video indexer.
* We store all of our data at the Azure Blob Storage
* he manifest table is a spreadsheet that lists the flight information for each passenger.
* Custom vision service will be used to build a custom lighter detection model first and use the custom model to detect lighter probability in given test images.
* Video Indexer will be used to match a given passenger's face from digital ID with the face extracted 30-second video.
* Azure Form Recognizer will be used to train a model to extract information from identification cards and boarding passes.
