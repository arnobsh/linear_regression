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

## Import all libraries to requirements.txt

To import all the libraries to the local machine of ours you should put something like

```bash
pip freeze > requirements.txt
```

## Running the program

Inside the container you can run the program by following command

### 1. Mini-Batch Gradient Descent Program:

```
root@ce0e3288f2fd:/app# cd src
root@ce0e3288f2fd:/app/src# python batch_graddes.py
```

### 2. Life Expectancy Program:

```
root@ce0e3288f2fd:/app# cd src
root@ce0e3288f2fd:/app/src# python gapminder1.py
```

### 2. Multiple Linear Regression Example:

```
root@ce0e3288f2fd:/app# cd src
root@ce0e3288f2fd:/app/src# python multiple_linear_regression.py
```

### 2. Multiple Linear Regression Example:

```
root@ce0e3288f2fd:/app# cd src
root@ce0e3288f2fd:/app/src# python multiple_linear_regression.py
```
### 2. Polynomial Regression Example:

```
root@ce0e3288f2fd:/app# cd src
root@ce0e3288f2fd:/app/src# python poly_reg.py
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

Following URLS consists all of the necessary code you may need for understanding the linear regression code

### 1. Mini-Batch Gradient Descent Program:

http://127.0.0.1:8888/notebooks/batch_graddes.ipynb

### 2. Life Expectancy Program:

http://127.0.0.1:8888/notebooks/gapminder1.ipynb

### 3. Linear Regression Example From Scikit:

http://127.0.0.1:8888/notebooks/plot_ols.ipynb

### 4. Multiple Linear Regression Example:

http://127.0.0.1:8888/notebooks/multiple_linear_regression.ipynb

### 4. Polynomial Regression Example:

http://127.0.0.1:8888/notebooks/poly_reg.ipynb
