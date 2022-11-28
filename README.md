# depression-detection-using-text

This is a simple Wave application to detect depression level of a text. 

## Installation 

Follow the instructions [here](https://wave.h2o.ai/docs/installation) to download and run the latest Wave Server, a requirement for all sample apps. Then, choose an app from below for setup instructions.

## Running this App Locally

### System Requirements

1. Python 3.7+
2. pip3


### 1. Run the Wave Server

New to H2O Wave? We recommend starting in the documentation to [download and run](https://wave.h2o.ai/docs/installation) the Wave Server on your local machine. Once the server is up and running you can easily use any Wave app.

### 2. Setup Your Python Environment

```bash
gh repo clone Pusse-01/h2o_wave_app--depression-detection-using-texts
```
Install the pip:

```bash
sudo apt-get install python-pip
```

Install the virtual environment:

```bash
sudo pip install virtualenv
```

Create a new virtualenv

```bash
virtualenv -p python3 yourVenv
```

To activate:

```bash
source yourVenv/bin/activate
```

Install Requirements:

```bash
pip install -r requirements.txt
```

To exit your new virtualenv, just ```deactivate ```


### 3. Run the App

```bash
wave run app.py
```

### 4. View the App
Point your favorite web browser to [localhost:10101](http://localhost:10101)

