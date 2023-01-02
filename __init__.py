import os
import sys

ADDON_FOLDER_PATH = os.path.dirname(__file__)
VERSION = (0, 1, 8)
MODULE_NAME = "earendill"
ADDON_NAME = (
    f"Earendill v{VERSION[0]}.{VERSION[1]}.{VERSION[2]}"
)

bl_info = {
    "name": "Earendill v0.1.8",
    "author": "Jilt",
    "version": (0, 1, 8),
    "blender": (2, 83, 0),
    "description": "A module to mint your Mintbase NFT from Blender.",
    "category": "Blockchain",
    "doc_url": "https://earendill.varda.vision",
}


def register():
    print(f'ENABLED "{ADDON_NAME}" addon')

    print(f"\tadding {MODULE_NAME} to sys path: {ADDON_FOLDER_PATH}")
    sys.path.append(ADDON_FOLDER_PATH)


def unregister():
    print(f'DISABLE "{ADDON_NAME}" addon')

    print(f"\tremoving {MODULE_NAME} from sys path: {ADDON_FOLDER_PATH}")
    sys.path.remove(ADDON_FOLDER_PATH)


if __name__ == "__main__":
    register()
