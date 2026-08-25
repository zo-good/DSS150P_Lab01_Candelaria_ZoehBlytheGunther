import yaml

with open('docs/data_contract.yaml', 'r', encoding='utf-8') as f:
    contract = yaml.safe_load(f)

print('=== DATA CONTRACT REQUIREMENTS CHECK ===')
print()

if len(contract['schema']) >= 5:
    print(f"✅ Schema has {len(contract['schema'])} fields (required: at least 5)")
else:
    print(f"❌ Schema has only {len(contract['schema'])} fields (need 5+)")

if len(contract['quality_rules']) >= 4:
    print(f"✅ Has {len(contract['quality_rules'])} quality rules (required: at least 4)")
else:
    print(f"❌ Has only {len(contract['quality_rules'])} quality rules (need 4+)")

rules_text = ' '.join(contract['quality_rules'])
if 'unique' in rules_text.lower() or 'null' in rules_text.lower():
    print('✅ Has key uniqueness or nullability rule')
else:
    print('❌ Missing key uniqueness or nullability rule')

if 'format' in rules_text.lower() or 'pattern' in rules_text.lower() or 'between' in rules_text.lower() or 'one of' in rules_text.lower():
    print('✅ Has domain/range/format rule')
else:
    print('❌ Missing domain/range/format rule')

required_fields = ['dataset_name', 'version', 'owner', 'source_type', 'source_format', 
                   'acquisition_method', 'expected_update_pattern', 'primary_key', 
                   'schema', 'quality_rules', 'freshness_expectation', 'duplicate_policy', 
                   'schema_evolution_policy', 'consumer', 'notes']

print()
print('Required fields:')
for field in required_fields:
    if field in contract:
        print(f"  ✅ {field}")
    else:
        print(f"  ❌ {field} MISSING")
