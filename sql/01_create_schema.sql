-- DSS150P Lab 01 - Schema Creation for customers.csv
-- Chosen Source: customers.csv
-- This script creates the schema and table for customer master data
-- Based on profiling evidence from Task 2.2

-- Create lab schema if it does not already exist
CREATE SCHEMA IF NOT EXISTS dss150p_lab;

-- Create customers table
-- Data types chosen based on profiling:
--   customer_id: VARCHAR(10) - String pattern like 'C0001'
--   first_name: VARCHAR(50) - Short text field
--   last_name: VARCHAR(50) - Short text field
--   email: VARCHAR(100) - Email addresses (3 missing values found)
--   city: VARCHAR(50) - City names (2 missing values found)
--   signup_date: DATE - Date in YYYY-MM-DD format
--   customer_segment: VARCHAR(20) - 4 distinct values found
CREATE TABLE IF NOT EXISTS dss150p_lab.customers (  
    customer_id VARCHAR(10) PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100),
    city VARCHAR(50),
    signup_date DATE NOT NULL,
    customer_segment VARCHAR(20) NOT NULL,
    
    -- CHECK constraints based on profiling evidence
    CONSTRAINT ck_customer_id_format 
        CHECK (customer_id ~ '^C[0-9]{4}$'),
    
    CONSTRAINT ck_customer_segment_values 
        CHECK (customer_segment IN ('Professional', 'Retail', 'SME', 'Student')),
    
    CONSTRAINT ck_signup_date_range 
        CHECK (signup_date >= '2025-01-01' AND signup_date <= '2026-12-31')
);

-- Add indexes for frequently queried columns
CREATE INDEX IF NOT EXISTS idx_customers_email ON dss150p_lab.customers(email);
CREATE INDEX IF NOT EXISTS idx_customers_city ON dss150p_lab.customers(city);
CREATE INDEX IF NOT EXISTS idx_customers_segment ON dss150p_lab.customers(customer_segment);

-- Add table comment
COMMENT ON TABLE dss150p_lab.customers IS 'Customer master data from customers.csv';
COMMENT ON COLUMN dss150p_lab.customers.customer_id IS 'Unique customer identifier (pattern: C####)';
COMMENT ON COLUMN dss150p_lab.customers.first_name IS 'Customer first name';
COMMENT ON COLUMN dss150p_lab.customers.last_name IS 'Customer last name';
COMMENT ON COLUMN dss150p_lab.customers.email IS 'Customer email (may be missing)';
COMMENT ON COLUMN dss150p_lab.customers.city IS 'Customer city (may be missing)';
COMMENT ON COLUMN dss150p_lab.customers.signup_date IS 'Date when customer signed up';
COMMENT ON COLUMN dss150p_lab.customers.customer_segment IS 'Customer segment classification';