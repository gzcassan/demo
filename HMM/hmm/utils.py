import  os

dict_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dict.txt')

def iter_dict():
    with open(dict_path, 'r', ) as f:
        for line in f:
            phrase, frequency, tag = line.split()
            yield phrase.decode('utf8'), int(frequency)
