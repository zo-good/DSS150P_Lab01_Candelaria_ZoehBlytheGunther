# Source Systems Inventory

## Overview
This document catalogs all source systems for the DSS150P Lab 01 activity. Each source is documented with its characteristics, structure, and acquisition requirements to support future pipeline development.

## Source Inventory Table

| Field | customers.csv | orders.json | products.parquet | REST API | PostgreSQL |
|-------|--------------|-------------|------------------|----------|------------|
| **Source Name** | Customer Master Data | Order Transactions | Product Catalog | External Data API | inventory_snapshot |
| **Source-System Type** | File System (CSV) | File System (JSON) | File System (Parquet) | Web Service (HTTP) | Relational Database |
| **Data Format** | CSV (Comma-Separated Values) | JSON (JavaScript Object Notation) | Parquet (Columnar Storage) | JSON (REST API response) | SQL Tables |
| **Structure Type** | Structured | Semi-structured | Structured | Semi-structured | Structured |
| **Expected Update Pattern** | Daily batch upload | Real-time streaming | Weekly batch update | On-demand (per request) | Transactional (continuous) |
| **Likely Acquisition Method** | File download/import via pandas | File download/import via pandas | File download/import via pyarrow | HTTP GET request via requests library | SQL query via SQLAlchemy |
| **Schema Location** | Header row in file | JSON keys (may be nested) | Embedded in Parquet metadata | API documentation (external) | Database information_schema |
| **Possible Primary/Business Key** | customer_id | order_id | product_id | Varies by endpoint | inventory_id |
| **Schema-Evolution Risk** | Low - fixed column structure | High - flexible JSON can change | Medium - dependent on Parquet schema version | High - API versioning and changes | Medium - ALTER TABLE operations |
| **Data-Quality Risk** | Missing values, duplicate records | Nested structures, inconsistent field types | Type enforcement may hide issues | Rate limiting, format changes, downtime | Constraint violations, data drift |

## Detailed Source Descriptions

### 1. customers.csv
- **Source Name**: Customer Master Data
- **Description**: Contains customer information records
- **File Location**: data/raw/customers.csv
- **File Size**: 17.8 KB
- **Data Format**: CSV with header row
- **Structure**: Structured (tabular)
- **Access Method**: pandas.read_csv()
- **Update Frequency**: Daily batch
- **Potential Issues**: 
  - Missing values in optional fields
  - Duplicate customer records
  - Inconsistent date formats

### 2. orders.json
- **Source Name**: Order Transactions
- **Description**: Contains order transaction data
- **File Location**: data/raw/orders.json
- **File Size**: 79.5 KB
- **Data Format**: JSON (possibly nested)
- **Structure**: Semi-structured
- **Access Method**: pandas.read_json()
- **Update Frequency**: Real-time
- **Potential Issues**:
  - Nested JSON structures requiring flattening
  - Variable fields across records
  - Inconsistent data types

### 3. products.parquet
- **Source Name**: Product Catalog
- **Description**: Contains product information
- **File Location**: data/raw/products.parquet
- **File Size**: 14.3 KB
- **Data Format**: Parquet (columnar)
- **Structure**: Structured with embedded schema
- **Access Method**: pandas.read_parquet() or pyarrow
- **Update Frequency**: Weekly batch
- **Potential Issues**:
  - Schema version changes between updates
  - Type enforcement may mask data issues

### 4. REST API
- **Source Name**: External Data API
- **Description**: External data source accessed via HTTP
- **API URL**: [TO BE FILLED from LMS]
- **Data Format**: JSON response
- **Structure**: Semi-structured
- **Access Method**: requests.get() with timeout
- **Update Frequency**: On-demand
- **Potential Issues**:
  - API rate limiting
  - Authentication requirements
  - Response format changes
  - Network connectivity issues

### 5. PostgreSQL Database
- **Source Name**: inventory_snapshot
- **Description**: Relational database table with inventory data
- **Connection**: postgresql://dss150p:dss150p_lab@localhost:5432/dss150p_lab
- **Data Format**: SQL table
- **Structure**: Structured (relational)
- **Access Method**: SQL queries via SQLAlchemy
- **Update Frequency**: Transactional
- **Potential Issues**:
  - Constraint violations
  - Data type mismatches
  - Missing indexes affecting performance

## Acquisition Requirements Summary

| Source | Required Tools | Authentication | Network Access | Special Considerations |
|--------|---------------|----------------|----------------|----------------------|
| customers.csv | pandas | None | No | Ensure correct encoding |
| orders.json | pandas | None | No | Handle nested structures |
| products.parquet | pyarrow/pandas | None | No | Verify Parquet schema version |
| REST API | requests | [Per instructor] | Yes | Use timeout, handle rate limits |
| PostgreSQL | SQLAlchemy/psycopg2 | Username/Password | Local (Docker) | Container must be running |

## Next Steps
- Profile each source to understand exact schema (Task 2.2)
- Retrieve API data and document structure (Task 2.3)
- Inspect PostgreSQL table structure (Task 2.4)
- Create data contract based on findings (Task 2.5)
