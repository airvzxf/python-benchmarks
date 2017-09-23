# CSV Parse Benchmarks
These are benchmarks test for CSV parser

## Usages
run the main program:<br>
`$ python __main__.py`<br>

You're able to modified the functions of:<br>
`splitParse.py`<br>
`csvParse.py`<br>

## Installation and setup

### 1.1 Install packages in Arch Linux
`$ sudo pacman -S python-pip`<br>
`$ sudo pacman -S python-psutil`<br>

### 1.2 Install the python packages with pip
`$ sudo pip install profilehooks`<br>
`$ sudo pip install memory_profiler`<br>

### 2.a Run in command line
Create a function and put this @profile decorator above then execute
one of the these commands line.<br>
`$ timer python file.py`<br>
`$ python -m cProfile file.py`<br>
`$ python -m memory_profiler file.py`<br>

### 2.b Import in your code

#### For total time:
`$ python file.py`<br>
```python
from profilehooks import timecall

@timecall
def function_name():
    # something
    pass

# Execute the function
function_name()
```

#### For time:
`$ python file.py`<br>
```python
from profilehooks import profile

@profile
def function_name():
    # something
    pass

# Execute the function
function_name()
```

#### For memory:
`$ python file.py`<br>
```python
from memory_profiler import profile

@profile
def function_name():
    # something
    pass

# Execute the function
function_name()
```

#### For coverage:
`$ python file.py`<br>
```python
from profilehooks import coverage

@coverage
def function_name():
    # something
    pass

# Execute the function
function_name()
```

## My results

### Sat Sep 23 01:41:46 EDT 2017
__Winner:__ __csvParser__ with `import csv`<br>
Time: csvParser was faster but not to much.<br>
Memory: Almost the same memory use.<br>

__Used travel.log with 50,000 records__<br>
Speed: 22.63% faster<br>
Memory: 15.1 MiB<br>

|  CSV  | Split |    %   | Average |
| ----: | -----:| ------:| -------:|
| 0.058 | 0.072 | 19.44% |         |
| 0.063 | 0.083 | 24.10% | 22.63%  |
| 0.059 | 0.078 | 24.36% |         |


__Used travel.log with 500,000 records__<br>
Speed: 21.24% faster<br>
Memory: 19.1 MiB<br>

|  CSV  | Split |    %   | Average |
| ----: | -----:| ------:| -------:|
| 0.636 | 0.792 | 19.70% |         |
| 0.604 | 0.807 | 25.15% | 21.24%  |
| 0.611 | 0.753 | 18.86% |         |
