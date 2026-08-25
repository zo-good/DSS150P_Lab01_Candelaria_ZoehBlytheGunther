# DSS150P Lab 01 - Data Engineering Workspace

## Laboratory Title
Data Engineering Lifecycle and Source Systems Assessment

## Student Information
- **Full Name**: Candelaria, Zoeh Blythe Gunther
- **Student Number**: [ADD YOUR STUDENT NUMBER HERE]

## Purpose of the Laboratory
This laboratory establishes a reproducible local data-engineering workspace and performs a first-pass technical assessment of multiple source systems. The activity demonstrates how source systems, data pipelines, storage platforms, and downstream consumers fit within the data engineering lifecycle. It covers environment setup, source profiling, API inspection, database schema creation, and data contract development.

## Software Requirements
- Python 3.x (tested with Python 3.14.7)
- Git (tested with Git 2.55.0)
- Docker Desktop with Docker Compose (tested with Docker 29.7.2)
- Visual Studio Code or any code editor
- Python packages: pandas, pyarrow, requests, sqlalchemy, psycopg2-binary, pyyaml

## Steps to Reproduce the Environment

### 1. Clone the Repository
``bash
git clone https://github.com/zo-good/DSS150P_Lab01_Candelaria_ZoehBlytheGunther.git
cd DSS150P_Lab01_Candelaria_ZoehBlytheGunther

python -m venv .venv
.\.venv\Scripts\Activate.ps1

pip install -r requirements.txt

docker compose up -d
docker ps

python src/verify_environment.py

docker compose up -d

docker compose down

docker compose down -v

docker ps
docker logs dss150p-postgres

python src/verify_environment.py

python src/profile_sources.py

python src/inspect_api.py

python src/verify_schema.py

python src/validate_contract.py


### Step 2: Create docs/reflection.md

`powershell
@"
# Laboratory Reflection

## 1. Which source would be easiest to integrate into a future pipeline, and why?

The products.parquet file would be the easiest source to integrate into a future pipeline. The profiling revealed zero missing values, zero duplicate rows, and properly typed columns with embedded schema information. Parquet's self-describing nature eliminates type inference ambiguity that affects CSV and JSON files. The clean structure includes a clear primary key (product_id with 200 distinct values) and categorical fields with controlled vocabularies. The columnar storage format also provides efficient compression and fast query performance, making it ideal for analytical workloads with minimal transformation required.

## 2. Which source presents the greatest schema or data-quality risk, and what evidence supports your answer?

The orders.json file presents the greatest schema and data-quality risk. The profiling evidence shows a nested shipping field containing a dictionary with region and method keys, creating complexity for relational storage. While current data shows no missing values or duplicates, the semi-structured JSON format allows schema drift without warning. The order_timestamp is stored as a string requiring parsing, which could fail if the format changes. Additionally, the flexible nature of JSON means future records could have different keys or additional nesting levels that would break extraction logic and require pipeline modifications.

## 3. What could go wrong if a pipeline is built before the source schema and contract are understood?

Building a pipeline without understanding source schemas and contracts could lead to data type mismatches causing crashes or silent errors. Missing values would propagate downstream, corrupting aggregations and business metrics. Duplicate records would inflate counts and lead to incorrect decisions. Schema changes like renamed columns or changed types would break the pipeline unexpectedly. Without a data contract, consumers would not know field formats, nullability rules, or quality expectations, leading to data misinterpretation and misuse. The pipeline would be fragile, unreliable, and difficult to maintain.

## 4. How do Git, virtual environments, containers, and documentation improve reproducibility for a data-engineering team?

Git tracks all code and documentation changes, enabling version control and collaboration. Virtual environments isolate Python dependencies, ensuring consistent package versions across team members. Containers package the entire runtime environment including PostgreSQL, guaranteeing identical database behavior on any machine. Documentation explains setup procedures, data meanings, and quality rules that code alone cannot convey. Together, these tools ensure that any team member can recreate the exact environment and produce identical results, eliminating the common problem of code working on one machine but failing on another.

## Conclusion

This laboratory demonstrated the critical importance of systematic source assessment before pipeline development. By profiling sources, documenting schemas, creating data contracts, and establishing reproducible environments, we built a foundation for reliable data engineering that prioritizes understanding data before moving it.
