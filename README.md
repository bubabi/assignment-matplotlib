# assignment-matplotlib
Fraud Detection in 2012 USA Presidential Election

## Getting Started

A Python program that analyzes the results of the USA presidential election held in 2012 and interprets whether it is fraudulent or not.

### Prerequisites

* [matplotlib](https://matplotlib.org/users/installing.html) - the Python 2D plotting library used

* [numPy](https://www.scipy.org/install.html) - is the fundamental package for scientific computing with Python


### Installing

The arguments of the function defined (filename and a list of nominees’ names) dynamic and takes their values from command-line arguments.

```
$ python assignment4.py ElectionUSA2012.csv Obama,Romney,Johnson,Stein
```

![ComparativeVotes.pdf](https://image.ibb.co/g2q2Rb/ss1.png)

![CompVotePercs.pdf](https://image.ibb.co/mnCrmb/ss2.png)

#### Result

```
MSE value of 2012 USA election is 0.0023644752018454436
The number of MSE of random samples which are larger than or equal to USA election MSE is 4202
The number of MSE of random samples which are smaller than USA election MSE is 5798
2012 USA election rejection level p is 0.5798
Finding: There is no statistical evidence to reject null hypothesis
```
