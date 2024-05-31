# Precize_Assessment_1

# Precize_Assessment_1

1. Set Up the Project Structure:

    - Create a directory for the project.
    - Inside the directory, create necessary files: `Dockerfile`, `requirements.txt`, and a Python script (e.g., `generate_report.py`).

2. Python Script (`generate_report.py`):

    - This script will use the Hugging Face API to fetch data about the models.
    - It will compile the list of the top 10 downloaded models.
    - It will save this report to a file.

3. Dockerfile:

    - This file will set up a Docker image with Python and the necessary libraries installed.
    - It will copy the Python script into the image and set it as the entry point.

4. Requirements.txt:

    - List the Python dependencies needed for the script, such as `requests`.

5. Scheduler:

    - Use a simple scheduling mechanism within the Python script to run the report generation periodically.

Here's how the project structure would look:


huggingface-report/
│
├── Dockerfile
├── generate_report.py
└── requirements.txt





 1. `generate_report.py`


import requests
import time

def fetch_top_models():
    url = "https://huggingface.co/api/models"
    response = requests.get(url)
    models = response.json()
    
    # Sort models by the number of downloads
    sorted_models = sorted(models, key=lambda x: x['downloads'], reverse=True)
    
    # Get the top 10 models
    top_10_models = sorted_models[:10]
    
    # Create a report
    report = "Top 10 Hugging Face Models by Downloads:\n"
    for i, model in enumerate(top_10_models, 1):
        report += f"{i}. {model['modelId']} - {model['downloads']} downloads\n"
    
    # Save the report to a file
    with open("top_10_models_report.txt", "w") as file:
        file.write(report)
    
    print("Report generated and saved to top_10_models_report.txt")

if __name__ == "__main__":
    fetch_top_models()
    print("Shutting down the container.")









 2. `Dockerfile`

Dockerfile
# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run generate_report.py when the container launches
CMD ["python", "generate_report.py"]


 3. `requirements.txt`


requests


 Building and Running the Docker Container

1. Build the Docker image:
    Open a terminal in the `huggingface-report` directory and run:

    docker build -t huggingface-report .
    

2. Run the Docker container:

    docker run huggingface-report
    

This Docker container will execute the `generate_report.py` script to fetch data from the Hugging Face model hub, compile a list of the top 10 downloaded models, save the report, and then stop.

 Submitting the Solution

1. Initialize a Git repository:

    git init
    

2. Add the files:

    git add .
    


3. Commit the files:

    git commit -m "Initial commit"
    

4. Create a GitHub repository:
    - Go to GitHub and create a new repository.

5. Push the local repository to GitHub:

    git remote add origin https://github.com/your-username/huggingface-report.git
    git push -u origin master


- generate_report.py functionality

Import Statements

import requests
import time

- requests: This is a Python library used to make HTTP requests. In this script, it is used to fetch data from the Hugging Face model hub API.
- time: This library provides various time-related functions. In this script, time is imported but not used. It can be removed if not needed.

Function Definition: fetch_top_models

def fetch_top_models():
url = "https://huggingface.co/api/models"
response = requests.get(url)
models = response.json()

- url: This is the API endpoint for Hugging Face models.
- requests.get(url): Sends a GET request to the specified URL.
- response.json(): Parses the JSON response from the API into a Python dictionary.

Sorting Models by Downloads

# Sort models by the number of downloads
sorted_models = sorted(models, key=lambda x: x['downloads'], reverse=True)

- sorted(models, key=lambda x: x['downloads'], reverse=True): This line sorts the list of models based on the number of downloads in descending order.
- models: The list of model data fetched from the API.
- key=lambda x: x['downloads']: Specifies that sorting should be done based on the downloads field of each model.
- reverse=True: Sorts the list in descending order (highest downloads first).

Extracting Top 10 Models

# Get the top 10 models
top_10_models = sorted_models[:10]

- sorted_models[:10]: Slices the sorted list to get the top 10 models.

Creating the Report

# Create a report
report = "Top 10 Hugging Face Models by Downloads:\n"
for i, model in enumerate(top_10_models, 1):
report += f"{i}. {model['modelId']} - {model['downloads']} downloads\n"

- report: Initializes a string to store the report.
- for i, model in enumerate(top_10_models, 1): Iterates over the top 10 models, where i is the index (starting from 1) and model is the model data.
- report += f"{i}. {model['modelId']} - {model['downloads']} downloads\n": Appends each model's rank, ID, and download count to the report string.

Saving the Report to a File

# Save the report to a file
with open("top_10_models_report.txt", "w") as file:
file.write(report)

print("Report generated and saved to top_10_models_report.txt")

- with open("top_10_models_report.txt", "w") as file: Opens a file named top_10_models_report.txt in write mode. The with statement ensures the file is properly closed after writing.
- file.write(report): Writes the report string to the file.
- print("Report generated and saved to top_10_models_report.txt"): Prints a confirmation message indicating that the report has been saved.

Main Execution Block

if __name__ == "__main__":
fetch_top_models()
print("Shutting down the container.")

- if __name__ == "__main__":: Ensures that the script runs the following code only if it is executed as the main module (not imported as a library).
- fetch_top_models(): Calls the fetch_top_models function to generate the report.
- print("Shutting down the container."): Prints a message indicating that the container is shutting down.

Summary
1. Fetch Data: The script fetches data about models from the Hugging Face API.
2. Sort Models: It sorts the models by the number of downloads in descending order.
3. Extract Top 10: It extracts the top 10 most downloaded models.
4. Generate Report: It creates a textual report listing these models.
5. Save Report: The report is saved to a file named top_10_models_report.txt.
6. Shutdown Message: It prints a message indicating the container is shutting down.

The entire script is designed to be run inside a Docker container that fetches the top models, generates a report, and then stops, allowing you to extract the report from the container.


The report generated by the script will be saved inside the Docker container at the path /app/top_10_models_report.txt.

1) Run the Docker Container

docker run huggingface-report

2) Find the Container ID

docker ps -a 

CONTAINER ID  IMAGE                               COMMAND                            CREATED                        STATUS                                     PORTS             NAMES
c8352f85bac5     huggingface-report    "python generate_rep…"     2 minutes ago            Exited (0) 2 minutes ago                            dazzling_allen

3) Copy the report

docker cp c8352f85bac5:/app/top_10_models_report.txt .

4) Verify the report

cat top_10_models_report.txt

Top 10 Hugging Face Models by Downloads:
1. google-bert/bert-base-uncased - 61509631 downloads
2. distilbert/distilbert-base-uncased - 20143253 downloads
3. openai-community/gpt2 - 11739061 downloads
4. FacebookAI/roberta-large - 11119441 downloads
5. FacebookAI/roberta-base - 10959847 downloads
6. FacebookAI/xlm-roberta-large - 8483278 downloads
7. FacebookAI/xlm-roberta-base - 6095594 downloads
8. distilbert/distilbert-base-uncased-finetuned-sst-2-english - 5734916 downloads
9. google-bert/bert-base-multilingual-cased - 4966281 downloads
10. google-t5/t5-small - 4737685 downloads

