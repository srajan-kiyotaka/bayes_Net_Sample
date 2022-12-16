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