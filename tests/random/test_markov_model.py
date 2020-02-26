from rbp.random.markov_model import MarkovModel


def test_markov_model():
    m = MarkovModel(k=2)
    m.fit(['ACCG', 'GAACAT', 'CTAGAAA', 'AGGCCCG', 'CAGATAC'])
    s = m.predict(10)
    assert len(s) == 10
