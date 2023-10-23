from PIL import Image as PILImage

class Image:
    def __init__(self, image: PILImage.Image):
        self.image = image

    def show(self) -> None:
        self.image.show()

    def save(self, filename: str) -> None:
        self.image.save(filename + '.png')

    def get_image(self) -> PILImage.Image:
        return self.image
