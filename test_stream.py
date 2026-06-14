import pandas as pd
import requests
import json

# Load the generated mock database
df = pd.read_csv("aircraft_technical_logs.csv")

# Convert the pandas dataframe into a json payload matching our Pydantic schema
payload = df.to_dict(orient="records")

# Send the payload to the ingestion endpoint
url = "http://127.0.0.1:8000/api/v1/ingest"
headers = {"Content-Type": "application/json"}

print("🚀 Initiating stream of 500 mock aircraft logs to pipeline...")
response = requests.post(url, data=json.dumps(payload), headers=headers)

print(f"Response Status: {response.status_code}")
print(f"Server Response: {json.dumps(response.json(), indent=2)}")