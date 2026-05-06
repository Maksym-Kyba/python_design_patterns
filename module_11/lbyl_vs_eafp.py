import os


def test_open_file(filename):
    if os.path.exists(filename):
        with open(filename) as f:
            print(f.text)
    else:
        print("No file there")

#This is LBYL, and when new to Python
#You would think that it is the right way to treat such situations.
#But in Python, it is recommended to favor EAFP, where appropriate
#For cleaner, more Pythonic code. 
#The recommended way for the expected result would give the following code:

def better_test_open_file(filename):
    try:
        with open(filename) as f:
            print(f.text)
    except FileNotFoundError:
        print("No file there")


if __name__ == "__main__":
    filename = "no_file.txt"
    test_open_file(filename)
    better_test_open_file(filename)
