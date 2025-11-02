import os
import sys
file = open("match.txt", "w")
file.write('WhiteTitle <> "BOT"\n')
file.write('BlackTitle <> "BOT"\n')
file.write('WhiteElo >= "2200"\n')
file.write('BlackElo >= "2200"\n')
file.close()
file_name = sys.argv[1].replace("lichess_db_standard_rated_", "").replace(".zst", "").split("/")[-1]
book_name = file_name.replace(".pgn", ".bin")
if os.path.isfile(file_name) == False:
    os.system(f"pzstd -dc {sys.argv[1]} | pgn-extract -t match.txt --notags -C -N -V -o {file_name}")
if os.path.isfile(book_name) == False:
    os.system(f"jja make --min-games 10 --output {book_name} {file_name}")
if os.path.isdir("supervised-0") == False:
    os.system(f"trainingdata-tool {file_name}")