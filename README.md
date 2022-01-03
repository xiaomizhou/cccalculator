# cccalculator
calculate the cyclomatic complexity of python source file
Use M = E − N + 2 to calculate the complexity .
The output is the McCabe complexity of each python source file under the path.
# Installation
This package currently only works with Python 3

`pip install cccalculator`

# Usage
`from cccalculate.calculate import do_calculate_from_directory`
`do_calculate_from_directory('/path/to/your/pythonfiles/')`


   The output will be like this

    /path_to_your_python_file_directory/test_file4.py

    fun:7----------6

    /path_to_your_python_file_directory/test_file1.py

    class:1--fun:2----------1

    class:1--fun:5----------6

    fun:26----------5

Explanations of output

class:1--fun:5----------6 

in the class which starts at line 1, the cyclomatic complexity of function which starts at line 5 is 6