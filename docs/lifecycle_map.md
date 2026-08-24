# Data Engineering Lifecycle Map

## Lifecycle Elements Table

| Lifecycle Element | What It Means | Example in This Lab | Primary Tool/Artifact | Possible Failure |
|------------------|---------------|---------------------|----------------------|------------------|
| Source system | Where data comes from originally | CSV files with customer data, JSON files with orders, Parquet files with products, REST API endpoint, PostgreSQL database | File systems, REST API, PostgreSQL database | API downtime, file corruption, database unavailable |
| Ingestion/acquisition | Getting data from sources into our pipeline | Python scripts reading CSV/JSON/Parquet files, making HTTP requests to API, SQL queries to database | Python scripts (profile_sources.py, inspect_api.py), requests library, SQLAlchemy | Network failures, timeout errors, incomplete data |
| Storage | Where data is kept and saved | Raw files in data/raw folder, PostgreSQL database in Docker container | Docker volume, local file system, PostgreSQL tables | Disk space full, data loss, backup failure |
| Processing/transformation | Cleaning and preparing data for use | Reading files with pandas, converting data types, handling missing values | pandas DataFrames, pyarrow for Parquet files | Type errors, memory problems, encoding issues |
| Data quality/validation | Checking data is correct and complete | Looking for null values, duplicate rows, wrong data types | profile_sources.py, data profiling reports, data_contract.yaml | Missed errors, invalid data, duplicates |
| Delivery | Making data available to users | PostgreSQL database queries, data contracts | PostgreSQL, API endpoints, data_contract.yaml | Access problems, slow performance |
| Consumer | People or apps that use the data | Data analysts, BI dashboards, reports | SQL clients, BI tools, Python scripts | Wrong interpretation, outdated data |

## Data Flow Diagram
[CSV Source] ────┐
│
[JSON Source] ───┤
│
[Parquet Source] ─┤──> [Pipeline/Process] ──> [Storage/Destination] ──> [Analyst/Application]
│ (Python Scripts) (PostgreSQL Database) (Consumer)
[REST API] ───────┤
│
[PostgreSQL] ─────┘


## Diagram Explanation

The diagram shows:
- **Sources** (left side): CSV, JSON, Parquet files, REST API, and PostgreSQL database
- **Pipeline** (middle): Python scripts that process the data
- **Storage** (right middle): PostgreSQL database where processed data is stored
- **Consumer** (far right): Analysts and applications that use the data

## Key Components

### Sources
- **customers.csv**: Customer information in CSV format
- **orders.json**: Order data in JSON format
- **products.parquet**: Product catalog in Parquet format
- **REST API**: External data from web service
- **PostgreSQL**: Database with inventory data

### Pipeline
- Python scripts for reading and processing data
- Data profiling and validation
- Transformation logic

### Storage
- PostgreSQL database (dss150p_lab)
- Docker volume for persistence
- Local files in data/raw/

### Consumers
- Data analysts running queries
- Business intelligence tools
- Applications needing data

## Checkpoint Verification

- [x] All required tools verified (Python, Git, Docker, Docker Compose)
- [x] Python virtual environment works with dependencies installed
- [x] PostgreSQL container runs and connection test succeeds
- [x] Git has at least one commit
- [x] Lifecycle map contains both table and diagram
- [x] Evidence files saved under data/evidence/
