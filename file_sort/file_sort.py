def main():
    first_names_dict = read_file_into_dict("file1.txt")
    last_names_dict = read_file_into_dict("file2.txt")

    sorted_ids = sorted(first_names_dict.keys())

    with open("file_output.txt", "w") as f:
        for id in sorted_ids:
            entry = format_entry(first_names_dict, last_names_dict, id)
            f.write("{0}\n".format(entry))

def read_file_into_dict(filename):
    dict = {}
    with open(filename) as f:
        for entry in f:
            value, key = entry.split()
            dict[key] = value
    return dict

def format_entry(first_names_dict, last_names_dict, id):
    first_name = first_names_dict[id]
    last_name = last_names_dict[id]
    return "{0} {1} {2}".format(first_name, last_name, id)

if __name__ == '__main__':
    main()