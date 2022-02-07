print("\nThis program prints a text in the terminal with the color you want")

from termcolor import colored

text = str(input("\nYour text :"))

color = str(input("\nYour color :"))

color = color.casefold()

print("\n"+colored(text, color))


# There is also a second method to print a text in color in the terminal.
# This method only needs one line of code!

" print('\x1b[38;2;r;g;bm' + 'Zuper' + '\x1b[38;2;r;g;bm') "

# Ok.. Let me explain you this line:
# 'Zuper' this is the text you want to print.

# The first '\x1b[38;2;r;g;bm' 
# Here, you just need to replace the r and g and b to have the color you want.

# The second '\x1b[38;2;r;g;bm' And this is the background color.

