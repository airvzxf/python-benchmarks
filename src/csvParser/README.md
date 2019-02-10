# CSV Parse Benchmarks

These are benchmarks tests for CSV parser

## Usages

Run the main program:<br>
* `PYTHONPATH`: The root path is this project.
* The second line execute the virtual environment python which contains all the libraries.
* The last line run the main script.
```bash
PYTHONPATH=./../../ \
./../../venv/bin/python \
./__main__.py
```


## My results
Sat Sep 23 01:41:46 EDT 2017<br>

__Winner:__ __csvParser__ with `import csv`<br>
Time: csvParser was faster but not to much.<br>
Memory: Almost the same memory use.<br>


### Using csv.log with 120,000 records.

1st Run

| Strategy | Time (s) | Memory (MiB) |
| -------: | -------: | -----------: |
| CSV      |    0.068 |          0.7 |
| Split    |    0.071 |          0.7 |


2nd Run

| Strategy | Time (s) | Memory (MiB) |
| -------: | -------: | -----------: |
| CSV      |    0.071 |          0.7 |
| Split    |    0.070 |          0.7 |


3th Run

| Strategy | Time (s) | Memory (MiB) |
| -------: | -------: | -----------: |
| CSV      |    0.067 |          0.7 |
| Split    |    0.070 |          0.7 |


### Using csv.log with 2,400,000 records.

1st Run

| Strategy | Time (s) | Memory (MiB) |
| -------: | -------: | -----------: |
| CSV      |    1.325 |         18.2 |
| Split    |    1.406 |         18.2 |


2nd Run

| Strategy | Time (s) | Memory (MiB) |
| -------: | -------: | -----------: |
| CSV      |    1.394 |         18.2 |
| Split    |    1.433 |         18.2 |


3th Run

| Strategy | Time (s) | Memory (MiB) |
| -------: | -------: | -----------: |
| CSV      |    1.369 |         18.2 |
| Split    |    1.449 |         18.2 |
