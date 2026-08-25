# DSS150P Lab 01 - Data Engineering Workspace

## Laboratory Title
Data Engineering Lifecycle and Source Systems Assessment

## Student Information
- **Full Name**: Candelaria, Zoeh Blythe Gunther D.
- **Student Number**: 2024102638

## Purpose of the Laboratory
This laboratory establishes a reproducible local data-engineering workspace and performs a first-pass technical assessment of multiple source systems. The activity demonstrates how source systems, data pipelines, storage platforms, and downstream consumers fit within the data engineering lifecycle. It covers environment setup, source profiling, API inspection, database schema creation, and data contract development.

## Software Requirements
- Python 3.x (tested with Python 3.14.7)
- Git (tested with Git 2.55.0)
- Docker Desktop with Docker Compose (tested with Docker 29.7.2)
- Visual Studio Code or any code editor
- Python packages: pandas, pyarrow, requests, sqlalchemy, psycopg2-binary, pyyaml

## Repository Structure
DSS150P_Lab01_Candelaria_ZoehBlytheGunther/
├── data/
│ ├── raw/ # Raw source files and API snapshot
│ └── evidence/ # Terminal outputs and verification evidence
├── docs/ # Documentation and analysis
├── sql/ # SQL initialization scripts
├── src/ # Python scripts
├── .gitignore
├── docker-compose.yml
├── requirements.txt
└── README.md

## Steps to Reproduce the Environment

### 1. Clone the Repository
```bash
git clone https://github.com/zo-good/DSS150P_Lab01_Candelaria_ZoehBlytheGunther.git
cd DSS150P_Lab01_Candelaria_ZoehBlytheGunther