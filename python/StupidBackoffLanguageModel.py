import math,collections

class StupidBackoffLanguageModel:

  def __init__(self, corpus):
    """Initialize your data structures in the constructor."""
    # TODO your code here
    self.bigramCounts = collections.defaultdict(lambda: collections.defaultdict(lambda: 0))
    self.unigramCounts = collections.defaultdict(lambda: 0)
    self.total = 0
    self.unnecessary_words = []
    # self.unnecessary_words =  ['<s>', '<\s>', 'and', 'is', 'are', 'in', 'the', '', '.', '?', ',', '!', ';', ':', 'this', 'here', 'there', 'where',
    #                      'why', 'who', 'what', 'when', 'that']
    self.train(corpus)


  def train(self, corpus):
    """ Takes a corpus and trains your language model.
        Compute any counts or other corpus statistics in this function.
    """
    # TODO your code here
    for sentence in corpus.corpus:
      for datum in sentence.data:
        token = datum.word
        if token not in self.unnecessary_words:
          self.unigramCounts[token] = self.unigramCounts[token] + 1
          self.total += 1

    token0 = 'chutiya'
    for sentence in corpus.corpus:
        for datum in sentence.data:
            token1 = datum.word
            if token0 != 'chutiya' and token1 not in self.unnecessary_words:
                self.bigramCounts[token0][token1] = self.bigramCounts[token0][token1] + 1
            token0 = token1

  def score(self, sentence):
    """ Takes a list of strings as argument and returns the log-probability of the
        sentence using your language model. Use whatever data you computed in train() here.
    """
    score = 0.0
    flag = 0
    t0 = ''
    for token in sentence:
      if token not in self.unnecessary_words:
        t1 = token
        if flag is 0:
            count = self.unigramCounts[token]
            x = (count) / (self.total)
        elif self.bigramCounts[t0][t1] is not 0:
            # for tok in self.bigramCounts[t0]:
            #     tot = tot + self.bigramCounts[t0][tok]
            tot = self.unigramCounts[t0]
            count = self.bigramCounts[t0][t1]
            x = (count)/(tot)
        elif self.unigramCounts[token] is not 0:
            count = self.unigramCounts[token]
            x = (count) / (self.total)
        else:
            count = self.unigramCounts[token]
            x = (count + 1) / (self.total + len(self.unigramCounts))
        flag = 1
        t0 = t1
        # tot = 0
        # print(x)
        score += math.log(x)

    return score
