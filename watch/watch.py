import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if youtube_url := re.search(r"src=\"https?\:\/\/(?:www\.)?(youtu)(be)\.com\/embed(\/\w{11})", s):
        return (f"https://{youtube_url.group(1)}.{youtube_url.group(2)}{youtube_url.group(3)}")


if __name__ == "__main__":
    main()