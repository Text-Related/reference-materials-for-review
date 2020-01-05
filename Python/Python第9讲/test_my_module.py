# using a module
#my_module contains the c_to_f()function
import my_module
cel = float(input('enter a temperature in Celsius:'))
fah = my_module.c_to_f(cel)
print("That's {0} degree of Fahernheit".format(fah))