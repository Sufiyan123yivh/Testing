import requests

debug = open("debug.txt", "w")

url = "http://mini.allinonereborn.fun/zee-paid/index.php?id=0-9-zeebangla"
debug.write("Opening URL: " + url + "\n\n")

headers = {
    "User-Agent": "https://allinonereborn.online/zee/@allinone_reborn.php",
    "Accept": "*/*",
    "Connection": "keep-alive"
}

# Follow redirects normally
r = requests.get(url, allow_redirects=True, headers=headers)

debug.write("=== Redirect History ===\n")
for step in r.history:
    debug.write(f"{step.url} --> {step.status_code}\n")

debug.write("\n=== FINAL URL ===\n")
debug.write(r.url + "\n")

FINAL_URL = r.url

# Extract hdntl token
TOKEN = ""
if "?" in FINAL_URL:
    TOKEN = "?" + FINAL_URL.split("?", 1)[1]

debug.write("\n=== TOKEN EXTRACTED ===\n")
debug.write(TOKEN + "\n")

with open("token.txt", "w") as f:
    f.write(TOKEN)

# Escape for GitHub Actions
esc = TOKEN.replace("%", "%25").replace("\n", "%0A").replace("\r", "%0D")

print(f"token={esc}")
