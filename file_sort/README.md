# File Sort

There are 2 solutions, `file_sort.py`, a faster, naive approach, and `file_sort_sql.py`, a low memory footprint approach, and a helper `generate_dataset.py` script. The script helps us generate test data.

## Problem

Input data is contained in two disk files. Both files contain multiple entries separated by a
newline character. The first file is of the following form:

```
<first name> <ID number>
```

The other file contains entries of the following format:

```
<last name> <ID number>
```

Write a program that, based on the information contained in input files, creates an output file
with the format:

```
<first name> <last name> <ID number>
```

**Example input:**

```
Adam 1234
John 4321

Anderson 4321
Smith 1234
```

**Expected output:**

```
Adam Smith 1234
John Anderson 4321
```

**Extension #1:** sort output entries by the ID number

**Extension #2:** input data is too big to fit into main memory

## Approach to the problem

### Naive approach

Both of the files are read into a dictionary to speed up access times, then their IDs are sorted, after that each entry is saved to a file one by one with corresponding first/last name combinations.

The solution found in `file_sort.py` takes care of the basic problem and extension #1 of the problem. Trying this approach on extension #2 of the problem would fail as shown by the profiler info on a 160 MB file (10.000.000 entries):

```
Line #    Mem usage    Increment   Line Contents
================================================
     3   10.863 MiB   10.863 MiB   @profile
     4                             def main():
     5 1076.188 MiB 1065.324 MiB       first_names_dict = read_file_into_dict("input1.txt")
     6  918.445 MiB -157.742 MiB       last_names_dict = read_file_into_dict("input2.txt")
     7
     8  918.449 MiB    0.004 MiB       ids = first_names_dict.keys()
     9 1369.301 MiB -5783893058.562 MiB       sorted_ids = sorted(ids, key=lambda x: int(x))
    10
    11  646.387 MiB -722.914 MiB       output_file_path = _get_absolute_file_path("output.txt")
    12  646.789 MiB    0.402 MiB       with open(output_file_path, "w") as f:
    13 2931.164 MiB -330409372.199 MiB           for id in sorted_ids:
    14 2931.164 MiB -330407423.020 MiB               entry = format_entry(first_names_dict, last_names_dict, id)
    15 2931.164 MiB -330410031.000 MiB               f.write("{0}\n".format(entry))
```

### Memory aware approach

Extension #2 takes the complexity problem to the next level, we have a few approaches:

- treat data as CSV (since it's 2 columns and we could ignore the lack of headers) and use a CSV sorting/merging library which allows for external sorting, that way, no mather how big the dataset is, we should be able to solve it, altough the performance might not be great
- import all the data to a SQL database since that's what they excel at: joining, sorting, etc. There's already SQLite on most operating systems, and a version should come preinstalled with Python
- We could use Unix tools like `sort`, `paste` and `awk`, this should work for files larger than machine's memory

Using the SQLite seems like the most straightforward and flexible solution, it's implemented in `file_sort_sql.py`. A high level overview of the solution:

- create a temporary database and table with id, first_name and last_name columns
- read the file with first names and import it to a table via insert statements
- read the file with last names and import it to the same table via update statements on matching IDs, this solves the problem of combining the pairs
- start reading the entries from the table ordered by ID
- output the read entries formatted as: first_name last_name id
- clean up the temporary database

Using this solution the program's RAM usage is very low, output of [memory_profiler](https://pypi.org/project/memory_profiler/) when sorting 10.000.000 entries (each input file has 160MB):

```
Line #    Mem usage    Increment   Line Contents
================================================
     4   10.969 MiB   10.969 MiB   @profile
     5                             def main():
     6   10.969 MiB    0.000 MiB       database_name = 'db.sqlite'
     7   11.676 MiB    0.707 MiB       connection = _setup_db(database_name)
     8   14.098 MiB    2.422 MiB       _insert_data(connection, 'input1.txt', 'input2.txt')
     9    7.824 MiB   -6.273 MiB       _output_sorted_data(connection, 'output.txt')
    10    8.105 MiB    0.281 MiB       _cleanup_db(database_name, connection)
```

### Unix solution to the problem

We could use the shell to solve this problem via the following command: 

`paste <(sort -k 2,2n file1.txt) <(sort -k 2,2n file2.txt) | awk '{print $1 " " $3 " " $4}' > sorted.txt`


A breakdown:

- We sort the files by the 2nd column numerically
- we load both of the files to paste which outputs them in a 2D format: `first_name id last_name id`
- we use awk to select only the 1st (first_name), 3rd (last_name) and 4th (id) column
- we save the output to sorted.txt