# import mymodule as mm
from mymodule import greet, goodbye, default_name

greeting = greet('사람이름')
bye = goodbye()

print(greeting)
print(bye)
print(default_name)