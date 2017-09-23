# CSV Parse Benchmarks
These are benchmarks test for CSV parser

## 1.1 Install packages in Arch Linux
sudo pacman -S python-pip<br>
sudo pacman -S python-psutil<br>

## 1.2 Install the python packages with pip
sudo pip install profilehooks<br>
sudo pip install memory_profiler<br>

## 2.a Run in command line
Create a function and put this @profile decorator above then execute
one of the these commands line.<br>
`$ timer python file.py`<br>
`$ python -m cProfile file.py`<br>
`$ python -m memory_profiler file.py`<br>

## 2.b Import in your code

### For total time:
`$ python file.py`<br>
```python
from profilehooks import timecall
@timecall
def functionName():
	#...

functionName()
```

### For time:
`$ python file.py`<br>
```python
from profilehooks import profile
@profile
def functionName():
	#...

functionName()
```

### For memory:
`$ python file.py`<br>
```python
from memory_profiler import profile
@profile
def functionName():
	#...

functionName()
```

### For coverage:
`$ python file.py`<br>
```python
from profilehooks import coverage
@coverage
def functionName():
	#...

functionName()
```

## My results

### Sat Sep 23 01:41:46 EDT 2017
__Winner:__ __csvParser__ with `import csv`<br>
CPU: Both useed the same resources.<br>
Time: csvParser was faster but not to much.<br>
Memory: Both used the same.
