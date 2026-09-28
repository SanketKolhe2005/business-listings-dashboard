Yes. Based on the **actual files you showed on GitHub**—`backend`, `database`, `scraper`, React/Vite files, `businesses.csv`, and `business_dashboard.sql`—use this README.

**Delete the current `README.md` and paste this entire content:**

````markdown
# Business Listings Dashboard

A full-stack Business Listings Dashboard developed using **React.js, FastAPI, MySQL, Python, and Recharts**.

This project was developed as part of a **Python Development Internship assignment**. The application stores business listing data in MySQL, provides REST APIs using FastAPI, and displays business analytics through an interactive React dashboard.

---

## Project Overview

The Business Listings Dashboard provides a centralized interface to analyze business listings based on:

- City
- Category
- Data Source
- Business Details

The application supports 500+ business listing records and provides visual reports through interactive charts.

---

## Features

### Dashboard

- Total number of businesses
- City-wise business distribution
- Category-wise business distribution
- Source-wise business distribution
- Interactive charts
- Searchable business listings
- Refresh dashboard data
- API connection status

### Business Listings

The application displays:

- Business ID
- Business Name
- Category
- City
- Address
- Phone
- Source

### Backend

- FastAPI REST API
- MySQL database integration
- SQLAlchemy ORM
- Individual listing insertion
- Bulk listing insertion
- Business listing retrieval
- City-wise reports
- Category-wise reports
- Source-wise reports

### Data Processing

- CSV dataset
- Python data processing
- Pandas
- Bulk upload through FastAPI

---

## Technology Stack

### Frontend

- React.js
- JavaScript
- Axios
- Recharts
- CSS
- Vite

### Backend

- Python
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn
- PyMySQL

### Database

- MySQL
- MySQL Workbench

### Data Processing

- Python
- Pandas
- CSV

### Development Tools

- Visual Studio Code
- Git
- GitHub
- MySQL Workbench

---

## Project Structure

```text
business-listings-dashboard/
│
├── backend/
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── requirements.txt
│
├── database/
│   └── business_dashboard.sql
│
├── scraper/
│   ├── businesses.csv
│   ├── generate_data.py
│   └── upload_csv.py
│
├── src/
│   ├── App.jsx
│   ├── App.css
│   ├── api.js
│   └── main.jsx
│
├── .gitignore
├── README.md
├── index.html
├── package.json
├── package-lock.json
└── vite.config.js
````

---

# System Architecture

```text
                    Business Listing Data
                            |
                            v
                       CSV Dataset
                            |
                            v
                    Python Processing
                            |
                            v
                      FastAPI API
                            |
                            v
                    MySQL Database
                            |
                            v
                    Dashboard APIs
                            |
                            v
                     React Frontend
                            |
                            v
              Charts + Searchable Table
```

---

# Database

## Database Name

```text
business_dashboard
```

## Table Name

```text
listing_master
```

## Table Structure

| Column        | Type         | Description          |
| ------------- | ------------ | -------------------- |
| id            | INT          | Primary key          |
| business_name | VARCHAR(255) | Business name        |
| category      | VARCHAR(150) | Business category    |
| city          | VARCHAR(100) | City                 |
| address       | TEXT         | Business address     |
| phone         | VARCHAR(50)  | Phone number         |
| source        | VARCHAR(100) | Data source          |
| created_at    | TIMESTAMP    | Record creation time |

---

# Database Dump

A MySQL database dump is included in:

```text
database/business_dashboard.sql
```

The SQL file contains the database structure and business listing data used by the project.

The database can be restored using MySQL Workbench or the MySQL command line.

---

# Backend API

The FastAPI backend runs on:

```text
http://127.0.0.1:8000
```

FastAPI Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### 1. API Health Check

```http
GET /
```

Response:

```json
{
  "message": "Business Listings API is running"
}
```

---

### 2. Test MySQL Connection

```http
GET /test-db
```

Checks whether FastAPI can successfully connect to MySQL.

Example response:

```json
{
  "database": "MySQL connected",
  "listing_count": 501
}
```

---

### 3. Create a Single Listing

```http
POST /listings
```

Example request:

```json
{
  "business_name": "ABC Restaurant",
  "category": "Restaurant",
  "city": "Pune",
  "address": "FC Road, Pune",
  "phone": "9876543210",
  "source": "Business Directory"
}
```

---

### 4. Bulk Insert Listings

```http
POST /listings/bulk
```

This endpoint accepts multiple business listings and inserts them into MySQL.

Example:

```json
[
  {
    "business_name": "ABC Restaurant",
    "category": "Restaurant",
    "city": "Pune",
    "address": "FC Road, Pune",
    "phone": "9876543210",
    "source": "Business Directory"
  },
  {
    "business_name": "National Cafe",
    "category": "Cafe",
    "city": "Mumbai",
    "address": "Main Road, Mumbai",
    "phone": "9127503042",
    "source": "Local Directory"
  }
]
```

---

### 5. Get All Listings

```http
GET /listings
```

Returns the business listings stored in the database.

---

### 6. Total Business Count

```http
GET /dashboard/total
```

Returns the total number of business listings.

Example:

```json
{
  "total_businesses": 501
}
```

---

### 7. City-wise Business Count

```http
GET /dashboard/city
```

Returns business counts grouped by city.

Example:

```json
[
  {
    "city": "Pune",
    "count": 52
  },
  {
    "city": "Mumbai",
    "count": 50
  }
]
```

---

### 8. Category-wise Business Count

```http
GET /dashboard/category
```

Returns business counts grouped by category.

---

### 9. Source-wise Business Count

```http
GET /dashboard/source
```

Returns business counts grouped by source.

---

# Data Collection

The project contains a CSV-based data preparation pipeline.

The dataset contains the required business listing fields:

* Business Name
* Category
* City
* Address
* Phone
* Source

The project uses a structured sample dataset for the implementation. Direct scraping from public business directories can be restricted by website terms, anti-bot mechanisms, or access limitations.

The sample data follows the required schema and is processed through the same upload and backend pipeline.

The project does not claim that the generated sample records were directly scraped from Google Maps or another business directory.

---

# Data Processing Pipeline

```text
businesses.csv
      |
      v
