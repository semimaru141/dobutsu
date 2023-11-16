from typing import List, Tuple
from src.consts.domain import *
from src.domains.shogi.const import *


class Captured:
    def __init__(self, captured: List[int]):
        self._captured = captured

    @staticmethod
    def create_initial() -> 'Captured':
        return Captured(INITIAL_CAPTURED)

    def copy(self) -> 'Captured':
        return Captured(self._captured.copy())
    
    # 所持している駒の個数を返す
    def get_count_by_index(self, index: CapturedIndex):
        return self._captured[index]

    # Pieceを取得する。該当のPieceの個数を増やす
    def take_piece(self, piece: Piece):
        if(piece == OP_LION_NUM): return
        index = parse_piece(piece)
        self._captured[index] += 1

    # Pieceを使用する。該当するPieceの個数を減らす 
    def use_piece(self, piece: Piece):
        index = parse_piece(piece)
        self._captured[index] -= 1
    
    # 先手が使用可能なPieceを取得する
    def get_my_pieces(self) -> List[Piece]:
        return [get_piece_num(capturedIndex) for capturedIndex in range(3) if self._captured[capturedIndex] != 0]
    
    # 先手後手を入れ替える
    def turn(self):
        new_captured = list(range(RANGE_OF_CAPTURED))
        for index in range(RANGE_OF_CAPTURED):
            new_captured[turn_index(index)] = self._captured[index]
        return Captured(new_captured)
    
    def get_unique_key(self) -> str:
        # 現在のcapturedに一意なkeyを返す
        return ''.join(map(str, self._captured))
    
    # 先手・後手に関わらず0でないpiece・indexを取得する
    def get_nonzero_set(self) -> List[Tuple[Piece, CapturedIndex]]:
        return [(get_piece_num(captured_index), captured_index) for captured_index in range(RANGE_OF_CAPTURED) if self._captured[captured_index] != 0]

    # 強制的に駒を使用する
    def use_index_unsafe(self, index: CapturedIndex):
        self._captured[index] -= 1
    
    # 強制的に駒を持ち駒に入れる
    def take_piece_unsafe(self, piece: Piece, player: Player):
        if(piece == MY_LION_NUM or piece == OP_LION_NUM): return
        if player == Player.ME:
            index = parse_piece(piece)
            self._captured[index] += 1
        if player == Player.OP:
            index = turn_index(parse_piece(piece))
            self._captured[index] += 1

# 駒を与えると、自分の駒のインデックスを返す
# 駒取得時・駒使用時の双方から使用される
piece_to_cap_index_dic = {
    MY_ELE_NUM: MY_ELE_INDEX,
    MY_GIR_NUM: MY_GIR_INDEX,
    MY_CHICK_NUM: MY_CHICK_INDEX,
    MY_HEN_NUM: MY_CHICK_INDEX,
    OP_ELE_NUM: MY_ELE_INDEX,
    OP_GIR_NUM: MY_GIR_INDEX,
    OP_CHICK_NUM: MY_CHICK_INDEX,
    OP_HEN_NUM: MY_CHICK_INDEX
}

def parse_piece(piece: Piece) -> CapturedIndex:
    return piece_to_cap_index_dic[piece]

# 持ち駒のインデックスから打った後のPieceを返す
cap_index_to_piece_dic = {
    MY_ELE_INDEX: MY_ELE_NUM,
    MY_GIR_INDEX: MY_GIR_NUM,
    MY_CHICK_INDEX: MY_CHICK_NUM,
    OP_ELE_INDEX: OP_ELE_NUM,
    OP_GIR_INDEX: OP_GIR_NUM,
    OP_CHICK_INDEX: OP_CHICK_NUM
}

def get_piece_num(index: CapturedIndex) -> Piece:
    return cap_index_to_piece_dic[index]

# 版を回転させた後の番号を取得する
turn_index_dic = {
    MY_ELE_INDEX: OP_ELE_INDEX,
    MY_GIR_INDEX: OP_GIR_INDEX,
    MY_CHICK_INDEX: OP_CHICK_INDEX,
    OP_ELE_INDEX: MY_ELE_INDEX,
    OP_GIR_INDEX: MY_GIR_INDEX,
    OP_CHICK_INDEX: MY_CHICK_INDEX
}

def turn_index(index: CapturedIndex) -> CapturedIndex:
    return turn_index_dic[index]
