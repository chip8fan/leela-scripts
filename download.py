import sys
import webbrowser
webbrowser.open(f"https://lichess.org/api/games/user/{sys.argv[1]}?rated=true&tags=true&clocks=false&evals=false&opening=false&literate=false&perfType=ultraBullet%2Cbullet%2Cblitz%2Crapid%2Cclassical%2Ccorrespondence%2Cstandard")