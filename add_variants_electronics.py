import sys

variants = [
    ("smartphone_gold", "Gold Smartphone", "Mobile"),
    ("smartphone_navy", "Navy Smartphone", "Mobile"),
    ("laptop_rose", "Rose Laptop", "Computing"),
    ("laptop_teal", "Teal Laptop", "Computing"),
    ("headphones_mint", "Mint Headphones", "Audio"),
    ("headphones_purple", "Purple Headphones", "Audio"),
    ("smartwatch_pink", "Pink Smartwatch", "Wearable"),
    ("smartwatch_gold", "Gold Smartwatch", "Wearable"),
    ("gaming_console_neon", "Neon Gaming Console", "Gaming"),
    ("gaming_console_crimson", "Crimson Gaming Console", "Gaming"),
    ("game_controller_mint", "Mint Game Controller", "Gaming"),
    ("game_controller_purple", "Purple Game Controller", "Gaming"),
    ("digital_camera_rose", "Rose Digital Camera", "Imaging"),
    ("digital_camera_navy", "Navy Digital Camera", "Imaging"),
    ("tablet_gold", "Gold Tablet", "Mobile"),
    ("tablet_mint", "Mint Tablet", "Mobile"),
    ("mechanical_keyboard_neon", "Neon Mechanical Keyboard", "Peripherals"),
    ("mechanical_keyboard_pink", "Pink Mechanical Keyboard", "Peripherals"),
    ("optical_mouse_crimson", "Crimson Optical Mouse", "Peripherals"),
    ("optical_mouse_mint", "Mint Optical Mouse", "Peripherals"),
    ("vr_headset_purple", "Purple VR Headset", "Gaming"),
    ("vr_headset_navy", "Navy VR Headset", "Gaming"),
    ("audio_speaker_white", "White Audio Speaker", "Audio"),
    ("audio_speaker_neon", "Neon Audio Speaker", "Audio"),
    ("studio_microphone_gold", "Gold Studio Microphone", "Audio"),
    ("studio_microphone_pink", "Pink Studio Microphone", "Audio"),
    ("electronic_calculator_mint", "Mint Electronic Calculator", "Office"),
    ("electronic_calculator_rose", "Rose Electronic Calculator", "Office"),
    ("wifi_router_white", "White Wi-Fi Router", "Networking"),
    ("wifi_router_purple", "Purple Wi-Fi Router", "Networking"),
    ("floppy_disk_neon", "Neon Floppy Disk", "Storage"),
    ("floppy_disk_crimson", "Crimson Floppy Disk", "Storage"),
    ("usb_flash_drive_gold", "Gold USB Flash Drive", "Storage"),
    ("usb_flash_drive_mint", "Mint USB Flash Drive", "Storage"),
    ("cd_player_pink", "Pink CD Player", "Audio"),
    ("cd_player_navy", "Navy CD Player", "Audio"),
    ("cassette_tape_neon", "Neon Cassette Tape", "Audio"),
    ("cassette_tape_gold", "Gold Cassette Tape", "Audio"),
    ("mp3_player_mint", "Mint MP3 Player", "Audio"),
    ("mp3_player_crimson", "Crimson MP3 Player", "Audio"),
    ("retro_radio_rose", "Rose Retro Radio", "Audio"),
    ("retro_radio_teal", "Teal Retro Radio", "Audio"),
    ("smart_speaker_white", "White Smart Speaker", "Audio"),
    ("smart_speaker_purple", "Purple Smart Speaker", "Audio"),
    ("walkie_talkie_mint", "Mint Walkie Talkie", "Communication"),
    ("walkie_talkie_navy", "Navy Walkie Talkie", "Communication"),
    ("quadcopter_drone_neon", "Neon Quadcopter Drone", "Gadget"),
    ("quadcopter_drone_gold", "Gold Quadcopter Drone", "Gadget"),
    ("video_projector_pink", "Pink Video Projector", "Display"),
    ("video_projector_navy", "Navy Video Projector", "Display"),
]

new_lines = []
for idx, (vid, name, vtype) in enumerate(variants):
    desc = f"A colorful {name.lower()} variant."
    ending = "," if idx < len(variants) - 1 else ""
    line = f'    {{ id: "{vid}", name: "{name}", filename: "images/electronics/{vid}_50x50.png", category: "electronics", type: "{vtype}", material: "Various", rarity: "★★★☆☆", description: "{desc}" }}{ending}'
    new_lines.append(line)

with open("app.js", "r") as f:
    content = f.read()

# find the last element in electronics
# Actually I'll find where `const electronics = [` ends. It's before `const clothing = [`.
# Wait, let's just use `    { id: "eink_reader", name: "E-Ink Reader"` which is probably the last element in electronics.
# Wait, I don't know the last element in electronics. Let's just find `];` before `// Clothing dataset` or `const clothing`.

import re
match = re.search(r'\];\s*// Clothing dataset\s*const clothing = \[', content)
if match:
    index = match.start()
    part1 = content[:index]
    part2 = content[index:]
    
    # In part1, find the last `}`
    last_brace = part1.rfind('}')
    
    # We will insert a comma and our new lines right after the last `}`
    new_part1 = part1[:last_brace+1] + ",\n" + "\n".join(new_lines) + "\n" + part1[last_brace+1:]
    
    content = new_part1 + part2
    with open("app.js", "w") as f:
        f.write(content)
    print("Success app.js")
else:
    print("Failed to find electronics array end")
