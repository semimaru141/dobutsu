import math
from PIL import Image, ImageDraw, ImageFont
from src.domains.shogi.board import Board
from src.domains.shogi.captured import Captured, get_piece_num
from src.domains.shogi.const import *
from src.domains.shogi.shogi_state import ShogiState
from src.domains.shogi.visualizer import Visualizer
from src.domains.shogi.visualizers.image import Image as MyImage

# 盤面のサイズとセルのサイズを設定します
board_w_count = 3  # 盤面のサイズ（8x8）
board_h_count = 4
cell_size = 60  # セルのサイズ（ピクセル）
capture_size = 25
padding = 5     # セル間の空白スペースのサイズ（ピクセル）

class SimpleVisualizer(Visualizer):
    def __init__(self, state: ShogiState, should_turn: bool) -> None:
        if should_turn: self._state = state.turn()
        else: self._state = state

    @property
    def state(self) -> ShogiState:
        return self._state
    
    @property
    def board(self) -> Board:
        return self.state.board
    
    @property
    def captured(self) -> Captured:
        return self.state.captured
    
    def visualize(self) -> MyImage:
        # 盤面の画像を作成します
        cell_with_padding = cell_size + padding
        board_h_size = board_h_count * cell_size + padding * (board_h_count - 1)
        capture_h_size = capture_size + padding
        image_w_size = board_w_count * cell_size + padding * (board_w_count - 1)
        image_h_size = board_h_size + capture_h_size * 2
        image = Image.new("RGB", (image_w_size, image_h_size), "white")
        draw = ImageDraw.Draw(image)

        # 盤面の背景を描画します
        draw.rectangle([(0, 0), (image_w_size, capture_h_size)], fill="gray")
        draw.rectangle([(0, capture_h_size), (image_w_size, capture_h_size + board_h_size)], fill="gray")
        draw.rectangle([(0, board_h_size + capture_h_size), (image_w_size, image_h_size)], fill="gray")

        # 盤面のマス目を描画します
        for row in range(board_h_count):
            for col in range(board_w_count):
                x1 = col * cell_with_padding
                y1 = row * cell_with_padding
                x2 = x1 + cell_size
                y2 = y1 + cell_size
                draw.rectangle([(x1, y1 + capture_h_size), (x2, y2 + capture_h_size)], fill="lightgray")

        op_count = 0
        for i, count in enumerate(self.captured._captured[3:]):
            if count == 0: continue
            piece_image = self.get_image(get_piece_num(i)).resize((capture_size, capture_size))
            for _ in range(count):
                x = op_count * (capture_size + padding)
                image.paste(piece_image, (x, 0))
                op_count += 1

        for i, piece in enumerate(self.board._board):
            x = i % 3 * cell_with_padding
            y = math.floor(i / 3) * cell_with_padding
            if piece == EMPTY: continue
            piece_image = self.get_image(piece).resize((cell_size, cell_size))
            image.paste(piece_image, (x, y + capture_h_size))

        my_count = 0
        for i, count in enumerate(self.captured._captured[:3]):
            if count == 0: continue
            piece_image = self.get_image(get_piece_num(i)).resize((capture_size, capture_size))
            for _ in range(count):
                x = my_count * (capture_size + padding)
                image.paste(piece_image, (x, board_h_size + capture_h_size + padding))
                my_count += 1
        return MyImage(image)

    def get_image(self, piece):
        if piece == MY_LION_NUM:
            return self.make_image('L', False)
        elif piece == MY_ELE_NUM:
            return self.make_image('E', False)
        elif piece == MY_GIR_NUM:
            return self.make_image('G', False)
        elif piece == MY_CHICK_NUM:
            return self.make_image('C', False)
        elif piece == MY_HEN_NUM:
            return self.make_image('H', False)
        elif piece == OP_LION_NUM:
            return self.make_image('l', True)
        elif piece == OP_ELE_NUM:
            return self.make_image('e', True)
        elif piece == OP_GIR_NUM:
            return self.make_image('g', True)
        elif piece == OP_CHICK_NUM:
            return self.make_image('c', True)
        elif piece == OP_HEN_NUM:
            return self.make_image('h', True)
        raise 'piece not found'
    
    def make_image(self, text: str, rotate: bool):
        image = Image.new('RGB', (cell_size, cell_size), color="white")
        font = ImageFont.truetype("assets/NotoSansJP-Regular.ttf", 30)
        draw = ImageDraw.Draw(image)

        if rotate:
            draw.text((20, 0), text, font=font, fill="black")
        else:
            draw.text((20, 5), text, font=font, fill="black")

        if rotate:
            image = image.rotate(180)
        return image
