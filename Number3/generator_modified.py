"""
Program: generator.py
Author: Ken
Generates and displays sentences using a simple grammar
and vocabulary.  Words are chosen at random.
"""
    ### nouns.txt, verbs. txt, articles.txt, and prepositions.txt
import random

def getWords(filename):
  """Reads words from a file and returns a tuple of word lists."""
  word_list = []
  with open(filename, "r") as f:
    for line in f:
      word_list.extend(line.strip().split())
  return tuple(word_list)

def sentence(noun_tuple, verbs_tuple, prepositions_tuple, articles_tuple):
    """Builds and returns a sentence."""
    return nounPhrase(articles_tuple, noun_tuple) + " " + verbPhrase(noun_tuple, verbs_tuple, prepositions_tuple, articles_tuple)

def nounPhrase(articles_tuple, nouns_tuple):
    """Builds and returns a noun phrase."""
    return random.choice(articles_tuple) + " " + random.choice(nouns_tuple)

def verbPhrase(nouns_tuple, verbs_tuple, prepositions_tuple, articles_tuple):
    """Builds and returns a verb phrase."""
    return random.choice(verbs_tuple) + " " + nounPhrase(articles_tuple, nouns_tuple) + " " + \
           prepositionalPhrase(prepositions_tuple,articles_tuple, nouns_tuple)

def prepositionalPhrase(prepositions,articles_tuple, noun_tuple):
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase(articles_tuple, noun_tuple)

def main():
    """Allows the user to input the number of sentences
    to generate."""
    noun_tuple = getWords("nouns.txt")
    verbs_tuple = getWords("verbs.txt")
    prepositions_tuple = getWords("prepositions.txt")
    articles_tuple = getWords("articles.txt")
    print(sentence(noun_tuple, verbs_tuple, prepositions_tuple, articles_tuple))


# The entry point for program execution
if __name__ == "__main__":
    main()

