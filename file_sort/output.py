def main():
    with open("input1.txt", "w") as file:
        for x in range(100000000):
            file.write("a{0} {0}\n".format(x))

    with open("input2.txt", "w") as file:
        for x in range(100000000):
            file.write("b{0} {0}\n".format(x))

if __name__ == '__main__':
    main()