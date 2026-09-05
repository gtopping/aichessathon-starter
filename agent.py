import math
import time
import random
import chess

MG_PST = {
    chess.PAWN: [
          0,   0,   0,   0,   0,   0,   0,   0,
        -35,  -1, -20, -23, -15,  24,  38, -22,
        -26,  -4,  -4, -10,   3,   3,  33, -12,
        -27,  -2,  -5,  12,  17,   6,  10, -25,
        -14,  13,   6,  21,  23,  12,  17, -23,
         -6,   7,  26,  31,  65,  56,  25, -20,
         98, 134,  61,  95,  68, 126,  34, -11,
          0,   0,   0,   0,   0,   0,   0,   0,
    ],

    chess.KNIGHT: [
        -105, -21, -58, -33, -17, -28, -19, -23,
         -29, -53, -12,  -3,  -1,  18, -14, -19,
         -23,  -9,  12,  10,  19,  17,  25, -16,
         -13,   4,  16,  13,  28,  19,  21,  -8,
          -9,  17,  19,  53,  37,  69,  18,  22,
         -47,  60,  37,  65,  84, 129,  73,  44,
         -73, -41,  72,  36,  23,  62,   7, -17,
        -167, -89, -34, -49,  61, -97, -15, -107,
    ],

    chess.BISHOP: [
        -33,  -3, -14, -21, -13, -12, -39, -21,
          4,  15,  16,   0,   7,  21,  33,   1,
          0,  15,  15,  15,  14,  27,  18,  10,
         -6,  13,  13,  26,  34,  12,  10,   4,
         -4,   5,  19,  50,  37,  37,   7,  -2,
        -16,  37,  43,  40,  35,  50,  37,  -2,
        -26,  16, -18, -13,  30,  59,  18, -47,
        -29,   4, -82, -37, -25, -42,   7,  -8,
    ],

    chess.ROOK: [
        -19, -13,   1,  17,  16,   7, -37, -26,
        -44, -16, -20,  -9,  -1,  11,  -6, -71,
        -45, -25, -16, -17,   3,   0,  -5, -33,
        -36, -26, -12,  -1,   9,  -7,   6, -23,
        -24, -11,   7,  26,  24,  35,  -8, -20,
         -5,  19,  26,  36,  17,  45,  61,  16,
         27,  32,  58,  62,  80,  67,  26,  44,
         32,  42,  32,  51,  63,   9,  31,  43,
    ],

    chess.QUEEN: [
         -1, -18,  -9,  10, -15, -25, -31, -50,
        -35,  -8,  11,   2,   8,  15,  -3,   1,
        -14,   2, -11,  -2,  -5,   2,  14,   5,
         -9, -26,  -9, -10,  -2,  -4,   3,  -3,
        -27, -27, -16, -16,  -1,  17,  -2,   1,
        -13, -17,   7,   8,  29,  56,  47,  57,
        -24, -39,  -5,   1, -16,  57,  28,  54,
        -28,   0,  29,  12,  59,  44,  43,  45,
    ],

    chess.KING: [
        -15,  36,  12, -54,   8, -28,  24,  14,
          1,   7,  -8, -64, -43, -16,   9,   8,
        -14, -14, -22, -46, -44, -30, -15, -27,
        -49,  -1, -27, -39, -46, -44, -33, -51,
        -17, -20, -12, -27, -30, -25, -14, -36,
         -9,  24,   2, -16, -20,   6,  22, -22,
         29,  -1, -20,  -7,  -8,  -4, -38, -29,
        -65,  23,  16, -15, -56, -34,   2,  13,
    ],
}


