# DSS150P Lab 01 - Data Engineering Workspace

## Laboratory Title
Data Engineering Lifecycle and Source Systems Assessment

## Student Information
- **Full Name**: Candelaria, Zoeh Blythe Gunther D.
- **Student Number**: 2024102638

## Purpose of the Laboratory
This laboratory establishes a reproducible local data-engineering workspace and performs a first-pass technical assessment of multiple source systems.

## Software Requirements
- Python 3.x (tested with Python 3.14.7)
- Git (tested with Git 2.55.0)
- Docker Desktop with Docker Compose (tested with Docker 29.7.2)
- Visual Studio Code
- Python packages: pandas, pyarrow, requests, sqlalchemy, psycopg2-binary, pyyaml

## Steps to Reproduce the Environment

### 1. Clone the Repository
git clone https://github.com/zo-good/DSS150P_Lab01_Candelaria_ZoehBlytheGunther.git
cd DSS150P_Lab01_Candelaria_ZoehBlytheGunther

text

### 2. Create and Activate Python Virtual Environment
python -m venv .venv
..venv\Scripts\Activate.ps1

text

### 3. Install Dependencies
pip install -r requirements.txt

text

### 4. Start PostgreSQL with Docker
docker compose up -d
docker ps

text

### 5. Verify Environment
python src/verify_environment.py

text

## PostgreSQL Commands

### Start PostgreSQL
docker compose up -d

text

### Stop PostgreSQL
docker compose down

text

### Stop and Remove Data Volume
docker compose down -v

text

## How to Run Python Scripts

### 1. Environment Verification
python src/verify_environment.py

text

### 2. Source Profiling
python src/profile_sources.py

text

### 3. API Inspection
python src/inspect_api.py

text

### 4. Schema Verification
python src/verify_schema.py

text

### 5. Data Contract Validation
python src/validate_contract.py

text

## Source Descriptions

### customers.csv
- Format: CSV
- Size: 17.76 KB, 250 rows, 7 columns
- Key: customer_id
- Issues: 2 duplicates, 3 missing emails, 2 missing cities

### orders.json
- Format: JSON with nested structure
- Size: 79.53 KB, 250 rows, 9 columns
- Key: order_id
- Issues: None

### products.parquet
- Format: Parquet
- Size: 14.31 KB, 200 rows, 7 columns
- Key: product_id
- Issues: None

### REST API
- Source: https://jsonplaceholder.typicode.com/posts
- Records: 100 posts

### PostgreSQL
- Database: dss150p_lab

## Known Limitations
1. API Authentication requirements unknown
2. Data Update Frequency not confirmed
3. Missing Values Strategy needs clarification
4. Schema Evolution for JSON API uncertain
5. Data Volume is small test data