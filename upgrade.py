import os
import sys
os.system(f"curl -d '' http://localhost:8080/api/bot/account/upgrade -H \"Authorization: Bearer {sys.argv[1]}\"")