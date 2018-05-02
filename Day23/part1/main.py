#from instructions import instructions
from printer import printer
with open("input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
my_printer = printer(content)
my_printer.run_program()