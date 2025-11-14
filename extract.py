import os
for file in os.listdir(os.getcwd() + "/zst"):
    if file.endswith(".zst"):
        os.system(f"python3 extract_month.py zst/{file}")