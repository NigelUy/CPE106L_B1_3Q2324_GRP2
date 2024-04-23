def mode(words):
        """
        File: mode.py
        Prints the mode of a set of numbers in a file.
        """
        theDictionary = {}
        for word in words:
            number = theDictionary.get(word, None)
            if number == None:
                # word entered for the first time
                theDictionary[word] = 1
            else:
                # word already seen, increment its number
                theDictionary[word] = number + 1

        # Find the mode by obtaining the maximum value
        # in the dictionary and determining its key
        theMaximum = max(theDictionary.values())
        for key in theDictionary:
            if theDictionary[key] == theMaximum:
                print("The mode is", key)
                break
def median(numbers):
  """
  File: median.py
  Prints the median of a set of numbers in a file.
  """

  midpoint = len(numbers) // 2
  print("The median is", end=" ")
  if len(numbers) % 2 == 1:
    print(numbers[midpoint])
  else:
    print((numbers[midpoint] + numbers[midpoint - 1]) / 2)

def mean(numbers):
    print("The mean is ", end="")
    print((sum(numbers))/len(numbers))
def main():
    numbers = []
    # Input the text, convert it to numbers, and
    # add the numbers to a list
    with open('testfile.txt', 'r') as f: 
        for line in f:
            words = line.split()
            for word in words:
                numbers.append(float(word))
    numbers.sort()
    median(numbers)
    mode(numbers)
    mean(numbers)

main()
