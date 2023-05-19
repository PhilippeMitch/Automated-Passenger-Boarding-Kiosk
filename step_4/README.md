In this step, we build a custom object detection model that can detect if the passenger's carry-on items include a lighter or not. And use this model to detect if a given image contains a lighter.

Here is the summary of tasks you will do in this step:

* Create Azure Custom Vision resource and use it to build object detection model
* Upload lighter images as training images and complete image labeling
* Complete the training process
* Check the model performance and improve precision value is less than 75%
* Get the lighter probability in the provided test image

The "lighter_test_images" folder contains the images that we used to test the model.

**The creenshot folder contains:**
* Screenshot from the "https://customvision.ai" website while performing image labeling in the object detection model training process (lighter-images-labelling.png)
* Screenshot provin that we performed the training also from the Python API with training images with labels (model-training-1.png)
* Screenshots from the "https://customvision.ai" website while performing the training process of the object detection model (model-training-0.png)
* Screenshot showing the precision and recall values of the custom object detection model (model-training-4.png)
* Screenshot showing the model is deployed to an endpoint (lighter-custom-model-deployment.png)
* Screenshot showing how the custom model is used for prediction (detection-probability-on-each-image.png)
* Screenshot displaying lighter detection probability using the custom object detection model for every one of the 5 provided test images (detection-probability-on-each-image-2.png)
