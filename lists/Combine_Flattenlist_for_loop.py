legacy_customers = ['Alice', 'Bob']
new_customers = ['Tiffany', 'Kristine']

raw_db = [legacy_customers, new_customers]

print(raw_db)

for legacy_customers in legacy_customers:
    new_customers.append(legacy_customers)
    
print(new_customers)