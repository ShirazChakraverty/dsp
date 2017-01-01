# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.
    
    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """
    if isinstance(count,int) is True:
        if count < 10:
            return "Number of donuts: ",count
        else:
            return "Number of donuts: many"
    else:
        raise NotImplementedError("Count of donuts must be a number")


def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    if isinstance(s,str) is True:
        if len(s) > 2:
            return s[0]+s[1]+s[len(s)-1]+s[len(s)-2]
        else:
            return ""
    else:
        raise NotImplementedError("Please enter a valid string")


def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """
    if isinstance(s,str) is True:
        if len(s) > 1:
            x = 1
            s1 = s[0]
            while x < len(s):
                if s[x] == s[0]:
                    s1 = s1 + "*"
                    x = x + 1
                else:
                    s1 = s1 + s[x]
                    x = x + 1
            return s1
        else:
            return ""
    else:
        raise NotImplementedError("Please enter a valid string")



def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    if isinstance(a,str) and isinstance(b,str) is True:
        if len(a) > 1 and len(b) > 1:
            return b[0:2]+a[2:len(a)]+" "+a[0:2]+b[2:len(b)]
        else:
            return ""
    else:
        raise NotImplementedError("Please enter two strings at least 2 characters long")


def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    if isinstance(s,str) is True:
        if len(s) > 2:
            string = s[(len(s)-3):len(s)]
            if string <> "ing":
                return s + "ing"
            if string == "ing":
                return s + "ly"
        else:
            return s
    else:
        raise NotImplementedError("Please enter  a string")


def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """
    if isinstance(s,str) is True:
        if s.find("not") < s.find("bad"):
            loc = s.find("not")
            s2 = s[0:loc] + "good"
            return s2
        else:
            return s
    else:
        raise NotImplementedError("Please enter  a string")

def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    if isinstance(a,str) and isinstance(b,str) is True:
        if len(a) % 2 == 0:
            a_front = a[0:(len(a)/2)]
            a_back = a[(len(a)/2):len(a)]
        else:
            a_front = a[0:(len(a)/2)+1]
            a_back = a[(len(a)/2)+1:len(a)]
        if len(b) % 2 == 0:
            b_front = b[0:(len(b)/2)]
            b_back = b[(len(b)/2):len(b)]
        else:
            b_front = b[0:(len(b)/2)+1]
            b_back = b[(len(b)/2)+1:len(b)]
        return a_front + b_front + a_back + b_back
    else:
        raise NotImplementedError("Please enter two strings at least 2 characters long")
