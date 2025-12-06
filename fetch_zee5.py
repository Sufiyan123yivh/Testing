import requests

debug = open("debug.txt", "w")

url = "https://stream.kliv.fun/allplus5d/z5/index.php?id=0-9-255"
debug.write("Opening URL: " + url + "\n\n")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 ygx/69.1 Safari/537.36",
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
