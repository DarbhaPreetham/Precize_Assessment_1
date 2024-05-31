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
