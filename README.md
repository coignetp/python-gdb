# python-gdb
Some python script to ease debugging with gdb

# Install
Clone the repository
`git clone https://github.com/coignetp/python-gdb.git`

Install the requirements
`pip3 install requirements.txt`
## How to use it
If you have a compiled program you want to debug it using `trace_function`, use:
```
gdb ./my_prog
source /path/to/repo/trace_function.py
trace_function my_function
run
...
```