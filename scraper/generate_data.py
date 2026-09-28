import csv
import random


cities = [
    "Pune",
    "Mumbai",
    "Nashik",
    "Nagpur",
    "Aurangabad",
    "Kolhapur",
    "Thane",
    "Bengaluru",
    "Hyderabad",
    "Delhi"
]


categories = [
    "Restaurant",
    "Cafe",
    "Hospital",
    "Hotel",
    "IT Company",
    "Gym",
    "Retail Store",
    "Education",
    "Salon",
    "Automobile"
]


sources = [
    "Sample Directory",
    "Business Directory",
    "Local Directory"
]


business_prefixes = [
    "Royal",
    "City",
    "Global",
    "Prime",
    "Smart",
    "National",
    "Green",
    "Metro",
    "Modern",
    "Elite"
]


business_types = {
    "Restaurant": "Restaurant",
    "Cafe": "Cafe",
    "Hospital": "Hospital",
    "Hotel": "Hotel",
    "IT Company": "Technology",
    "Gym": "Fitness",
    "Retail Store": "Retail",
    "Education": "Education",
    "Salon": "Beauty",
    "Automobile": "Automobile"
}


records = []


for i in range(1, 501):

    city = random.choice(cities)

    category = random.choice(categories)

    prefix = random.choice(business_prefixes)

    business_name = (
        f"{prefix} {business_types[category]} {i}"
    )

    address = (
        f"Main Road, {city}, Maharashtra"
    )

    phone = (
        "9"
        + "".join(
            random.choices(
                "0123456789",
                k=9
            )
        )
    )

    source = random.choice(sources)

    records.append([
        business_name,
        category,
        city,
        address,
        phone,
        source
    ])


# Create CSV file

with open(
    "businesses.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.writer(file)

    writer.writerow([
        "business_name",
        "category",
        "city",
        "address",
        "phone",
        "source"
    ])

    writer.writerows(records)


print("500 business records created successfully.")
print("File: businesses.csv")