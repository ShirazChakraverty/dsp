[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

code:
pmf = thinkstats2.Pmf(t)

thinkplot.Pmf(pmf, linewidth=0.1)

thinkplot.Config(xlabel='Random variate', ylabel='PMF')

random_cdf = thinkstats2.Cdf(np.random.random(1000), label='random')

thinkplot.Cdf(random_cdf)

thinkplot.Config(xlabel='Random Numbers', ylabel='CDF', loc='upper right')


The cdf is a smooth straight line, indicating a uniform distribution, rather than random.
