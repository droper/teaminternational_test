# Challenge solution

We implement the Feetwick Tree to solve the challenge complying with the given parameters.

## Setup

`$ git clone https://github.com/droper/teaminternational_test.git`

## Run

Add numbers and calculate less, between and greater.  

```
$ python
>>> from classes import DataCapture, DataStats
>>> capture = DataCapture()
>>> capture.add(3)
>>> capture.add(9)
>>> capture.add(3)
>>> capture.add(4)
>>> capture.add(6)
>>> stats = capture.build_stats()
>>> stats.less(4)
2
>>> stats.between(3, 6)
4
>>> stats.greater(4)
2
```

Run the tests.

```
$ python tests.py
```

