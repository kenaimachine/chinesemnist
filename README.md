# Image Classification With Pytorch  
Image Classification Of Chinese Characters Using CNN model. 
---

## Description

This is a simple image classification project using CNN model. It is built with Pytorch.
The dataset is available from Kaggle (see below for link).

---
**TO START**

1. Download from Kaggle: https://www.kaggle.com/datasets/gpreda/chinese-mnist/download?datasetVersionNumber=7
2. Copy the folder 'chinesemnist' and upload to Google Dive or your local machine.
3. Copy the chinesemnistclassification.ipynb to 'chinesemnist' folder.
4. The creation of other directories and copying of images will be handled programmatically by `chinesemnistclassification.ipynb`.

---

**HOW TO USE**

1. If you only have uploaded the images as per 'TO START' instruction:
  * Just proceed to run all the jupyter notebook cells in sequential order.
2. If you have already run the code to create all the folders and move the images (essentially complete PART1), you just need to :
    * import the libraries and 
    * run 1.Initial Preparation
    * skip everything else from 1.2 to 1.5.
3. If you just wish to adjust the model and retrain the model, you need to:
    * import the libraries
    * run 1.Initial Preparation
    * skip everything else from 1.2 to 1.5.
    * run PART 2 and PART 3. Edit the code as required.
3. If you wish to make only inferences on test data you need to:
    * import the libraries
    * run 1. Initial Preparation
    * And eveything in PART 4. 

---
**Directory Structure**

In your google drive folder you will have the following directory structure set up:

(structure is similar if running on local machine)

```
Directory Structure In Google Drive:
MyDrive
|
+-- chinesemnist
     |
     +--data
        |
        +--chinesemnist.csv
        +--model.pth
        +--loss.png
        +--accuracy.png
        |
        +--data
        |  |
        |  +--(original chinese mnist image data)
        |   
        +--selectedData
        |  |
        |  +--(required character images)
        +--modelData
           |
           +--train
           |   |
           |   +--(folder of images by class)
           +--valid
           |   |
           |   +--(folder of images by class)
           +--test
               |
               +--images for testing

```  
