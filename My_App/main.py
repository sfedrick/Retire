import argparse


def main(numbers,target,helpful):
    if(helpful):
        print("hello")
    else:
        print(" i'm not so helpful")
    
    return numbers

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--list", nargs="+", type=int, help="a list of inputs input with spaces like : python3 main.py -n 1 2 3 4 ")
    parser.add_argument("-t", "--single_int",type=int, help="A single integer like : python3 main.py -t ")
    parser.add_argument("-q", "--helpful", action="store_true", help="A single boolean like : python3 main.py -q true ")
    args = parser.parse_args()
    main(args.list,args.single_int,args.helpful)
