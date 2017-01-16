[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

```python

print ('U.S. Male pop. in range:', np.round((dist.cdf(185.42) - dist.cdf(177.8)) * 100) , '%')
# logic explained : cumulative distribution upto the high limit - cumulative distribution upto the lower limit
# the high limit is height os 6 feet 1 inch and low is 5 feet and 10 inch

```

U.S. Male pop. in range : 34.0 %
