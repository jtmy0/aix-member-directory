import json
from json_repair import repair_json

with open('members.json', 'r', encoding='utf-8') as f:
    content = f.read()

# Repair the broken JSON
fixed = repair_json(content)

# Verify by parsing
data = json.loads(fixed)
print(f'OK: {len(data["members"])} members')

# Write clean JSON
with open('members.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print('Written clean JSON')

# Also write a Python backup so we can regenerate cleanly later
with open('members_backup.py', 'w', encoding='utf-8') as f:
    f.write('# -*- coding: utf-8 -*-\n')
    f.write('members_data = ')
    f.write(repr(data))
