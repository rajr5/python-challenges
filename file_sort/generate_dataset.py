import random
import os

def main():
    dataset_size = 100_000_000
    ids = []

    for x in range(1, dataset_size + 1):
        ids.append(x)

    script_path = os.path.dirname(os.path.realpath(__file__))

    random.shuffle(ids)
    input_1_path = os.path.join(script_path, "input1.txt")

    with open(input_1_path, "w") as file:
        for x in ids:
            file.write("a{0} {0}\n".format(x))

    random.shuffle(ids)
    input_2_path = os.path.join(script_path, "input2.txt")

    with open(input_2_path, "w") as file:
        for x in ids:
            file.write("b{0} {0}\n".format(x))

if __name__ == '__main__':
    main()