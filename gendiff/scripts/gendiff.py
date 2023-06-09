#!/usr/bin/env python3

"""A script that runs a main function in terminal."""

from gendiff.gendiff import generate_diff
import argparse


def main():
    """A function that creates description in terminal. """
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', type=str, default='stylish', help='set format of output')
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
