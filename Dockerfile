FROM python:3.6

# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt ./

RUN pip3 install -r requirements.txt

RUN python -m pip install -U pip setuptools
RUN python -m pip install matplotlib pillow
RUN python -m pip install opencv-python
# Installing Jupyter notebook
RUN python -m pip install jupyter
# Copy resource file
COPY resources/* ./resources/

# Bundle app source
COPY src/* ./src/

EXPOSE 8080 8888
CMD  [ "python", "jupyter notebook" ]