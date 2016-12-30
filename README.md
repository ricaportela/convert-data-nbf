Convert Data without Python builtin Functions
=============================================

Getting Started
---------------

### Initial Setup ###
1. On Linux make a new virtualenv: ``python3.5 -m venv .venv`` 
2. Activate the virtualenv: ``source .venv/bin/activate``



### Instructions ###
You should create the following function using Python:
def change_date(date, op, value):
Where,
date: A date as String in the format “dd/MM/yyyy HH24:mi”;
op: Can be only ‘+’ | ‘-‘;
value: The integer value that should be incremented/decremented. 
  It will be expressed in minutes;
Restrictions:
- you shall not work with non-native classes / libraries;
- you shall not make use python's datetime module or any Date handler library;
- if the op is not valid an exception must be thrown;
- if the value is smaller than zero, you should ignore its signal;
- if the result sum is bigger than max value to the field, you should 
  increment its immediate bigger field;
- ignore the fact that February have 28/29 days and always consider only 28 days;
- ignore the daylight save time rules.

Example:
========
change_date("01/03/2010 23:00", '+', 4000) = "04/03/2010 17:40"

