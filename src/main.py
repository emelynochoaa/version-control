from datetime import datetime 

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("docs/version.md", "w") as f:
    f.write(now + "\n")
