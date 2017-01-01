# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> A tuple is one dimensional, fixed length and immutable sequence. A list is variable length and mutable, contents can be easily modified.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Set is unordered collection of unique elements, like the keys in a dictionary. 

Set usage:

a = {1,2,3,4,5}
b = { 8,9,3,5}

a & b # intersection

output : set([3,5])

List usage:

a_list = [0,1,3,4,5,6,5,4,4,3,3,3,3,4,4,5,6,2,3,4]

2 in a_list

output : True

Sets are faster for simply finding an element as their structure only allows for a unique set of elements.


---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> simple use of lambda : sort this unsorted baby names list based on length of the name:

baby_names = ["martha","tom","rumpelstiltskin","john","joseph",]

baby_names = sorted(baby_names,key=lambda x: len(set(list(x))))

baby_names
Out[18]: ['tom', 'john', 'martha', 'joseph', 'rumpelstiltskin']

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> # example of a list comprehension to change the list based on a simple condition
print "LIST EXAMPLES FOR COMPREHENSION, MAP, and FILTER"
print "Example of list comprehension"
baby_names = ["martha","tom","rumpelstiltskin","john","joseph",]
print baby_names
baby_names = [names.upper() for names in baby_names if len(names) > 4]
print baby_names

#example of using map
print "Example of Map function"
baby_names = ["martha","tom","rumpelstiltskin","john","joseph",]
print baby_names
baby_length = map(lambda value: len(value), baby_names)
print baby_length

#example of using map
print "Example of filter function returning names with odd number of characters"
baby_names = ["martha","tom","rumpelstiltskin","john","joseph",]
print baby_names
baby_length = filter(lambda value: len(value) % 2 == 1, baby_names)
print baby_length
print "End of List examples"

# example of a set comprehension to change the list based on a simple condition
print "SET EXAMPLES FOR COMPREHENSION, MAP, and FILTER"
print "Example of Set comprehension"
baby_names_set = ("martha","tom","rumpelstiltskin","john","joseph")
print baby_names_set
baby_names_set_rev = (names.upper() for names in baby_names if len(names) > 4)
print baby_names_set_rev

#example of using map
print "Example of Set Map function"
baby_names_set2 = ("martha","tom","rumpelstiltskin","john","joseph")
print baby_names_set2
baby_name_length_set3 = map(lambda value: len(value), baby_names)
print "Name lengths in set:", baby_name_length_set3

#example of using map
print "Example of Set filter function returning names with odd number of characters"
baby_names_set4 = ("martha","tom","rumpelstiltskin","john","joseph")
print baby_names_set4
baby_names_set5 = filter(lambda value: len(value) % 2 == 1, baby_names_set4)
print baby_names_set5


# example of a dict comprehension to change the list based on a simple condition
print "DICTIONARY EXAMPLES FOR COMPREHENSION, MAP, and FILTER"
print "Example of Dictionary comprehension"
baby_names_dict = {1:"martha",2:"tom",3:"rumpelstiltskin",4:"john",5:"joseph"}
print baby_names_dict
baby_names_dict = {v for k,v in baby_names_dict.items() if len(v) > 4}
print baby_names_dict

#example of using map
print "Example of DICT with a Map function"
baby_names_dict = ["martha","tom","rumpelstiltskin","john","joseph",]
print baby_names_dict
baby_length = map(lambda v: len(v), baby_names_dict)
print baby_length

#example of using map
print "Example of DICT filter function returning names with odd number of characters"
baby_names_dict = ["martha","tom","rumpelstiltskin","john","joseph",]
print "All baby names:", baby_names_dict
baby_names_odd = filter(lambda v: len(v) % 2 == 1, baby_names_dict)
print "Only with odd characters:", baby_names_odd
[output]
LIST EXAMPLES FOR COMPREHENSION, MAP, and FILTER
Example of list comprehension
['martha', 'tom', 'rumpelstiltskin', 'john', 'joseph']
['MARTHA', 'RUMPELSTILTSKIN', 'JOSEPH']
Example of Map function
['martha', 'tom', 'rumpelstiltskin', 'john', 'joseph']
[6, 3, 15, 4, 6]
Example of filter function returning names with odd number of characters
['martha', 'tom', 'rumpelstiltskin', 'john', 'joseph']
['tom', 'rumpelstiltskin']
End of List examples
SET EXAMPLES FOR COMPREHENSION, MAP, and FILTER
Example of Set comprehension
('martha', 'tom', 'rumpelstiltskin', 'john', 'joseph')
Example of Set Map function
('martha', 'tom', 'rumpelstiltskin', 'john', 'joseph')
Name lengths in set: [6, 3, 15, 4, 6]
Example of Set filter function returning names with odd number of characters
('martha', 'tom', 'rumpelstiltskin', 'john', 'joseph')
('tom', 'rumpelstiltskin')
DICTIONARY EXAMPLES FOR COMPREHENSION, MAP, and FILTER
Example of Dictionary comprehension
{1: 'martha', 2: 'tom', 3: 'rumpelstiltskin', 4: 'john', 5: 'joseph'}
set(['joseph', 'rumpelstiltskin', 'martha'])
Example of DICT with a Map function
['martha', 'tom', 'rumpelstiltskin', 'john', 'joseph']
[6, 3, 15, 4, 6]
Example of DICT filter function returning names with odd number of characters
All baby names: ['martha', 'tom', 'rumpelstiltskin', 'john', 'joseph']
Only with odd characters: ['tom', 'rumpelstiltskin']


---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> number of days: 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> number of days: 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> number of days: 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





