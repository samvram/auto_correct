# Autocorrect

In this assignment we will be training a language model to build a spell checker. Specifically, we will
be implementing part of a noisy-channel model for spelling correction. We will give the likelihood
term, or edit model, and Our job is to make a language model, the prior distribution in the noisy
channel model. At test time we will be given a sentence with exactly one typing error. We then select
the correction which gets highest likelihood under the noisy-channel model, using Our language
model as the prior. Our language models will be evaluated for accuracy, the number of valid
corrections, divided by the number of test sentences.

## Language Models used:
* **Laplace Unigram Model** - A unigram model with add-one smoothing. Treat out-of-
vocabulary items as a word which was seen zero times in training.
* **Laplace Bigram Model** - A bigram model with add-one smoothing.
* **Stupid Back-Off Model** - Uses an unsmoothed bigram model combined with backoff to
an add-one smoothed unigram model
* **Custom Language Model** - Uses a smoothened Bigram and Unigram model estimating probabilities in a 
fashion similar to stupid back off but slightly different.

## Evaluation
The code SpellChecker.py returns the metrics used for evaluation.

The results are:
````
Uniform Language Model : 
correct: 31 total: 471 accuracy: 0.065817
Laplace Unigram Language Model: 
correct: 52 total: 471 accuracy: 0.110403
Laplace Bigram Language Model: 
correct: 65 total: 471 accuracy: 0.138004
Stupid Backoff Language Model: 
correct: 86 total: 471 accuracy: 0.182590
Custom Language Model: 
correct: 90 total: 471 accuracy: 0.191083
````
 
 The required parameters for accuracy were:
````
Model Name                         Accuracy
*******************************************
Laplace Unigram Language Model       0.11 
Laplace Bigram Language Model        0.13
Stupid Backoff Language Model        0.18
Custom Language Model                0.18
````

## Conclusion

As we can clearly see, the given resuts are well above the 
required metrics.