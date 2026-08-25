# Laboratory Reflection

## 1. Which source would be easiest to integrate into a future pipeline, and why?

The products.parquet file would be the easiest source to integrate into a future pipeline. The profiling revealed zero missing values, zero duplicate rows, and properly typed columns with embedded schema information. Parquet's self-describing nature eliminates type inference ambiguity that affects CSV and JSON files. The clean structure includes a clear primary key (product_id with 200 distinct values) and categorical fields with controlled vocabularies. The columnar storage format also provides efficient compression and fast query performance, making it ideal for analytical workloads with minimal transformation required.

## 2. Which source presents the greatest schema or data-quality risk, and what evidence supports your answer?

The orders.json file presents the greatest schema and data-quality risk. The profiling evidence shows a nested shipping field containing a dictionary with region and method keys, creating complexity for relational storage. While current data shows no missing values or duplicates, the semi-structured JSON format allows schema drift without warning. The order_timestamp is stored as a string requiring parsing, which could fail if the format changes. Additionally, the flexible nature of JSON means future records could have different keys or additional nesting levels that would break extraction logic.

## 3. What could go wrong if a pipeline is built before the source schema and contract are understood?

Building a pipeline without understanding source schemas and contracts could lead to data type mismatches causing crashes or silent errors. Missing values would propagate downstream, corrupting aggregations and business metrics. Duplicate records would inflate counts and lead to incorrect decisions. Schema changes like renamed columns or changed types would break the pipeline unexpectedly. Without a data contract, consumers would not know field formats, nullability rules, or quality expectations, leading to data misinterpretation and misuse.

## 4. How do Git, virtual environments, containers, and documentation improve reproducibility for a data-engineering team?

Git tracks all code and documentation changes, enabling version control and collaboration. Virtual environments isolate Python dependencies, ensuring consistent package versions across team members. Containers package the entire runtime environment including PostgreSQL, guaranteeing identical database behavior on any machine. Documentation explains setup procedures, data meanings, and quality rules that code alone cannot convey. Together, these tools ensure that any team member can recreate the exact environment and produce identical results.

## Conclusion

This laboratory demonstrated the critical importance of systematic source assessment before pipeline development. By profiling sources, documenting schemas, creating data contracts, and establishing reproducible environments, we built a foundation for reliable data engineering that prioritizes understanding data before moving it.
