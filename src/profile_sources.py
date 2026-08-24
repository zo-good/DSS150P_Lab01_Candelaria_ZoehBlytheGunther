from pathlib import Path
import pandas as pd
import numpy as np
from datetime import datetime, timezone

RAW = Path("data/raw")

def format_size(bytes):
    if bytes < 1024:
        return f"{bytes} bytes"
    elif bytes < 1024 * 1024:
        return f"{bytes/1024:.2f} KB"
    else:
        return f"{bytes/(1024*1024):.2f} MB"

def profile_df(df, name, filepath):
    print(f"\n{'='*80}")
    print(f"PROFILE: {name}")
    print(f"{'='*80}")
    
    size = filepath.stat().st_size
    print(f"\nFILE INFORMATION:")
    print(f"  File name: {name}")
    print(f"  File size: {format_size(size)}")
    print(f"  File size (bytes): {size:,}")
    
    print(f"\nSHAPE:")
    print(f"  Rows: {len(df):,}")
    print(f"  Columns: {len(df.columns):,}")
    
    print(f"\nCOLUMN NAMES (in order):")
    for i, col in enumerate(df.columns, 1):
        print(f"  {i}. {col}")
    
    print(f"\nDATA TYPES:")
    for col in df.columns:
        print(f"  {col}: {df[col].dtype}")
    
    print(f"\nMISSING VALUES:")
    for col in df.columns:
        nulls = df[col].isna().sum()
        pct = (nulls/len(df)*100) if len(df) > 0 else 0
        print(f"  {col}: {nulls:,} ({pct:.2f}%)")
    
    print(f"\nDUPLICATES:")
    try:
        # Convert all columns to string for duplicate check
        df_str = df.astype(str)
        dupes = df_str.duplicated().sum()
        print(f"  Fully duplicated rows: {dupes:,}")
    except:
        print(f"  Unable to check duplicates")
    
    print(f"\nDISTINCT VALUES:")
    for col in df.columns:
        try:
            print(f"  {col}: {df[col].nunique():,}")
        except:
            # For nested structures
            try:
                df_str = df[col].astype(str)
                print(f"  {col}: {df_str.nunique():,}")
            except:
                print(f"  {col}: (unhashable)")
    
    print(f"\nFIRST 5 RECORDS:")
    print(df.head().to_string())
    
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) > 0:
        print(f"\nNUMERIC STATISTICS:")
        for col in numeric_cols:
            print(f"  {col}:")
            print(f"    Min: {df[col].min()}")
            print(f"    Max: {df[col].max()}")
            print(f"    Mean: {df[col].mean():.2f}")
    
    print(f"\nDATE/TIME COLUMNS:")
    date_found = False
    for col in df.columns:
        if 'date' in col.lower() or 'time' in col.lower():
            try:
                converted = pd.to_datetime(df[col], errors='coerce')
                if converted.notna().sum() > 0:
                    print(f"  {col}:")
                    print(f"    Earliest: {converted.min()}")
                    print(f"    Latest: {converted.max()}")
                    date_found = True
            except:
                pass
    if not date_found:
        print("  None detected")

print("DSS150P LAB 01 - SOURCE DATA PROFILING")
print(f"Started at (UTC): {datetime.now(timezone.utc).isoformat()}")

# Profile CSV
csv_path = RAW / "customers.csv"
if csv_path.exists():
    print(f"\nReading CSV: {csv_path}")
    customers = pd.read_csv(csv_path)
    profile_df(customers, "customers.csv", csv_path)

# Profile JSON - handle nested shipping
json_path = RAW / "orders.json"
if json_path.exists():
    print(f"\nReading JSON: {json_path}")
    orders = pd.read_json(json_path)
    # Show original with nested field
    profile_df(orders, "orders.json", json_path)
    
    # Also show flattened version
    print(f"\n{'='*80}")
    print("ORDERS.JSON - SHIPPING DETAILS (Nested Structure)")
    print(f"{'='*80}")
    if 'shipping' in orders.columns:
        shipping_sample = orders['shipping'].head(3)
        print("\nSample shipping field values:")
        for i, val in enumerate(shipping_sample, 1):
            print(f"  Order {i}: {val}")
        
        # Flatten the shipping column
        shipping_df = pd.json_normalize(orders['shipping'])
        shipping_df.columns = ['shipping_' + col for col in shipping_df.columns]
        print("\nFlattened shipping columns:")
        print(f"  {list(shipping_df.columns)}")
        print(f"\nShipping region distinct values:")
        print(f"  {shipping_df['shipping_region'].value_counts().to_string()}")
        print(f"\nShipping method distinct values:")
        print(f"  {shipping_df['shipping_method'].value_counts().to_string()}")

# Profile Parquet
parquet_path = RAW / "products.parquet"
if parquet_path.exists():
    print(f"\nReading Parquet: {parquet_path}")
    products = pd.read_parquet(parquet_path)
    profile_df(products, "products.parquet", parquet_path)

print(f"\n{'='*80}")
print("PROFILING COMPLETE")
print(f"Completed at (UTC): {datetime.now(timezone.utc).isoformat()}")