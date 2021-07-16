# pdb is builtin python debugger

a = input('type a')
b = input('type b')

breakpoint()

def sum_the_values(a,b):
	print('We are inside func')
	print(a+b)
	

sum_the_values(a,b)
breakpoint()
print('End of the code!!')

# We can control how code is running
# 1) pdb console appears whenever it sees a breakpoint().
# 2) c(continue) => continue all the leftover code after breakpoint.
# or untill the next breakpoint.
# 3) n(next) => runs the very next piece of code
# 4) s(step inside) => to step inside a function such that enter will
# work like showing us next line which is going to execute instead
# of normal behaviour
# 5) We can use print to know values of the variables at a stage in 
# pdb
# 6) We can also know the data type by using 'whatis'

#cmd py pdb_working.py