import sys
import webbrowser
sys.argv.pop(0)
for user in sys.argv:
    webbrowser.open(f"https://lichess.org/api/games/user/{user}?rated=true&tags=true&clocks=false&evals=false&opening=false&literate=false&perfType=blitz%2Crapid%2Cclassical%2Ccorrespondence%2Cstandard")