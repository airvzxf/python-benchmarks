# CSV Parse Benchmarks
This benchmarks test the CSV parser

## 1.1 Install packages in Arch Linux
sudo pacman -S python-pip<br>
sudo pacman -S python-psutil<br>

## 1.2 Install the python packages with pip
sudo pip install memory_profiler<br>
sudo pip install profilehooks<br>

## 2.a Run in command line
Create a function and put @profile above then execute the command line.<br>
`python -m cProfile file.py`<br>
`python -m memory_profiler file.py`<br>
`timer python file.py`<br>

## 2.b import in your code

### For total time:
```python
from profilehooks import timecall
@timecall
def functionName():
	#...

functionName()
```

### For time:
```python
from profilehooks import profile
@profile
def functionName():
	#...

functionName()
```

### For memory:
```python
from memory_profiler import profile
@profile
def functionName():
	#...

functionName()
```