Python / Pandas
      |
      v
Data Cleaning
      |
      v
JSON Records
      |
      v
FastAPI /listings/bulk
      |
      v
MySQL listing_master
      |
      v
React Dashboard
```

---

# Scraper / Data Scripts

The `scraper` directory contains:

### `generate_data.py`

Generates the structured business listing dataset.

### `businesses.csv`

Contains the business listing dataset used by the application.

### `upload_csv.py`

Reads the CSV file and sends the business listing records to the FastAPI bulk insertion API.

---

# Dashboard Reports

## Total Businesses

Displays the total number of business listings stored in MySQL.

## City-wise Business Distribution

A bar chart displays the number of businesses in each city.

## Category Distribution

A pie chart displays the distribution of businesses across different categories.

Example categories include:

* Restaurant
* Cafe
* Hospital
* Hotel
* IT Company
* Gym
* Retail Store
* Education
* Salon
* Automobile

## Source Distribution

A pie chart displays the distribution of listings by source.

## Business Listing Table

The dashboard provides a searchable table containing:

* ID
* Business Name
* Category
* City
* Address
* Phone
* Source

---

# Installation

## Prerequisites

Install the following software:

* Python 3.10+
* Node.js
* npm
* MySQL
* MySQL Workbench
* Git

---

# Backend Setup

Open a terminal in the project directory.

```bash
cd backend
```

Create a Python virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

Install backend dependencies:

```bash
pip install -r requirements.txt
```

---

# MySQL Configuration

Create the database in MySQL:

```sql
CREATE DATABASE business_dashboard;

USE business_dashboard;
```

Create the table:

```sql
CREATE TABLE listing_master (
    id INT AUTO_INCREMENT PRIMARY KEY,
    business_name VARCHAR(255) NOT NULL,
    category VARCHAR(150),
    city VARCHAR(100),
    address TEXT,
    phone VARCHAR(50),
    source VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

Alternatively, restore the database using:

```text
database/business_dashboard.sql
```

---

# Environment Configuration

Create a `.env` file inside the `backend` directory.

```env
DATABASE_URL=mysql+pymysql://root:YOUR_PASSWORD@localhost:3306/business_dashboard
```

Replace:

```text
YOUR_PASSWORD
```

with your local MySQL root password.

Do not upload the `.env` file to GitHub.

---

# Start Backend

From the `backend` directory:

```bash
uvicorn main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

Swagger API documentation:

```text
http://127.0.0.1:8000/docs
```

---

# Frontend Setup

From the project root:

```bash
npm install
```

Install the required frontend packages:

```bash
npm install axios recharts
```

Start the React development server:

```bash
npm run dev
```

Frontend:

```text
http://localhost:5173
```

---

# Load Business Data

Go to the scraper directory:

```bash
cd scraper
```

Run:

```bash
python upload_csv.py
```

The script uploads the CSV records to:

```text
POST /listings/bulk
```

The records are stored in the MySQL `listing_master` table.

---

# Running the Application

## Terminal 1 - FastAPI

```bash
cd backend
venv\Scripts\activate
uvicorn main:app --reload
```

## Terminal 2 - React

From the project root:

```bash
npm run dev
```

Then open:

```text
http://localhost:5173
```

---

# Challenges

## 1. Data Collection

Direct scraping from business directories may be restricted by website policies and anti-bot mechanisms.

A structured sample dataset was therefore used for the implementation while maintaining the required data fields and complete data pipeline.

## 2. Bulk Data Insertion

A dedicated bulk API was implemented to insert multiple business records through a single request.

```text
POST /listings/bulk
```

## 3. Database Integration

SQLAlchemy was used to connect the FastAPI backend with MySQL and perform database operations.

## 4. Dashboard Integration

React communicates with FastAPI using Axios.

The backend provides aggregated data for the dashboard, including:

* Total businesses
* City-wise counts
* Category-wise counts
* Source-wise counts

## 5. Data Visualization

Recharts was used to create:

* Bar chart
* Category pie chart
* Source pie chart

---

# Future Improvements

Possible future improvements include:

* Integration with an approved business directory API
* Real-time business data collection
* Pagination
* Advanced search and filters
* Duplicate record detection
* Data validation
* User authentication
* Admin dashboard
* CSV export
* Cloud deployment
* Scheduled data updates
* Advanced analytics

---

# Demo

The project demonstration can cover:

1. Project structure
2. MySQL database
3. FastAPI backend
4. Swagger API documentation
5. Business data
6. Bulk insertion API
7. React dashboard
8. Total business count
9. City-wise chart
10. Category-wise chart
11. Source-wise chart
12. Searchable business listings

---

# Submission Contents

The repository includes:

```text
backend/
database/
scraper/
src/
README.md
package.json
package-lock.json
index.html
vite.config.js
.gitignore
```

The database dump is available at:

```text
database/business_dashboard.sql
```

---

# Author

## Sanket Kolhe

Computer Engineering Graduate

### Technologies Used

```text
React.js
FastAPI
Python
MySQL
SQLAlchemy
Pandas
Axios
Recharts
```

---

## License

This project was developed for educational and internship assignment purposes.

````


rather than falsely documenting a `frontend/` directory.
