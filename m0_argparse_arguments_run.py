    #!/usr/bin/env python3
import argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("param")
    args = parser.parse_args()
    # Your code goes here!
    print(args.param)