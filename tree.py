import os
import argparse
import sys, traceback
import unittest

#Generator function to yeild depth and path of file
def files(path, depth, max_depth):    
    for f in os.scandir(path):
        # print(str(depth) + f.name)
        yield(depth, f)

        if f.is_dir() and depth < max_depth:
            yield from files (f.path, depth + 1, max_depth)

# Main Function to call the collect yield values and print
def main(path, max_depth):
    for depth, f in files(path, 0, max_depth):
        
        start = "├─" if depth == 0 else "|"
        padding = " " * 2 * depth
        tail = "─" if depth == 0 else "└─"
        
        print(f"{start}{padding}{tail}{f.name}")

def test_this_folder():
    expectedResult = [
        (0,'test1'),
        (1, 'test2'),
        (1, 'testfile2.txt'),
        (0, 'tree.py'),
        (0, '__pycache__'),
        (1, 'tree.cpython-37.pyc')
    ]
    actualResult = [(depth, file.name) for (depth, file) in files(".", 0, 1)]  
    test = 1
    print("----------------")
    print("Executing Test Case")
    assert 1 == test
    assert sorted(expectedResult) == sorted(actualResult)       
    print("TEST CASE PASSED ! ")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="tree")
    
    try:
        parser.add_argument("-p","--path", default=".", type=str)
        parser.add_argument("-d", "--depth", default=1, type=int)
    
    except TypeError:
        print("Invalid entry. If you are using arguments for PATH or DEPTH, please make sure the path is added in double quotes, and depth is a")
        exit(0)
    
    args = parser.parse_args()    
    
    if not os.path.exists(args.path):
        print ("Invalid Path !")
        exit (0)

    print (f"-------\nTree for: \nPath: { os.path.abspath(__file__) if args.path == '.' else args.path }\nDepth: {args.depth}")
    main(args.path, args.depth)

