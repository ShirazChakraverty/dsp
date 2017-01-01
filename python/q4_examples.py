# example of a list comprehension to change the list based on a simple condition
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