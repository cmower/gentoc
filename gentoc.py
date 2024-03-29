import sys
from dataclasses import dataclass

"""

Generate table of contents from README.md.

Usage

$ python gentoc.py /path/to/README.md

Copy, paste the output to your README.md file.

"""


@dataclass
class Header:
    line: str

    def level(self):
        return len(self.line.split(" ")[0])

    def title(self):
        return " ".join(self.line.split(" ")[1:]).rstrip()

    def link(self):
        title = self.title().lower().replace(" ", "-").replace(",", "").replace(".", "")
        return f"[{self.title()}](#{title.replace('+', '')})"

    def toc_line(self):
        n = self.level() - 1
        return " " * (n * 2) + "* " + self.link()


def main():
    print("# Table of contents\n")

    in_code = False

    with open(sys.argv[1], "r") as f:
        for line in f.readlines():
            if line.startswith("```") and not in_code:
                in_code = True
                continue

            if line.startswith("```") and in_code:
                in_code = False
                continue

            if in_code:
                continue

            if line.startswith("#"):
                print(Header(line).toc_line())


if __name__ == "__main__":
    main()
