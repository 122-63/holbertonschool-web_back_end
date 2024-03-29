# 0x00. Python - Variable Annotations
## Details
      By Emmanuel Turlay, Staff Software Engineer at Cruise          Weight: 1                Ongoing project - started Jun 6, 2022 , must end by Jun 7, 2022           - you're done with 0% of tasks.              Checker was released at Jun 6, 2022 12:00 PM        An auto review will be launched at the deadline      ### Concepts
For this project, we expect you to look at this concept:
* [Advanced Python](https://intranet.hbtn.io/concepts/136) 

 ![](https://i.redd.it/y9y25tefi5401.png) 

## Resources
Read or watch :
* [Python 3 typing documentation](https://intranet.hbtn.io/rltoken/AgrgHs3ohrFJnT3Eece1UQ) 

* [MyPy cheat sheet](https://intranet.hbtn.io/rltoken/iEWC38l9R9216w1Y-x8pMg) 

## Learning Objectives
### General
At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/0kx3ZdIopb6qMTq4TN-blw) 
 ,  without the help of Google :
* Type annotations in Python 3
* How you can use type annotations to specify function signatures and variable types
* Duck typing
* How to validate your code with  ` mypy ` 
## Requirements
### General
* Allowed editors:  ` vi ` ,  ` vim ` ,  ` emacs ` 
* All your files will be interpreted/compiled on Ubuntu 18.04 LTS using  ` python3 `  (version 3.7)
* All your files should end with a new line
* The first line of all your files should be exactly  ` #!/usr/bin/env python3 ` 
* A  ` README.md `  file, at the root of the folder of the project, is mandatory
* Your code should use the  ` pycodestyle `  style (version 2.5.)
* All your files must be executable
* The length of your files will be tested using  ` wc ` 
* All your modules should have a documentation ( ` python3 -c 'print(__import__("my_module").__doc__)' ` )
* All your classes should have a documentation ( ` python3 -c 'print(__import__("my_module").MyClass.__doc__)' ` )
* All your functions (inside and outside a class) should have a documentation ( ` python3 -c 'print(__import__("my_module").my_function.__doc__)' `  and  ` python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)' ` )
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
## Tasks
### 0. Basic annotations - add
          mandatory         Progress vs Score  Task Body Write a type-annotated function   ` add `   that takes a float   ` a `   and a float   ` b `   as arguments and returns their sum as a float. 
```bash
bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3
add = __import__('0-add').add

print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__)

bob@dylan:~$ ./0-main.py
True
{'a':  <class 'float'>, 'b': <class 'float'>, 'return': <class 'float'>}

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-web_back_end ` 
* Directory:  ` 0x00-python_variable_annotations ` 
* File:  ` 0-add.py ` 
 Self-paced manual review  Panel footer - Controls 
### 1. Basic annotations - concat
          mandatory         Progress vs Score  Task Body Write a type-annotated function   ` concat `   that takes a string   ` str1 `   and a string   ` str2 `   as arguments and returns a concatenated string
```bash
bob@dylan:~$ cat 1-main.py
#!/usr/bin/env python3
concat = __import__('1-concat').concat

str1 = "egg"
str2 = "shell"

print(concat(str1, str2) == "{}{}".format(str1, str2))
print(concat.__annotations__)

bob@dylan:~$ ./1-main.py
True
{'str1': <class 'str'>, 'str2': <class 'str'>, 'return': <class 'str'>}

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-web_back_end ` 
* Directory:  ` 0x00-python_variable_annotations ` 
* File:  ` 1-concat.py ` 
 Self-paced manual review  Panel footer - Controls 
### 2. Basic annotations - floor
          mandatory         Progress vs Score  Task Body Write a type-annotated function   ` floor `   which takes a float   ` n `   as argument and returns the floor of the float.
```bash
bob@dylan:~$ cat 2-main.py
#!/usr/bin/env python3

import math

floor = __import__('2-floor').floor

ans = floor(3.14)

print(ans == math.floor(3.14))
print(floor.__annotations__)
print("floor(3.14) returns {}, which is a {}".format(ans, type(ans)))

bob@dylan:~$ ./2-main.py
True
{'n': <class 'float'>, 'return': <class 'int'>}
floor(3.14) returns 3, which is a <class 'int'>

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-web_back_end ` 
* Directory:  ` 0x00-python_variable_annotations ` 
* File:  ` 2-floor.py ` 
 Self-paced manual review  Panel footer - Controls 
### 3. Basic annotations - to string
          mandatory         Progress vs Score  Task Body Write a type-annotated function   ` to_str `   that takes a float   ` n `   as argument and returns the string representation of the float.
```bash
bob@dylan:~$ cat 3-main.py
#!/usr/bin/env python3
to_str = __import__('3-to_str').to_str

pi_str = to_str(3.14)
print(pi_str == str(3.14))
print(to_str.__annotations__)
print("to_str(3.14) returns {} which is a {}".format(pi_str, type(pi_str)))

bob@dylan:~$ ./3-main.py
True
{'n': <class 'float'>, 'return': <class 'str'>}
to_str(3.14) returns 3.14, which is a <class 'str'>

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-web_back_end ` 
* Directory:  ` 0x00-python_variable_annotations ` 
* File:  ` 3-to_str.py ` 
 Self-paced manual review  Panel footer - Controls 
### 4. Define variables
          mandatory         Progress vs Score  Task Body Define and annotate the following variables with the specified values:
*  ` a ` , an integer with a value of 1
*  ` pi ` , a float with a value of 3.14
*  ` i_understand_annotations ` , a boolean with a value of True
*  ` school ` , a string with a value of “Holberton”
```bash
bob@dylan:~$ cat 4-main.py
#!/usr/bin/env python3

a = __import__('4-define_variables').a
pi = __import__('4-define_variables').pi
i_understand_annotations = __import__('4-define_variables').i_understand_annotations
school = __import__('4-define_variables').school

print("a is a {} with a value of {}".format(type(a), a))
print("pi is a {} with a value of {}".format(type(pi), pi))
print("i_understand_annotations is a {} with a value of {}".format(type(i_understand_annotations), i_understand_annotations))
print("school is a {} with a value of {}".format(type(school), school))

bob@dylan:~$ ./4-main.py
a is a <class 'int'> with a value of 1
pi is a <class 'float'> with a value of 3.14
i_understand_annotations is a <class 'bool'> with a value of True
school is a <class 'str'> with a value of Holberton

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-web_back_end ` 
* Directory:  ` 0x00-python_variable_annotations ` 
* File:  ` 4-define_variables.py ` 
 Self-paced manual review  Panel footer - Controls 
### 5. Complex types - list of floats
          mandatory         Progress vs Score  Task Body Write a type-annotated function   ` sum_list `   which takes a list   ` input_list `   of floats as argument and returns their sum as a float.
```bash
bob@dylan:~$ cat 5-main.py
#!/usr/bin/env python3

sum_list = __import__('5-sum_list').sum_list

floats = [3.14, 1.11, 2.22]
floats_sum = sum_list(floats)
print(floats_sum == sum(floats))
print(sum_list.__annotations__)
print("sum_list(floats) returns {} which is a {}".format(floats_sum, type(floats_sum)))

bob@dylan:~$ ./5-main.py
True
{'input_list': typing.List[float], 'return': <class 'float'>}
sum_list(floats) returns 6.470000000000001 which is a <class 'float'>

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-web_back_end ` 
* Directory:  ` 0x00-python_variable_annotations ` 
* File:  ` 5-sum_list.py ` 
 Self-paced manual review  Panel footer - Controls 
### 6. Complex types - mixed list
          mandatory         Progress vs Score  Task Body Write a type-annotated function   ` sum_mixed_list `   which takes a list   ` mxd_lst `   of integers and floats and returns their sum as a float.
You need to keep the same order to pass the checks (Union[int, float]).
```bash
bob@dylan:~$ cat 6-main.py
#!/usr/bin/env python3

sum_mixed_list = __import__('6-sum_mixed_list').sum_mixed_list

print(sum_mixed_list.__annotations__)
mixed = [5, 4, 3.14, 666, 0.99]
ans = sum_mixed_list(mixed)
print(ans == sum(mixed))
print("sum_mixed_list(mixed) returns {} which is a {}".format(ans, type(ans)))

bob@dylan:~$ ./6-main.py
{'mxd_lst': typing.List[typing.Union[int, float]], 'return': <class 'float'>}
True
sum_mixed_list(mixed) returns 679.13 which is a <class 'float'>

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-web_back_end ` 
* Directory:  ` 0x00-python_variable_annotations ` 
* File:  ` 6-sum_mixed_list.py ` 
 Self-paced manual review  Panel footer - Controls 
### 7. Complex types - string and int/float to tuple
          mandatory         Progress vs Score  Task Body Write a type-annotated function   ` to_kv `   that takes a string   ` k `   and an int OR float   ` v `   as arguments and returns a tuple. The first element of the tuple is the string   ` k `  . The second element is the square of the int/float   ` v `   and should be annotated as a float.
You need to keep the same order to pass the checks (Union[int, float]).
```bash
bob@dylan:~$ cat 7-main.py
#!/usr/bin/env python3

to_kv = __import__('7-to_kv').to_kv

print(to_kv.__annotations__)
print(to_kv("eggs", 3))
print(to_kv("school", 0.02))

bob@dylan:~$ ./7-main.py
{'k': <class 'str'>, 'v': typing.Union[int, float], 'return': typing.Tuple[str, float]}
('eggs', 9)
('school', 0.0004)

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-web_back_end ` 
* Directory:  ` 0x00-python_variable_annotations ` 
* File:  ` 7-to_kv.py ` 
 Self-paced manual review  Panel footer - Controls 
### 8. Complex types - functions
          mandatory         Progress vs Score  Task Body Write a type-annotated function   ` make_multiplier `   that takes a float   ` multiplier `   as argument and returns a function that multiplies a float by   ` multiplier `  .
```bash
bob@dylan:~$ cat 8-main.py
#!/usr/bin/env python3

make_multiplier = __import__('8-make_multiplier').make_multiplier
print(make_multiplier.__annotations__)
fun = make_multiplier(2.22)
print("{}".format(fun(2.22)))

bob@dylan:~$ ./8-main.py
{'multiplier': <class 'float'>, 'return': typing.Callable[[float], float]}
4.928400000000001

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-web_back_end ` 
* Directory:  ` 0x00-python_variable_annotations ` 
* File:  ` 8-make_multiplier.py ` 
 Self-paced manual review  Panel footer - Controls 
### 9. Let's duck type an iterable object
          mandatory         Progress vs Score  Task Body Annotate the below function’s parameters and return values with the appropriate types
 ` def element_length(lst):
    return [(i, len(i)) for i in lst]
 ` ```bash
bob@dylan:~$ cat 9-main.py 
#!/usr/bin/env python3

element_length =  __import__('9-element_length').element_length

print(element_length.__annotations__)

bob@dylan:~$ ./9-main.py 
{'lst': typing.Iterable[typing.Sequence], 'return': typing.List[typing.Tuple[typing.Sequence, int]]}

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-web_back_end ` 
* Directory:  ` 0x00-python_variable_annotations ` 
* File:  ` 9-element_length.py ` 
 Self-paced manual review  Panel footer - Controls 
[Done with the mandatory tasks? Unlock 3 advanced tasks now!](https://intranet.hbtn.io/projects/574/unlock_optionals) 

