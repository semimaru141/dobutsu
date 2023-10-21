import tempfile
from typing import List
from PIL import Image as PILImage
from src.domains.shogi.visualizers.image import Image as MyImage

DURATION = 1000

class Gif():
    def __init__(self, images: List[MyImage]) -> None:
        self.images = images

    def show(self) -> None:
        images = self._get_pil_images()
        # 一時的なファイルを作成
        with tempfile.NamedTemporaryFile(suffix=".gif", delete=False) as temp:
            # 画像の配列からGIFを作成し、一時的なファイルに保存
            images[0].save(temp.name, save_all=True, append_images=images[1:], duration=DURATION, loop=0)
            # 一時的なGIFを表示
            with PILImage.open(temp.name) as img:
                img.show()

    def save(self, filename: str) -> None:
        images = self._get_pil_images()
        images[0].save(filename + '.gif', save_all=True, append_images=images[1:], duration=DURATION, loop=0)

    def _get_pil_images(self) -> List[PILImage.Image]:
        return [image.get_image() for image in self.images]