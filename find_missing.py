import os
import re

# Get expected from app.js
with open('app.js', 'r') as f:
    content = f.read()

expected_files = re.findall(r'filename:\s*"([^"]+)"', content)

# Get actual from images/
actual_files = []
for root, dirs, files in os.walk('images'):
    for file in files:
        actual_files.append(os.path.join(root, file))

# Compare
missing = []
for expected in expected_files:
    if expected not in actual_files:
        missing.append(expected)

print(f"Missing files: {len(missing)}")
for m in missing:
    print(m)
