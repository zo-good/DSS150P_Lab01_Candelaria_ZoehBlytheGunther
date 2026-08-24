# Source Profile Analysis

## Profiling Date
2026-08-25 07:01:33

## Overview
This document provides interpretations of data profiling results for each source file. Observations focus on aspects that matter for future pipeline development.

---

## customers.csv

### Profile Summary
- **File size**: 17.76 KB (18,183 bytes)
- **Rows**: 250
- **Columns**: 7
- **Data types**: All string (including signup_date)
- **Missing values**: 3 emails (1.20%), 2 cities (0.80%)
- **Duplicates**: 2 fully duplicated rows
- **Distinct customer_id**: 247 (out of 250 rows)

### Observations for Pipeline Development

1. **Primary Key Issue**: The customer_id field has only 247 distinct values out of 250 rows, indicating duplicate records. The pipeline must implement deduplication logic before using customer_id as a primary key.

2. **Date Type Ambiguity**: signup_date is stored as string (not datetime). The pipeline needs to parse this field explicitly using pd.to_datetime() with a consistent format. The dates range from 2025-01-04 to 2026-05-16.

3. **Missing Value Strategy**: Small percentage of missing emails (3) and cities (2) require a decision: drop, fill with default, or flag for review. For a customer master dataset, these should likely be flagged rather than silently filled.

4. **Duplicate Risk**: 2 fully duplicated rows (0.80%) indicate potential data quality issues in the source system. The pipeline should log and remove duplicates during ingestion.

---

## orders.json

### Profile Summary
- **File size**: 79.53 KB (81,439 bytes)
- **Rows**: 250
- **Columns**: 9 (including nested shipping field)
- **Missing values**: None
- **Duplicates**: None
- **Nested structure**: shipping field contains region and method

### Observations for Pipeline Development

1. **Nested JSON Structure**: The shipping field contains a nested dictionary with egion (5 distinct values) and method (3 distinct values: Standard, Express, Pickup). The pipeline must flatten this structure for relational storage or use JSON functions for querying.

2. **Date Parsing Required**: order_timestamp is stored as string in ISO format (e.g., "2026-06-27T03:27:00"). The pipeline should parse this to datetime, noting the time component is present (unlike signup_date in customers.csv).

3. **Referential Integrity Check**: customer_id in orders references customers.csv, but orders only have 159 distinct customer_id values out of 247 available customers. The pipeline should validate that order customer_ids exist in the customer master.

4. **Shipping Fee Logic**: The shipping_fee field shows patterns based on method (0 for Pickup, 49-149 for Standard/Express). The pipeline could validate this business rule: Pickup should have 0 shipping fee.

---

## products.parquet

### Profile Summary
- **File size**: 14.31 KB (14,652 bytes)
- **Rows**: 200
- **Columns**: 7
- **Missing values**: None
- **Duplicates**: None
- **Data types**: Properly typed (string, float64, int32)

### Observations for Pipeline Development

1. **Clean Schema**: The Parquet file has well-defined types and no missing values, making it the most reliable source. The embedded schema can serve as a reference for data contracts.

2. **Stock Quantity Range**: Stock ranges from 0 to 250, with 0 indicating out-of-stock items. The pipeline should flag products with 0 stock for inventory management.

3. **Price Variation**: Unit prices range from 392.85 to 84,796.84, suggesting diverse product categories. The pipeline should validate prices are within expected ranges per category.

4. **Category and Brand Patterns**: With only 6 distinct categories and 6 distinct brands, this appears to be a controlled vocabulary. The pipeline can implement categorical validation.

---

## Cross-Source Observations

1. **Date Format Inconsistency**: 
   - customers.csv: signup_date is date-only (2025-04-27)
   - orders.json: order_timestamp includes time (2026-06-27T03:27:00)
   - Pipeline must handle both formats appropriately

2. **Key Relationships**:
   - customer_id links customers.csv to orders.json
   - No obvious foreign key to products in orders (orders don't reference product_id)
   - Future pipeline may need to create order_items table linking orders to products

3. **Data Quality Patterns**:
   - CSV has quality issues (duplicates, missing values)
   - JSON is complete but has nested structure complexity
   - Parquet is cleanest with proper typing

## Recommendations for Pipeline Development

1. **Implement Deduplication**: Remove duplicate customer records before loading
2. **Parse Dates Explicitly**: Convert all date/time strings to proper datetime types
3. **Flatten Nested JSON**: Extract shipping_region and shipping_method as separate columns
4. **Validate Referential Integrity**: Check that order customer_ids exist in customer master
5. **Create Data Contracts**: Document expected schema, types, and quality rules for each source
6. **Handle Missing Values**: Define strategy for null emails and cities in customer data
