import os

# Resolve the home directory
home_dir = os.path.expanduser("~")
file_path = os.path.join(home_dir, "example.txt")
content = "This is the first line in the file.\n"

# Create and write only if the file doesn't exist
if not os.path.exists(file_path):
    with open(file_path, "w") as f:
        f.write(content)
    print(f"File '{file_path}' created and content written.")
else:
    print(f"File '{file_path}' already exists. No action taken.")
