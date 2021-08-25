# 📌 Installing an auto formatter
# pip install black
# pip3 install black
# python -m pip install black
# python3 -m pip install black

# VS Code -> Setting -> search(python format provider) && Choose 'Black'
# VS Code -> Setting -> search(Format on Save) && choose 'ON'
def long_function_name_with_long_args(
    argument1, argument2, argument3, argument4, argument5, argument6, argument7
):
    print("run")


# 📌 General PEP8 Guidelines
# indent using space -> 4spaces


# 📌 Naming COnventions
# 👉 for variables -> use snake case
# hello_world -> Snake Case 👈 || helloWorld -> Camel Case || HelloWorld -> Pascal Case
hello_world_here

# 👉 for constants -> use all upper cases
HELLO_WORLD
COLOR = (255, 255, 255)
BG_COLOR = (255, 255, 255)

# 👉 for modules(Python file itself) -> all in lower case
# if multiple words then separate them using underscore(_)

# 👉 for Function -> same as variables
def hello_world()

# 👉 for Classes -> Pascal Case
class BaseClass:

class Base:

# 👉 for Exception -> Pascal Case
class XException:


# 📌 METHOD PARAMETER NAMING
# 👉 1st parameter of any instance method should always be named 'self'
class Test:
    def test(self):
        pass

# 👉 1st parameter of any class method should always be named 'cls'
    @classmethod
    def cls_method(cls):
        pass


# 📌 FUNCTION & CLASS SPACING
# 👉 Top level function or classes should be separated by 2 blank lines
# 👉 methods inside of classes are space out with 1 blank line
class Test:
    pass


class Foo:
    def __init__(self):
        pass

    def foo(self):
        pass


def bar():
    pass


# 📌 IMPORTS
# all the import as the top of the files
# 👉 import os, sys <- NOT CORRECT
import os
import sys

# 👉 from a module we can import them on the same line
from os import path, stat

# 👉 Should not use wild card import
# from os import * <- NOT CORRECT


# 📌 SINGLE OR DOUBLE QUOTES
# MIND IT: Only use one for the whole file/project
""
''


# 📌 WHITESPACES
# 🎈 Correct:
spam(ham[1], {eggs: 2})
# Wrong:
spam( ham[ 1 ], { eggs: 2 } )

# 🎈 Correct:
foo = (0,)
# Wrong:
bar = (0, )

# 🎈 Correct:
spam(1)
# Wrong:
spam (1)

# 🎈 Correct:
i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)
# Wrong:
i=i+1
submitted +=1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)

# 🎈 Correct:
def complex(real, imag=0.0):
    return magic(r=real, i=imag)
# Wrong:
def complex(real, imag = 0.0):
    return magic(r = real, i = imag)


# 📌 IN-LINE COMMENTS
# before # -> 2 space & after # -> 1 space & 1st word must be capital letter.
# 🎈 Correct:
COLOR = (0, 255, 0)  # This in correct
# Wrong:
COLOR = (0, 255, 0) #This in incorrect


# 📌 IS NONE OR ==NONE
x = None

if x is None:
    pass

# 🎈 Correct:
if foo is not None:
    pass
# Wrong
if not foo is None:
    pass


# 📌 TRY & EXCEPT
# 🎈 Correct:
try:
    import platform_specific_module
except ImportError:
    platform_specific_module = None
# Wrong
try:
    import platform_specific_module
except:
    platform_specific_module = None


# 📌 STRING PREFIX & SUFFIX
# 🎈 Correct:
if foo.startswith("bar"):
    pass
# Wrong
if foo[:3] == "bar":
    pass
