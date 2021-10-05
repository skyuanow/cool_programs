import os
from pathlib import Path

from PIL import Image
from tqdm import tqdm


def create_path(p):
    if not Path.exists(Path(p)):
        Path.mkdir(Path(p), exist_ok=True, parents=True)
    return p


def merge_images(file1, file2, filepath, filename):
    """Merge two images into one, displayed side by side
    :param file1: path to first image file
    :param file2: path to second image file
    :return: the merged Image object
    """
    image1 = Image.open(file1)
    image2 = Image.open(file2)

    (width1, height1) = image1.size
    (width2, height2) = image2.size

    result_width = width1 + width2
    result_height = max(height1, height2)

    result = Image.new('RGB', (result_width, result_height))
    result.paste(im=image1, box=(0, 0))
    result.paste(im=image2, box=(width1, (result_height - height2) // 2))

    p = create_path(f'comparisons\\{filepath}')
    result.save(p + f'\\{filename}')

if __name__ == '__main__':
    merge_images('image1.jpg', 'image2.jpg')
