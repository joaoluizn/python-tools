import argparse
import re

def abbreviate(words: str) -> str:
    """
    :param str sentence: Given sentence to abbreviate
    :rtype: bool
    """
    pre = re.sub('[^A-Za-z ]', '', words.replace('-', ' '))
    return re.sub('[^A-Z]', '', pre.lower().title())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--text",'-t', help="A text to be converted to its acronym.")
    args = parser.parse_args()

    if args.text:
        print(f'Your acronym is: {abbreviate(args.text)}')
    else:
        parser.print_help()
