# Installing Python and associated libraries

For the project and for installing necessary library build the docker image form the following command

```
 docker-compose build
```
Now run the docker image

```
 .\run.ps1
```
Or for linux
```
  run.sh
```

## Running the program

Inside the container you can run the program by following command

### 1. Image Filter Program:

```
root@ce0e3288f2fd:/app# cd src
root@ce0e3288f2fd:/app/src# python *.py
```

## Running the jupyter notebook

Inside the container for running jupyter notebook

```bash
#  jupyter notebook --ip 0.0.0.0 --no-browser --allow-root
```
Alternatively, from the command prompt, you can run

```
docker run -it -p 8888:8888 linear_regression_linear_regression:latest bash
```

inside bash run following

```
# jupyter notebook --ip 0.0.0.0 --no-browser --allow-root
```
It will allocate the ip and you can browse it from 

http://127.0.0.1:8888/tree

Following URLS consists all of the necessary code you may need for understanding the image filtering code

### 1. Mini-Batch Gradient Descent Program:

http://127.0.0.1:8888/notebooks/*.ipynb


## Problem Domain

### 1. Mini-Batch Gradient Descent Program:
