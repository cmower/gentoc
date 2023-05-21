import sys
from dataclasses import dataclass

"""

Generate table of contents from README.md.

Usage

$ python gentoc /path/to/README.md

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
        return f"[{self.title()}](#{title})"

    def toc_line(self):
        n = self.level() - 1
        return " " * (n * 2) + "* " + self.link()


def main():
    print("# Table of contents\n")

    with open(sys.argv[1], "r") as f:
        for line in f.readlines():
            if line.startswith("#"):
                print(Header(line).toc_line())


if __name__ == "__main__":
    main()
