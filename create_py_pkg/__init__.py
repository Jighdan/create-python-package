import argparse

parser = argparse.ArgumentParser(description="Create Python simple package file structure")
parser.add_argument("-n", "--name", type=str, help="Package name", required=True)

args = parser.parse_args()