EG_PST = {
    chess.PAWN: [
          0,   0,   0,   0,   0,   0,   0,   0,
         13,   8,   8,  10,  13,   0,   2,  -7,
          4,   7,  -6,   1,    0,  -5,  -1,  -8,
         13,   9,  -3,  -7,  -7,  -8,   3,  -1,
         32,  24,  13,   5,   -2,   4,  17,  17,
         94, 100,  85,  67,   56,  53,  82,  84,
        178, 173, 158, 134,  147, 132, 165, 187,
          0,   0,   0,   0,    0,   0,   0,   0,
    ],

    chess.KNIGHT: [
         -29, -51, -23, -15, -22, -18, -50, -64,
         -42, -20, -10,  -5,  -2, -20, -23, -44,
         -23,  -3,  -1,  15,  10,  -3, -20, -22,
         -18,  -6,  16,  25,  16,  17,   4, -18,
         -17,   3,  22,  22,  22,  11,   8, -18,
         -24, -20,  10,   9,  -1,  -9, -19, -41,
         -25,  -8, -25,  -2,  -9, -25, -24, -52,
         -58, -38, -13, -28, -31, -27, -63, -99,
    ],

    chess.BISHOP: [
         -23,  -9, -23,  -5,  -9, -16,  -5, -17,
         -14, -18,  -7,  -1,   4,  -9, -15, -27,
         -12,  -3,   8,  10,  13,   3,  -7, -15,
          -6,   3,  13,  19,   7,  10,  -3,  -9,
          -3,   9,  12,   9,  14,  10,   3,   2,
           2,  -8,   0,  -1,  -2,   6,   0,   4,
          -8,  -4,   7, -12,  -3, -13,  -4, -14,
         -14, -21, -11,  -8,  -7,  -9, -17, -24,
    ],

    chess.ROOK: [
          -9,   2,   3,  -1,  -5, -13,   4, -20,
          -6,  -6,   0,   2,  -9,  -9, -11,  -3,
          -4,   0,  -5,  -1,  -7, -12,  -8, -16,
           3,   5,   8,   4,  -5,  -6,  -8, -11,
           4,   3,  13,   1,   2,   1,  -1,   2,
           7,   7,   7,   5,   4,  -3,  -5,  -3,
          11,  13,  13,  11,  -3,   3,   8,   3,
          13,  10,  18,  15,  12,  12,   8,   5,
    ],

    chess.QUEEN: [
         -33, -28, -22, -43,  -5, -32, -20, -41,
         -22, -23, -30, -16, -16, -23, -36, -32,
         -16, -27,  15,   6,   9,  17,  10,   5,
         -18,  28,  19,  47,  31,  34,  39,  23,
           3,  22,  24,  45,  57,  40,  57,  36,
         -20,   6,   9,  49,  47,  35,  19,   9,
         -17,  20,  32,  41,  58,  25,  30,   0,
          -9,  22,  22,  27,  27,  19,  10,  20,
    ],

    chess.KING: [
         -53, -34, -21, -11, -28, -14, -24, -43,
         -27, -11,   4,  13,  14,   4,  -5, -17,
         -19,  -3,  11,  21,  23,  16,   7,  -9,
         -18,  -4,  21,  24,  27,  23,   9, -11,
          -8,  22,  24,  27,  26,  33,  26,   3,
          10,  17,  23,  15,  20,  45,  44,  13,
         -12,  17,  14,  17,  17,  38,  23,  11,
         -74, -35, -18, -18, -11,  15,   4, -17,
    ],
}


MG_PIECE_VALUE = {
    chess.PAWN: 82,
    chess.KNIGHT: 337,
    chess.BISHOP: 365,
    chess.ROOK: 477,
    chess.QUEEN: 1025,
    chess.KING: 0,
}

EG_PIECE_VALUE = {
    chess.PAWN: 94,
    chess.KNIGHT: 281,
    chess.BISHOP: 297,
    chess.ROOK: 512,
    chess.QUEEN: 936,
    chess.KING: 0,
}

PIECES = [
    chess.PAWN,
    chess.KNIGHT,
    chess.BISHOP,
    chess.ROOK,
    chess.QUEEN,
    chess.KING
]

PIECE_PHASE_WEIGHTINGS = {
    chess.PAWN: 0, 
    chess.KNIGHT: 1, 
    chess.BISHOP: 1, 
    chess.ROOK: 2, 
    chess.QUEEN: 4,
    chess.KING: 0
}

MOBILITY_WEIGHT = 4.0
MATE = 1_000_000

EXACT = 0
LOWERBOUND = 1
UPPERBOUND = 2

class SearchTimeout(Exception):
    pass

