import json,os
from cpu_registers import cpu_registers

cpu_regs = cpu_registers()
cpu_regs.execute_conditions()

print(cpu_regs.get_largest_registery())
