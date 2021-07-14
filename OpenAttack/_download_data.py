"""
"""
import os, sys, argparse
from typing import NoReturn

# overrides the package install via pip
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from OpenAttack.data import data_list


def run(dst_dir:str) -> NoReturn:
    """
    """
    for item in data_list:
        if item["url"] == "":
            continue
        print(item["name"].lower().replace(".", "_"))
        print(item["url"])
        dst_path = os.path.join(dst_dir, item["name"].lower().replace(".", "_"))
        os.makedirs(dst_path, exist_ok=True)
        item["download"](dst_path)


def get_parser() -> dict:
    """
    """
    description = "download options"
    parser = argparse.ArgumentParser(
        description=description,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-d", "--dst-dir", type=str,
        help="destination directory for the data to download",
        dest="dst_dir",
    )

    args = vars(parser.parse_args())

    return args


if __name__ == "__main__":
    args = get_parser()
    print(f"args = {args}")
    run(args.get("dst_dir"))
