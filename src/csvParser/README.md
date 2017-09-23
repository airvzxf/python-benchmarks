# CSV Parse Benchmarks
This benchmarks test the CSV parser

## 1.1 Install packages in Arch Linux
sudo pacman -S python-pip
sudo pacman -S python-psutil

## 1.2 Install the python packages with pip
sudo pip install memory_profiler
sudo pip install profilehooks

## 2.a Run in command line
Create a function and put @profile above then execute the command line
python -m cProfile file.py
python -m memory_profiler file.py
timer python file.py

## 2.b import in your code

### For total time:
```python
from profilehooks import timecall
@timecall
def functionName():
```

### For time:
```python
from profilehooks import profile
@profile
def functionName():
```

### For memory:
```python
from memory_profiler import profile
@profile
def functionName():
```
