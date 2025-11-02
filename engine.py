import chess.engine
import random
import os
class Engine():
    def play(self, board: chess.Board, cp_loss: int):
        if os.path.isfile("model.txt"):
            self.engine = chess.engine.SimpleEngine.popen_uci(["/opt/homebrew/bin/lc0", "--weights=model.txt"])
            moves = []
            for uci_move in board.legal_moves:
                board.push(uci_move)
                score = -self.engine.analyse(board, chess.engine.Limit(depth=1))['score'].relative
                if score.is_mate():
                    if "+" in str(score):
                        board.pop()
                        move = self.engine.play(board, chess.engine.Limit(depth=1)).move
                        self.engine.quit()
                        return move
                    elif "-" in str(score):
                        score = -100000
                else:
                    score = int(str(score))
                moves.append([score, uci_move])
                board.pop()
            self.engine.quit()
            best_moves = []
            high_score = max(moves)[0]
            for move in moves:
                if move[0]+cp_loss >= high_score:
                    best_moves.append(move[1])
            return random.choice(best_moves)
        else:
            return random.choice(list(board.legal_moves))