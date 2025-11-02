import chess.pgn
import chess.engine
import sys
with open(sys.argv[1]) as pgn:
    while True:
        game = chess.pgn.read_game(pgn)
        if game is None:
            break
        board = game.board()
        engine = chess.engine.SimpleEngine.popen_uci(["/opt/homebrew/bin/lc0", "--weights=/Volumes/Lichess/maia-chess/move_prediction/model_files/1900/final_1900-40.pb.gz"])
        correct_guesses = 0
        moves = 0
        if game.headers['White'] == sys.argv[2]:
            color = 'white'
        elif game.headers['Black'] == sys.argv[2]:
            color = 'black'
        for move in game.mainline_moves():
            if color == 'white':
                if board.turn == chess.WHITE:
                    moves += 1
                    engine_move = engine.play(board, chess.engine.Limit(depth=1)).move
                    if engine_move == move:
                        correct_guesses += 1
                    else:
                        print(f"Engine played {engine_move}, actual move was {move}")
            elif color == 'black':
                if board.turn == chess.BLACK:
                    moves += 1
                    engine_move = engine.play(board, chess.engine.Limit(depth=1)).move
                    if engine_move == move:
                        correct_guesses += 1
                    else:
                        print(f"Engine played {engine_move}, actual move was {move}")
            board.push(move)
        engine.quit()
        print(f"{correct_guesses}/{moves}")