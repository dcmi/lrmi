from argparse import ArgumentParser

# defaults
mdFileName = ""

def parse_arguments():
    parser = ArgumentParser(
        prog="ttl2md.py",
        description="Turns a ttl (Turtl, terse triple language) file defining an LRMI concept scheme into the md (markdown) tables used on the website."
    )
    parser.add_argument("ttlFileName", type=str)
    parser.add_argument("mdFileName", type=str, nargs="?")
    return parser.parse_args()
