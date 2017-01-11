# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > 

pwd - to know where you are

ls - to list contenst of current directory

mkdir and rmdir - make and delete directory

cat file.txt | wc -l counts the lines in a file, very useful

head or tail file.txt prints the first or last 10 lines

head -1 file.txt prints the first line only

grep age students.txt looks for the string age in the file

grep -n gives the line number

grep --color age students.txt highlights the text in color

echo $PATH gives me the value in this variabledirectories in this variable

wc for word counts

sort -k1 energy.csv gives me the first field sorted

uniq -d energy.csv gives me a quick check on duplicate lines



###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> >

ls gives a simple list of directory contents

ls -ala does not ignore entries with a dot in front

ls -l gives a detailed listing- permissions, size etc.

ls - lh gives in human readable sizes, like K and M etc.

ls -lah includes items with a dot infront, lists and gives human readable sizes

ls -t sorted by time of modification

ls -Glp gives a color coded listing with / appended to directories



###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > 
ls -lh - human readable format

ls - ld displays conent info of directories

ls -lt ordering files by last modified time

ls -ltr order by last modified time in reverse order

ls -l most common, gives all the details of the list of contents


---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > 
xargs can take a list of file names and perform a command operation on them, for example, we can find the word could of all csv files at once.

like, ls *.csv | xargs wc -w : will give me a word could of all the csv files

 

