import engine
import chess
import os
if os.path.isfile("games.pgn"):
    os.remove("games.pgn")
generated_games = 0
while generated_games < 10**5:
    board = chess.Board()
    move_list = ""
    move_count = 1
    while board.is_game_over(claim_draw=True) == False:
        move = engine.Engine().play(board, 100)
        if board.turn == chess.WHITE:
            move_list = f"{move_list}{move_count}. {board.san(move)} "
        elif board.turn == chess.BLACK:
            move_list = f"{move_list}{board.san(move)} "
        board.push(move)
        if board.turn == chess.WHITE:
            move_count += 1
    move_list = f"{move_list}{board.result(claim_draw=True)}"
    print(move_list, file=open("games.pgn", "a"), end="\n\n")
    generated_games += 1
    print(generated_games)