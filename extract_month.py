import os
import sys
file = open("match.txt", "w")
file.write('WhiteTitle <> "BOT"\n')
file.write('BlackTitle <> "BOT"\n')
file.close()
if sys.argv[1].endswith(".pgn.zst"):
    file_name = sys.argv[1].replace("lichess_db_standard_rated_", "").replace(".zst", "").split("/")[-1]
    if os.path.isfile(file_name) == False:
        os.system(f"pzstd -dc {sys.argv[1]} | pgn-extract -t match.txt --notags -C -N -V -s -o {file_name}")
elif sys.argv[1].endswith(".pgn"):
    file_name = f"{sys.argv[1].replace('lichess_', '').split('_')[0]}.pgn"
    if os.path.isfile(file_name):
        os.remove(file_name)
    os.system(f"pgn-extract -t match.txt -w2500 -C -N -V -s -o {file_name} {sys.argv[1]}")
else:
    raise Exception("Please specify a .pgn or .pgn.zst file!")
book_name = file_name.replace(".pgn", ".bin")
if sys.argv[1].endswith(".pgn") and os.path.isfile(book_name):
    os.remove(book_name)
#if os.path.isfile(book_name) == False and sys.argv[1].endswith(".pgn.zst"):
    #os.system(f"jja make --min-games 10 --output {book_name} {file_name}")
if sys.argv[1].endswith(".pgn"):
    root_directory = os.getcwd()
    training_directory = file_name.replace(".pgn", "")
    if os.path.isdir(training_directory) == False:
        os.system("unzip maia-individual-main.zip")
        os.system(f"mv maia-individual-main {training_directory}")
    if os.path.isdir(f"{root_directory}/players/{training_directory}") == False:
        os.chdir(f"{training_directory}/1-data_generation")
        os.system(f"./9-pgn_to_training_data.sh \"{root_directory}/{file_name}\" \"{root_directory}/players/{training_directory}\" {training_directory}")
    os.chdir(f"{root_directory}/{training_directory}/2-training")
    os.system(f"python3 train_transfer.py {root_directory}/{training_directory}.yml")