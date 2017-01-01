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

placed code in this file: [q4_examples](python/q4_examples.py)

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





