import yaml
from datetime import datetime, timezone

with open('docs/data_contract.yaml', 'r', encoding='utf-8') as f:
    contract = yaml.safe_load(f)

print('✅ YAML is valid!')
print(f"Dataset: {contract['dataset_name']}")
print(f"Version: {contract['version']}")
print(f"Primary Key: {contract['primary_key']}")
print(f"Schema fields: {len(contract['schema'])}")
print(f"Quality rules: {len(contract['quality_rules'])}")
print()
print('Schema:')
for field in contract['schema']:
    print(f"  - {field['name']}: {field['type']} (nullable={field['nullable']})")
print()
print('Quality Rules:')
for rule in contract['quality_rules']:
    print(f"  - {rule}")