class Engine:
    def __init__(self):
        self.nodes = 0
        self.deadline = 0.0
        self.positions = {}
        self.tt = {}

        rng = random.Random(12345)
        self.zobrist = {
            (piece, square, colour): rng.getrandbits(64)
            for piece in range(1, 7) 
            for square in range(64) 
            for colour in [chess.WHITE, chess.BLACK]
        }
        self.zobrist_turn = rng.getrandbits(64)
        self.zobrist_castling = [rng.getrandbits(64) for _ in range(16)]
        self.zobrist_ep = [rng.getrandbits(64) for _ in range(8)]

    def zobrist_hash(self, board):
        h = 0
        for square, piece in board.piece_map().items():
            h ^= self.zobrist[(piece.piece_type, square, piece.color)]
        if board.turn == chess.BLACK:
            h ^= self.zobrist_turn
        castling = 0
        if board.has_kingside_castling_rights(chess.WHITE):
            castling |= 1
        if board.has_queenside_castling_rights(chess.WHITE):
            castling |= 2
        if board.has_kingside_castling_rights(chess.BLACK):
            castling |= 4
        if board.has_queenside_castling_rights(chess.BLACK):
            castling |= 8
        h ^= self.zobrist_castling[castling]
        if board.ep_square is not None:
            h ^= self.zobrist_ep[chess.square_file(board.ep_square)]
        return h

    def check_time(self):
        if time.perf_counter() >= self.deadline:
            raise SearchTimeout

    def phase(self, board):
        total_phase = sum(
            value * (len(board.pieces(piece, 0)) + len(board.pieces(piece, 1))) 
            for piece, value in PIECE_PHASE_WEIGHTINGS.items()
        )
        return min(total_phase / 24, 1) # 1 middlegame and 0 endgame

    def piece_value(self, piece, square, colour, phase):
        if colour == chess.WHITE:
            sq = square
        else:
            sq = chess.square_mirror(square)
        return ((MG_PIECE_VALUE[piece] + MG_PST[piece][sq]) * phase) + ((EG_PIECE_VALUE[piece] + EG_PST[piece][sq]) * (1 - phase))

    def evaluate(self, board, phase=None, legal_move_count=None):
        colour = board.turn
        if phase is None:
            phase = self.phase(board)
        material = 0
        for piece in PIECES:
            for square in board.pieces(piece, colour):
                material += self.piece_value(piece, square, colour, phase)
            for square in board.pieces(piece, not colour):
                material -= self.piece_value(piece, square, not colour, phase)
        if legal_move_count is None:
            legal_move_count = board.legal_moves.count()
        return material + MOBILITY_WEIGHT * legal_move_count

    def move_score(self, board, move, phase):
        score = 0
        if move.promotion:
            score += 1_000_000
        if board.is_capture(move):
            score += 900_000
            if board.is_en_passant(move):
                victim = chess.PAWN
            else:
                victim = board.piece_at(move.to_square).piece_type
            attacker = board.piece_at(move.from_square).piece_type
            score += ((10 * self.piece_value(victim, move.to_square, not board.turn, phase)) - self.piece_value(attacker, move.from_square, board.turn, phase))
        if board.gives_check(move):
            score += 800_000
        return score

    def move_order(self, board, phase=None, moves=None):
        if phase is None:
            phase = self.phase(board)
        if moves is None:
            moves = board.legal_moves
        return sorted(moves, key = lambda move: self.move_score(board, move, phase), reverse = True)

    def quiescence(self, board, depth, alpha, beta, old_depth):
        self.nodes += 1
        if self.nodes % 100 == 0:
            self.check_time()
        if board.is_checkmate():
            return -MATE
        if board.is_stalemate() or board.is_insufficient_material():
            return 0
        phase = self.phase(board)
        if depth == 0:
            return self.evaluate(board, phase)
        moves = list(board.legal_moves)
        in_check = board.is_check()
        if not in_check:
            value = self.evaluate(board, phase, len(moves))
            if value >= beta:
                return beta
            alpha = max(value, alpha)
        else:
            value = -math.inf
        for move in self.move_order(board, phase, moves):
            if in_check or board.is_capture(move) or move.promotion:
                board.push(move)
                value = max(value, -self.quiescence(board, depth - 1, -beta, -alpha, old_depth))
                board.pop()
                if value >= beta:
                    return beta
                alpha = max(value, alpha)
        return alpha

    def search(self, board, depth, alpha, beta):
        self.nodes += 1
        if self.nodes % 100 == 0:
            self.check_time()
        if board.is_checkmate():
            return -MATE
        if board.is_stalemate() or board.is_insufficient_material():
            return 0
        original_alpha = alpha
        original_beta = beta
        key = self.zobrist_hash(board)
        entry = self.tt.get(key)
        tt_move = None
        if entry is not None:
            tt_depth, tt_score, tt_flag, tt_move = entry
            if tt_depth >= depth:
                if tt_flag == EXACT:
                    return tt_score
                elif tt_flag == LOWERBOUND:
                    alpha = max(alpha, tt_score)
                elif tt_flag == UPPERBOUND:
                    beta = min(beta, tt_score)
                if alpha >= beta:
                    return tt_score
        if depth == 0:
            return self.quiescence(board, 3, alpha, beta, depth)
        value = -math.inf
        best_move = None
        phase = self.phase(board)
        moves = self.move_order(board, phase)
        if tt_move is not None and tt_move in moves:
            moves.remove(tt_move)
            moves.insert(0, tt_move)
        for move in moves:
            board.push(move)
            score = -self.search(board, depth - 1, -beta, -alpha)
            board.pop()
            if score > value:
                value = score
                best_move = move
            alpha = max(value, alpha)
            if alpha >= beta:
                break
        if value <= original_alpha:
            flag = UPPERBOUND
        elif value >= original_beta:
            flag = LOWERBOUND
        else:
            flag = EXACT
        self.tt[key] = (depth, value, flag, best_move)
        return value
        
    def root_node_search(self, board, time_left_ms):
        time_left = time_left_ms / 1000
        move_time = time_left / 20
        safety_margin = 0.15
        self.nodes = 0
        overall_best = self.move_order(board)[0]
        if time_left <= safety_margin + 0.05:
            return overall_best
        self.deadline = time.perf_counter() + move_time - safety_margin
        try:
            for depth in range(1, 100):
                iteration_best = None
                best_score = -math.inf
                alpha = -math.inf
                beta = math.inf
                for move in self.move_order(board):
                    board.push(move)
                    score = -self.search(board, depth, -beta, -alpha)
                    board.pop()
                    if score > best_score:
                        best_score = score
                        iteration_best = move
                    alpha = max(alpha, score)
                overall_best = iteration_best
        except SearchTimeout:
            pass
        return overall_best


ENGINE = Engine()

def get_move(fen: str, time_left_ms: int) -> str:
    board = chess.Board(fen)
    move = ENGINE.root_node_search(board, time_left_ms)
    return move.uci()
