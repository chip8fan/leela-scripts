import chess.engine
import os
class Engine():
    def pull_latest_weights(self):
        files = []
        for file in os.listdir(os.getcwd() + "/maia-individual/2-training/models/final_config/"):
            if file.endswith(".pb.gz"):
                files.append([int(file.split("-")[-1].split(".pb.gz")[0]), file])
        files = sorted(files, reverse=True)[0][1]
        return files
    def play(self, board: chess.Board):
        self.engine = chess.engine.SimpleEngine.popen_uci(["/opt/homebrew/bin/lc0", f"--weights={os.getcwd()}/maia-individual/2-training/models/final_config/{self.pull_latest_weights()}"])
        self.move = self.engine.play(board, chess.engine.Limit(depth=4)).move
        self.engine.quit()
        return self.move