from datetime import datetime

# Get current date and time
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Write to version.md in the docs folder
with open("docs/version.md", "w") as f:
    f.write(now + "\n")

print("version.md updated successfully!")
