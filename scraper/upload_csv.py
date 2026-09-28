import pandas as pd
import requests


CSV_FILE = "businesses.csv"

API_URL = "http://127.0.0.1:8000/listings/bulk"


# Read CSV
df = pd.read_csv(CSV_FILE)

# Remove completely empty rows
df = df.dropna(how="all")

# Replace empty values with empty strings
df = df.fillna("")

# Make sure every column is a string
df["business_name"] = df["business_name"].astype(str)
df["category"] = df["category"].astype(str)
df["city"] = df["city"].astype(str)
df["address"] = df["address"].astype(str)
df["phone"] = df["phone"].astype(str)
df["source"] = df["source"].astype(str)


# Convert to JSON-compatible records
records = df[
    [
        "business_name",
        "category",
        "city",
        "address",
        "phone",
        "source"
    ]
].to_dict(orient="records")


print("Total records found:", len(records))

# Show first record for checking
print("First record:")
print(records[0])


# Send data to FastAPI
response = requests.post(
    API_URL,
    json=records
)


print("Status Code:", response.status_code)

print("Response:")
print(response.text)