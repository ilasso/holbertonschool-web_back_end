import asyncio
import glob
import os

from PIL import Image  # fades Pillow


def convert_image(filename):
    base, _ = os.path.splitext(filename)
    newname = base + ".jpg"
    Image.open(filename).save(newname)


async def main():
    for fname in glob.glob("*.png"):
        await loop.run_in_executor(None, convert_image, fname)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
