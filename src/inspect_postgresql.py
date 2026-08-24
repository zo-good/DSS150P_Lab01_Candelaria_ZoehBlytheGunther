from sqlalchemy import create_engine, text
from datetime import datetime, timezone

# Connect to PostgreSQL
engine = create_engine('postgresql+psycopg2://dss150p:dss150p_lab@localhost:5432/dss150p_lab')

print("=" * 80)
print("POSTGRESQL SOURCE INSPECTION")
print("=" * 80)
print(f"Inspection started at (UTC): {datetime.now(timezone.utc).isoformat()}")

with engine.connect() as conn:
    # 1. List all tables
    print("\n=== ALL TABLES IN DATABASE ===")
    result = conn.execute(text("""
        SELECT table_schema, table_name
        FROM information_schema.tables
        WHERE table_schema NOT IN ('pg_catalog', 'information_schema')
        ORDER BY table_schema, table_name
    """))
    tables = result.fetchall()
    if tables:
        for table in tables:
            print(f"  {table[0]}.{table[1]}")
    else:
        print("  No tables found")
    
    # 2. Check for inventory_snapshot
    print("\n=== TABLE: inventory_snapshot ===")
    result = conn.execute(text("""
        SELECT table_schema, table_name
        FROM information_schema.tables
        WHERE table_name = 'inventory_snapshot'
    """))
    table_exists = result.fetchall()
    if not table_exists:
        print("  inventory_snapshot table not found!")
        print("  Listing all available tables:")
        result = conn.execute(text("""
            SELECT table_schema, table_name
            FROM information_schema.tables
            WHERE table_schema NOT IN ('pg_catalog', 'information_schema')
        """))
        for t in result.fetchall():
            print(f"    {t[0]}.{t[1]}")
    else:
        print(f"  Found: {table_exists[0][0]}.{table_exists[0][1]}")
        
        # 3. Get column information
        print("\n=== COLUMNS ===")
        result = conn.execute(text("""
            SELECT column_name, data_type, is_nullable, column_default
            FROM information_schema.columns
            WHERE table_name = 'inventory_snapshot'
            ORDER BY ordinal_position
        """))
        columns = result.fetchall()
        if columns:
            print(f"{'Column Name':<25} {'Data Type':<20} {'Nullable':<10} {'Default':<20}")
            print("-" * 75)
            for col in columns:
                default = str(col[3]) if col[3] else ""
                print(f"{col[0]:<25} {col[1]:<20} {col[2]:<10} {default:<20}")
        else:
            print("  No columns found")
        
        # 4. Get constraints
        print("\n=== CONSTRAINTS/KEYS ===")
        result = conn.execute(text("""
            SELECT conname, contype, pg_get_constraintdef(oid)
            FROM pg_constraint
            WHERE conrelid = 'inventory_snapshot'::regclass
        """))
        constraints = result.fetchall()
        if constraints:
            for con in constraints:
                constraint_type = {
                    'p': 'PRIMARY KEY',
                    'f': 'FOREIGN KEY',
                    'u': 'UNIQUE',
                    'c': 'CHECK',
                    'x': 'EXCLUSION'
                }.get(con[1], con[1])
                print(f"  {con[0]}: {constraint_type}")
                print(f"    Definition: {con[2]}")
        else:
            print("  No constraints found")
        
        # 5. Row count
        result = conn.execute(text("SELECT COUNT(*) FROM inventory_snapshot"))
        count = result.scalar()
        print(f"\n=== ROW COUNT ===")
        print(f"  inventory_snapshot has {count} rows")
        
        # 6. Sample rows
        print(f"\n=== FIRST 5 ROWS ===")
        result = conn.execute(text("SELECT * FROM inventory_snapshot LIMIT 5"))
        rows = result.fetchall()
        cols = result.keys()
        
        print("  " + " | ".join(cols))
        print("  " + "-" * 100)
        for row in rows:
            print("  " + " | ".join(str(val) for val in row))

print(f"\nInspection completed at (UTC): {datetime.now(timezone.utc).isoformat()}")