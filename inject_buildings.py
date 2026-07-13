with open("buildings_app.js", "r") as f:
    buildings_js = f.read()

with open("app.js", "r") as f:
    content = f.read()

# 1. Add array
target1 = 'weather.forEach(w => { w.group = "weather"; });'
replacement1 = target1 + '\n\nconst buildings = [\n' + buildings_js + '\n];\nbuildings.forEach(b => { b.group = "buildings"; });'
content = content.replace(target1, replacement1)

# 2. Add to allItems
target2 = 'const allItems = [...animals, ...kitchen, ...vehicles, ...electronics, ...clothing, ...vegetables, ...weather,'
replacement2 = 'const allItems = [...animals, ...kitchen, ...vehicles, ...electronics, ...clothing, ...vegetables, ...weather, ...buildings,'
content = content.replace(target2, replacement2)

# 3. Add to resolutions
target3 = 'item.group === "weather") ? "50x50" : spriteResolution;'
replacement3 = 'item.group === "weather" || item.group === "buildings") ? "50x50" : spriteResolution;'
content = content.replace(target3, replacement3)

with open("app.js", "w") as f:
    f.write(content)

print("Successfully injected buildings into app.js")
