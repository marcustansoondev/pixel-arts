import os
import re

# Fix app.js
with open('app.js', 'r') as f:
    content = f.read()

# Find how many occurrences
matches = re.findall(r'(?:images/[a-z]+/)+images/', content)
print(f"Found {len(matches)} malformed paths in app.js")

# Replace
new_content = re.sub(r'(?:images/[a-z]+/)+images/', 'images/', content)

with open('app.js', 'w') as f:
    f.write(new_content)

# Fix missing suffixes in images/
renamed = 0
for root, dirs, files in os.walk('images'):
    for file in files:
        if file.endswith('.png') and not re.search(r'_\d+x\d+\.png$', file):
            old_path = os.path.join(root, file)
            new_path = os.path.join(root, file.replace('.png', '_50x50.png'))
            os.rename(old_path, new_path)
            renamed += 1

print(f"Renamed {renamed} images to add _50x50 suffix.")
