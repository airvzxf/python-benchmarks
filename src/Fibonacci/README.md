# Fibonacci

These are benchmarks tests for Fibonacci. It request a integer and
it returns the Fibonacci number at this position.

The tests cases cover these three benchmarks:
* Recursion and complexity O(n2).
* Recursion with Memoization and complexity O(n).
  - Top-Down storage technique.
* Dynamic programming with tabulation and complexity O(n).
  - Bottom-Up storage technique.


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

Fri Feb  8 20:39:42 CST 2019


### Tests based on recursion.

The slowest strategy is the recursion because it's deep and it does a lot of repeated operations.<br>
For numbers greater than 50 it was very slow in fact for 50 it spend at least 1 hour.


Get the Fibonacci number at position 40.

|   Strategy  | Method Calls | Time (s) | Memory (MiB) |
| ----------: | -----------: | -------: | -----------: |
| Recursion   |  204,668,309 |   17.167 |            0 |
| Memoization |           77 |        0 |            0 |
| Tabulation  |            1 |        0 |            0 |


### Tests based on Memoization.

It's a good solution except I'm not able to run positions bigger than 900 because it create a `RecursionError`
because it exceeded the max recursion deep also it consumes memory.

Get the Fibonacci number at position 900.<br>

|   Strategy  | Method Calls | Time (s) | Memory (MiB) |
| ----------: | -----------: | -------: | -----------: |
| Memoization |        1,797 |    0.001 |          1.1 |
| Tabulation  |            1 |        0 |            0 |


### Tests based on Tabulation.

For this problem / algorithm is the best solution.

Get the Fibonacci number at position 500,000.<br>

|   Strategy  | Method Calls | Time (s) | Memory (MiB) |
| ----------: | -----------: | -------: | -----------: |
| Tabulation  |            1 |    5.069 |      4.6 MiB |
