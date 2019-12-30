import json
import gdb
import time

tracepoint_function = {}
tpfc = {}

class TracepointFunction(gdb.Breakpoint):
  def __init__(self, tty, *args):
    super().__init__(*args)
    self.silent = True
    self.function_name = args
    self.tty = tty
    tracepoint_function[self.function_name] = {}

  def stop(self):
    cmd = "info args"
    raw_args = gdb.execute(cmd, self.tty, True)
    fc_args = {}
    for l in raw_args.split("\n"):
      a = l.split(" = ")
      if len(a) == 2:
        fc_args[a[0]] = a[1]

    fc_args = json.dumps(fc_args)

    if not fc_args in tracepoint_function[self.function_name]:
      tracepoint_function[self.function_name][fc_args] = 0
    
    tracepoint_function[self.function_name][fc_args] += 1 

    # do not stop
    return False

class TraceFunction(gdb.Command):
  """
  Trace a function call
  """

  def __init__(self):
    super().__init__("trace_function", gdb.COMMAND_USER)

  def invoke(self, args, tty):
    try:
      # global tracepoint_function
      # global tpfc
      tpfc[args] = TracepointFunction(tty, args)
    except Exception as e:
      print(e)
      print("Usage: trace_function [function_name]")


def finish(event):
  ts = int(time.time() * 1000)
  with open(f"{ts}.trf", "w") as file:
    file.write(str(tracepoint_function))

  for t in tracepoint_function.keys():
    print(f"Tracepoint {t}:")
    for args, count in tracepoint_function[t].items():
      print(f"\tArgs: '{args}' / Count: {count}")


gdb.events.exited.connect(finish)
TraceFunction()
