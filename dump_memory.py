"""
Credit to https://www.pythonsheets.com/appendix/python-gdb.html
"""

import gdb
import time
import re

class DumpMemory(gdb.Command):
    """Dump memory info into a file."""

    def __init__(self):
        super().__init__("dump_memory", gdb.COMMAND_USER)

    def get_addr(self, p, tty):
        """Get memory addresses."""
        cmd = "info proc mappings"
        out = gdb.execute(cmd, tty, True)
        addrs = []
        for l in out.split("\n"):
            if re.match(f".*{p}*", l):
                s, e, *_ = l.split()
                addrs.append((s, e))
        return addrs

    def dump(self, addrs):
        """Dump memory result."""
        if not addrs:
            return

        for s, e in addrs:
            f = int(time.time() * 1000)
            gdb.execute(f"dump memory {f}.bin {s} {e}")

    def invoke(self, args, tty):
        try:
            # cat /proc/self/maps
            addrs = self.get_addr(args, tty)
            # dump memory
            self.dump(addrs)
        except Exception as e:
            print("Usage: dump_memory [pattern]")

DumpMemory()
