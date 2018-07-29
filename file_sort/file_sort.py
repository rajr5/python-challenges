import os

def main():
    first_names_dict = read_file_into_dict("input1.txt")
    last_names_dict = read_file_into_dict("input2.txt")

    ids = first_names_dict.keys()
    sorted_ids = sorted(ids, key=lambda x: int(x))

    output_file_path = _get_absolute_file_path("output.txt")
    with open(output_file_path, "w") as f:
        for id in sorted_ids:
            entry = format_entry(first_names_dict, last_names_dict, id)
            f.write("{0}\n".format(entry))

def read_file_into_dict(filename):
    file_path = _get_absolute_file_path(filename)
    dict = {}

    with open(file_path) as f:
        for entry in f:
            value, key = entry.split()
            dict[key] = value
    return dict

def format_entry(first_names_dict, last_names_dict, id):
    first_name = first_names_dict[id]
    last_name = last_names_dict[id]
    return "{0} {1} {2}".format(first_name, last_name, id)

def _get_absolute_file_path(file_name):
    script_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(script_path, file_name)

if __name__ == '__main__':
    main()