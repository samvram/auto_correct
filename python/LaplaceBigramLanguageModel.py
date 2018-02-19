import math,collections

class LaplaceBigramLanguageModel:

  def __init__(self, corpus):
    """Initialize your data structures in the constructor."""
    # TODO your code here
    self.bigramCounts = collections.defaultdict(lambda: collections.defaultdict(lambda: 0))
    self.unigramCounts = collections.defaultdict(lambda: 0)
    self.total = 0
    self.train(corpus)

  def train(self, corpus):
    """ Takes a corpus and trains your language model. 
        Compute any counts or other corpus statistics in this function.
    """  
    # TODO your code here
    for sentence in corpus.corpus:
      for datum in sentence.data:
        token = datum.word
        self.unigramCounts[token] = self.unigramCounts[token] + 1
        self.total += 1

    token0 = 'chutiya'
    for sentence in corpus.corpus:
        for datum in sentence.data:
            token1 = datum.word
            if token0 != 'chutiya':
                self.bigramCounts[token0][token1] = self.bigramCounts[token0][token1] + 1
            token0 = token1





  def score(self, sentence):
    """ Takes a list of strings as argument and returns the log-probability of the 
        sentence using your language model. Use whatever data you computed in train() here.
    """

    # TODO your code here
    t0 = ''
    score = 0.0
    flag = 0
    # tot = 0
    for token in sentence:
        t1 = token
        if flag is 0:
            count = self.unigramCounts[token]
            x = (count + 1) / (self.total + len(self.unigramCounts))
        else:
            # for tok in self.bigramCounts[t0]:
            #     tot = tot + self.bigramCounts[t0][tok]
            tot = self.unigramCounts[t0]
            count = self.bigramCounts[t0][t1]
            x = (count + 1) / (tot + self.total)
        flag = 1
        t0 = t1
        # tot = 0
        score += math.log(x)

    return score
