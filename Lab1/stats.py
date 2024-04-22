###median mode mean
import statistics

def median(numbers):
    return statistics.median(numbers)

def mean(numbers):
    return statistics.mean(numbers)

def mode(numbers):
    num_dict = {}
    modes = []
    for number in numbers:
        if number not in num_dict.keys():
            num_dict[number] = 0
        else:
            num_dict[number] += 1
    x =  max(num_dict.values())
    for key, values in num_dict.items():
        if values == x:
            modes.append(key)
    print("Mode = ", end ="")
    for _ in modes:
        print(_)
        



def main():
    num = []
    print("INPUT ANY LETTER TO EXIT")
    while True:
        x = input("Numbers chosen: ")
        if x.isdigit():
            num.append(int(x))
        else:
            break

    if num:  # Check if the list is not empty
            medians = median(num)
            means = mean(num)
            print(f"Median = {medians}")
            print(f"Mean = {means}")
            mode(num)

    else:
        print("No Median")
        print("No Mean")
        print("No Mode")

if __name__ == "__main__":
    main()