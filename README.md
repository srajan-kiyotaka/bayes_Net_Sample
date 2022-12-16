<H1><center>
    Bayes Nets and Sampling
</center></H1>

## About: 

Developed code from scratch to compute an input probability query on a given Bayes net on discrete random variables using Prior sampling, Rejection Sampling, Likelihood weighting and Gibbs sampling. <br>
I had also written helper function to generate samples from any input univariate discrete distribution and then use it in your Bayes Net sampling code.

## BayesNets Class:

I implemented a BayesNets Class to do all the required task and computations.<br>
Basically I created a single class to do all the calculation, extractions of details from the file as well as implement all the sampling methods and sample generation.

## Install the Python Package

```
pip install bayes-nets-sample
```

## Import the Python Package

```
from bayes import bayesNets
```

## To see the Sample .txt file

```
from bayes.sample_input_txt import SampleInputTXT
SampleInputTXT().generate_sample()
```

## To Get more information about the BayesNets Class as well as its methods:
### run the following command:

```
help(BayesNets)
```

## Lets Start By Creating an object of BayesNets and extract the information from the file:

```
bayesNet = BayesNets(filepath = "example_bayesnet.txt")
```

## Let's Print The Extracted Information: 

```
print(bayesNet)
```

## Let's See how a single sample is generated:

```
bayesNet.generateSample()
```

## Now Lets Calculate the Query result using Prior Sampling Method:

`With verbose = True`

```
bayesNet.doPriorSampling(TOTAL_SAMPLE = 10000, verbose = True)
```

## Now Lets Calculate the Query result using Prior Sampling Method:

`With verbose = False`
- Just to see the final result.

```
bayesNet.doPriorSampling(TOTAL_SAMPLE = 10000, verbose = False)
```

## Now Lets Calculate the Query result using Rejection Sampling Method:

`With verbose = True`

```
bayesNet.doRejectionSampling(TOTAL_SAMPLE_REQUIRED = 10000, verbose = True)
```

## Now Lets Calculate the Query result using Rejection Sampling Method:

`With verbose = False`
- Just to see the final result.

```
bayesNet.doRejectionSampling(TOTAL_SAMPLE_REQUIRED = 10000, verbose = False)
```

## Let's See how a single weighted sample is generated:

```
bayesNet.generateWeightedSample(verbose = True)
```

## Now Lets Calculate the Query result using Likelihood Weighting Method:

`With verbose = True`

```
bayesNet.doLikelihoodWeighting(TOTAL_SAMPLE = 10000, verbose = True)
```

## Now Lets Calculate the Query result using Likelihood Weighting Method:

`With verbose = False`
- Just to see the final result.

```
bayesNet.doLikelihoodWeighting(TOTAL_SAMPLE = 10000, verbose = False)
```

## Sample File

```
5, B, E, A, J, M
B, +b, -b
E, +e, -e
A, +a, -a
J, +j, -j
M, +m, -m
B |
+b, 0.001
-b, 0.999
E |
+e, 0.002
-e, 0.998
A | B,E
+b, +e, +a, 0.95
+b, +e, -a, 0.05
+b, -e, +a, 0.94
+b, -e, -a, 0.06
-b, +e, +a, 0.29
-b, +e, -a, 0.71
-b, -e, +a, 0.001
-b, -e, -a, 0.999
J | A
+a, +j, 0.9
+a, -j, 0.1
-a, +j, 0.05
-a, -j, 0.95
M | A
+a, +m, 0.7
+a, -m, 0.3
-a, +m, 0.01
-a, -m, 0.99
Query: P( B=+b| J=+j)
```