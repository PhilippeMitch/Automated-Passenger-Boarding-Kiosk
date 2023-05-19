In this step, we extracted the face images from the digital ID and the 30-second video separately and then match them for similarity.

We used Azure Video Analyzer service to process video and Azure Face API service to get face from the digital ID.

Here is the summary of steps:

* Create Azure Video Analyzer and Face resources
* Upload video to Azure Video Indexer
* Extract face from video using Azure Video Indexer
* Create a Person model by combining various face frames
* Collect sentiment and emotion with Azure Video Indexer service
* Extract face from digital ID using Azure Face API
* Used Person model to match the face from the video with the face extracted from the digital ID

**The screenshots folder contains:**
* Screenshot showing the uploaded video in Azure Video Indexer (upload-local-video-to-azure-video-indexer-2.png)
* Screenshot showing face thumbnail extracted from Azure Video Indexer service (extract-thumbnail-from-uploaded-vdeo.png)
* Screenshot showing Person model is created based on face frames collected from Azure Video Indexer (person-model-based-on-faces-frame.png)
* Screenshot showing the face extraction code from the digital ID as input data using Azure Face API (extracted-face-from-digital-id-1, extracted-face-from-digital-id-2, extracted-face-from-digital-id-3)

The "Face Recognition Using Azure Face and Video Analyzer Services" notebook contains the code.
