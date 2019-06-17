# image-classification-grab-ai-sea-challenge
- This project contains the basic solution for the [Grab SEA Computer Vision Challenge](https://www.aiforsea.com/computer-vision)

### Introduction
This repository contains a simple python API for classifying the cars based on the make, model and year.
It includes 
- Health check endpoint
- Classify endpoint to classify the car make, model and year.

This project uses the [TensorFlow](https://www.tensorflow.org) library for the image classification.


### Running as Docker
**Pre-requisites**
- [Docker](https://www.docker.com/)

**Run the app**
- Clone this repo
- Run the app using following commands
```
➜  image-classification-grab-ai-sea-challenge git:(master) docker build -t imgclassify .
➜  image-classification-grab-ai-sea-challenge git:(master) docker run -it -p 5000:5000 --name=imgclassify imgclassify
```

NOTE: Here I've used PORT variable as 5000

### Test the app
- Below commands can be used to check whether docker is up and running
```
➜  image-classification-grab-ai-sea-challenge git:(master) docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS                    NAMES
a339439f82ec        imgclassify         "python start.py"   19 minutes ago      Up 19 minutes       0.0.0.0:5000->5000/tcp   imgclassify
```

- Once the docker container is up and running. Image classification can be tested.

##### Health Check
```
$ curl -X GET 'http://localhost:5000/health'

{
  "status": "true"
}
```

##### Image Classification

**Testing the online image**
- Parameters
  - `type`: `url` 
  - `path`: `https://hips.hearstapps.com/hmg-prod/amv-prod-cad-assets/images/11q1/394021/2012-ferrari-ff-photo-394052-s-986x603.jpg`(Some image url)

```
➜  image-classification-grab-ai-sea-challenge git:(master) ✗ curl -X GET \
  'http://localhost:5000/classify?path=https://hips.hearstapps.com/hmg-prod/amv-prod-cad-assets/images/11q1/394021/2012-ferrari-ff-photo-394052-s-986x603.jpg&type=url'

{
  "result": [
    {
      "category": "ferrari ff coupe 2012",
      "score": "0.95450"
    },
    {
      "category": "mclaren mp4 12c coupe 2012",
      "score": "0.00958"
    },
    {
      "category": "bugatti veyron 16 4 convertible 2009",
      "score": "0.00581"
    },
    {
      "category": "lamborghini aventador coupe 2012",
      "score": "0.00544"
    },
    {
      "category": "jaguar xk xkr 2012",
      "score": "0.00435"
    }
  ]
}
```

**Testing the local image from the local path**
- Parameters
  - `type`: `local` 
  - `path`: `/app/tf_files/car_test/Bentley Mulsanne Sedan 2011/02587.jpg`(Local path to the file)

```
➜  image-classification-grab-ai-sea-challenge git:(master) ✗ curl -X GET \
  'http://localhost:5000/classify?path=/app/tf_files/car_test/Bentley%20Mulsanne%20Sedan%202011/02587.jpg&type=local'

{
  "result": [
    {
      "category": "bentley mulsanne sedan 2011",
      "score": "0.67537"
    },
    {
      "category": "bmw x5 suv 2007",
      "score": "0.10948"
    },
    {
      "category": "audi s6 sedan 2011",
      "score": "0.06003"
    },
    {
      "category": "chevrolet tahoe hybrid suv 2012",
      "score": "0.01831"
    },
    {
      "category": "bentley continental flying spur sedan 2007",
      "score": "0.01497"
    }
  ]
}
```

- Category classification with the higher score determines the car's category.

### Training the model with car training images
**Pre-requisites**
- [Python](https://www.python.org/)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/)

**Organising the training images**
- Car training and the test images can be downloaded [here](https://ai.stanford.edu/~jkrause/cars/car_dataset.html)
- I've downloaded and placed in `{YOUR_CODE_PATH}/image-classification-grab-ai-sea-challenge/tf_files/car_train`. More information below.
- The Car training images categorized in to the folders as below.

```
➜  image-classification-grab-ai-sea-challenge git:(master) pwd
{YOUR_CODE_PATH}/image-classification-grab-ai-sea-challenge
➜  image-classification-grab-ai-sea-challenge git:(master) cd tf_files
➜  tf_files git:(master) ls
car_test  car_train
➜  tf_files git:(master) cd car_train
➜  car_train git:(master) ls
'Acura Integra Type R 2001'                               'Chevrolet Silverado 1500 Classic Extended Cab 2007'  'Hyundai Elantra Touring Hatchback 2012'
'Acura RL Sedan 2012'                                     'Chevrolet Silverado 1500 Extended Cab 2012'          'Hyundai Genesis Sedan 2012'
'Acura TL Sedan 2012'                                     'Chevrolet Silverado 1500 Hybrid Crew Cab 2012'       'Hyundai Santa Fe SUV 2012'
'Acura TL Type-S 2008'                                    'Chevrolet Silverado 1500 Regular Cab 2012'           'Hyundai Sonata Hybrid Sedan 2012'
...
...
...
➜  car_train git:(master) cd Acura\ TL\ Sedan\ 2012 
➜  Acura TL Sedan 2012 git:(master) ls
00002.jpg  01705.jpg  01870.jpg  02589.jpg  03030.jpg  03772.jpg  04588.jpg  05281.jpg  05434.jpg  05918.jpg  06406.jpg  06784.jpg  07121.jpg  07392.jpg  08133.jpg
00740.jpg  01716.jpg  02364.jpg  02663.jpg  03152.jpg  03871.jpg  04816.jpg  05333.jpg  05545.jpg  05967.jpg  06516.jpg  06816.jpg  07175.jpg  07663.jpg
01214.jpg  01750.jpg  02491.jpg  02832.jpg  03169.jpg  03881.jpg  05052.jpg  05347.jpg  05748.jpg  06328.jpg  06751.jpg  06974.jpg  07346.jpg  08005.jpg
```

**Training the model**
- After classifying to the proper folders
- Training can be performed as below
```
➜  image-classification-grab-ai-sea-challenge git:(master) ✗ virtualenv venv
New python executable in /home/swaminathan/Documents/myrepo/image-classification-grab-ai-sea-challenge/venv/bin/python2
Not overwriting existing python script /home/swaminathan/Documents/myrepo/image-classification-grab-ai-sea-challenge/venv/bin/python (you must use /home/swaminathan/Documents/myrepo/image-classification-grab-ai-sea-challenge/venv/bin/python2)
Installing setuptools, pip, wheel...
done.
➜  image-classification-grab-ai-sea-challenge git:(master) ✗ source venv/bin/activate
(venv) ➜  image-classification-grab-ai-sea-challenge git:(master) ✗ pip install -r requirements.txt
(venv) ➜  image-classification-grab-ai-sea-challenge git:(master) ✗ export IMAGE_SIZE=224                             
(venv) ➜  image-classification-grab-ai-sea-challenge git:(master) ✗ export ARCHITECTURE="mobilenet_0.50_${IMAGE_SIZE}"
(venv) ➜  image-classification-grab-ai-sea-challenge git:(master) ✗ python -m scripts.retrain \                       
  --bottleneck_dir=tf_files/bottlenecks \
  --model_dir=tf_files/models/ \
  --output_graph=tf_files/retrained_graph.pb \
  --output_labels=tf_files/retrained_labels.txt \
  --architecture="${ARCHITECTURE}" \
  --image_dir=tf_files/car_train
WARNING:tensorflow:From /home/swaminathan/Documents/myrepo/image-classification-grab-ai-sea-challenge/scripts/retrain.py:274: __init__ (from tensorflow.python.platform.gfile) is deprecated and will be removed in a future version.
...
...
...
```

**Things to be noted**
- We use the [Mobilenet](https://ai.googleblog.com/2017/06/mobilenets-open-source-models-for.html) convolution network to perform the image categorization.
- Here `IMAGE_SIZE` is used as **224px**. More the more pixel better accuracy. Here we used the maximum pixel supported by the mobilenet.
- Here `ARCHITECTURE` is used as **mobilenet_0.50_${IMAGE_SIZE}**. Model factor **0.50** is used here. Model factor ranges between 0.25, 0.5, 0.75, 1.
- Here 4000 iterations are used. If `--how_many_training_steps=500` is specified, then it uses 500 iterations and it takes less time to train the model. More number of iterations better the accuracy.
- After the training the folder looks will like the below

```
➜  tf_files git:(master) pwd
{YOUR_CODE_PATH}/image-classification-grab-ai-sea-challenge/tf_files
➜  tf_files git:(master) ls
bottlenecks  car_test  car_train  models  retrained_graph.pb  retrained_labels.txt
```

- Here the model_graph `retrained_graph.pb` is generated after training and labels for the cars categories are populated in the `retrained_labels.txt` file(i.e. the folder names where the cars images are placed)

### References
This repository is created based on the below references
- For [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/) the new, ground up rewrite targeted at mobile devices
  use [this version of the codelab](https://codelabs.developers.google.com/codelabs/tensorflow-for-poets-2-tflite) 
* For the more mature [TensorFlow Mobile](https://www.tensorflow.org/mobile/mobile_intro) use 
  [this version of the codealab](https://codelabs.developers.google.com/codelabs/tensorflow-for-poets-2).
- Categorization of car training images is downloaded from [here](https://www.kaggle.com/jessicali9530/stanford-cars-dataset)

This repo contains simplified and trimmed down version of tensorflow's example image classification.
