import chess.engine
import os
class Engine():
    def pull_latest_weights(self, player_name):
        files = []
        for file in os.listdir(f"{os.getcwd()}/{player_name}/2-training/models/final_config/"):
            if file.endswith(".pb.gz"):
                files.append([int(file.split("-")[-1].split(".pb.gz")[0]), file])
        files = sorted(files, reverse=True)[0][1]
        return files
    def play(self, board: chess.Board, player_name: str):
        self.engine = chess.engine.SimpleEngine.popen_uci(["/opt/homebrew/bin/lc0", f"--weights={os.getcwd()}/{player_name}/2-training/models/final_config/{self.pull_latest_weights(player_name)}"])
        self.move = self.engine.play(board, chess.engine.Limit(depth=4)).move
        self.engine.quit()
        return self.move