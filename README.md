# Python-Numerical-Digit-Distribution-Calculator

---
### CITS1401 - Computational Thinking with Python - Project_2 - (2020/SEM-1)
#### The University of Western Australia

---
#### Overview
Benford’s law is a mathematical rule on how frequent certain digits appear in numbers. For example, it is significantly more likely to see a 1 as the first digit in a number than a 9. For the second digit in a number, 1 is still more likely than 9, but the difference is less. In general, the further down the digit, the more balanced the distribution should be. As this law describes what sort of distributions of digits, we are likely to see, it can be used in detecting fraudulence.

Forensic accounting is about trying to detect the difference between normally occurring numbers, and numbers that have been changed in order to falsify an account. Due to the natural randomness in such accounts, it cannot be determined which individual numbers are fraudulent and which are legitimate. However, the digits over many numbers can be examined to build up a large distribution. If this distribution looks significantly different to the one predicted by Benford’s Law, there is some evidence that the account is fraudulent. 

---
#### Problem Specification
The task for this project is to write a program that can calculate the distribution
of digits for numbers found in a certain file. You are not asked to actually detect
any fraudulence.

**Input:**

Your program must define the function main with the following signature:
~~~
def main(filename,no_places,regularise=False):
~~~
- `filename`: This input argument is the name of the csv (comma separated values) file (a text file in which each value is separated by a comma ',' character - and each 'row' of values is separated by a new line) containing data which includes numerical data which needs to be analysed. There is also no prior knowledge about the number of rows, the number of elements in each row or the number of elements which will be "numerical" in the csv file. Your code will need to analyse the entire file but ensure it analyses only numerical values which include integers and decimal numbers only.
- `no_places`: This input argument provides the information about the number of places in each numerical data to analyse. For example, if this value is 1, we are only examining the distributions of the first digits (from left hand side) in each numerical data. If the value is 3, we are examining the first, second, and third digits (from left hand side) of each numerical data. Each digit place will have its own distribution.
- `regularise`: This input argument is an optional parameter with a default value of `False`. When set to `True`, the distribution values should represent the distribution as a fraction of the total sum for each digit place in the output instead of the count. See below for an example of how your program should work with this parameter set to True. 

---
**Output:**

The function is required to return the list of lists. Each sub-list (inner list) represents the distribution of digits for that digit place. Each sub-list should be of length 10, and represents the counts of each of the digits 1, 2, 3, 4, 5, 6, 7, 8, 9, and 0 respectively (in that order). 

All returned lists must contain numerical values rounded to four decimal places (if required). Remember not to round the values during calculations and round them only at the time of saving them in the output list.

For example, if the number of places input (`no_places`) is 3, then it is expected that the output to be a list of 3 sub-lists. Each sub-list represents the distribution of digits in the first, second, and third digit places respectively. Each sub-list would have a length of 10.

---
**Example:**

A sample interaction is:

Sample 1:
~~~
>>> output = main("sample_accounts.csv",1)
~~~
The output returned in the variable is:
~~~
>>> output
[[26, 22, 28, 22, 16, 20, 31, 22, 13, 0]]
~~~
Sample 2:
~~~
>>> output = main("sample_accounts.csv",1,True)
~~~
The output returned in the variable is:
~~~
>>> output
[[0.13, 0.11, 0.14, 0.11, 0.08, 0.1, 0.155, 0.11, 0.065, 0.0]]
~~~
Sample 3:
~~~
>>> output = main("sample_accounts.csv",3)
~~~
The output returned in the variable is:
~~~
>>> output
[[26, 22, 28, 22, 16, 20, 31, 22, 13, 0], [17, 21, 23, 15, 15, 23, 30, 18, 14, 23], [14, 12, 23, 22, 22, 8, 21, 24, 25, 28]]
~~~

---
**Additional requirements:**

There are few more requirements for your program.

- Your program needs to validate the inputs to the main() function and gracefully terminate if invalid inputs are provided.
- You program needs to terminate gracefully if the file cannot be found or opened.
- For graceful terminations, you may provide an error message followed by an empty list as an output.
- Your program needs to validate the input data from the file and it should analyse the integer part of the data only. Note float numbers digit counts should consist of only the digits to the left of the decimal point (e.g. the number "52.385686" is considered to have 2 digits and therefore only '5' and '2' should be counted by your program).
- Your program needs to consider that all numeric data in the file will not be of same length so distribution will, obviously, not count higher digits (when reading digit numbers from left to right) on the numeric data that does not contain these digits (e.g. if no_places = 5 and your program is processing the number "268" then it will not count anything for digit places 4 and 5). For instance, if you sum all the elements of each sub-list of Sample 3 output (presented above), you will observe that sum of first sub-list is greater than sum of second and third sub-lists. This is due to the reason that there is a numerical data in the csv file which is of single digit only. 

---
NOTE: THIS PROJECT WAS PART OF THE COMPUTATIONAL THINKING WITH PYTHON  UNIT (CITS1401) AT THE UNIVERSITY OF WESTERN AUSTRALIA.
