from random import choice
import sys


def multiplyNums(a, b):
    odds = [0, 0, 1] # 0: correct result, 1: incorrect result
    result = a*b
    
    accurate = choice(odds) # Chooses a random value from the list of odds

    if choice(odds) == 0: # Return the correct result
        return result
    else:                 # Return an incorrect result
        return result-1


def main():
    if len(sys.argv) != 2:
        raise Exception("Command to run: python3 chernoff.py <number_of_trials>")

    total_trials = int(sys.argv[1])
    num_correct = 0
    num_incorrect = 0

    num1 = 4
    num2 = 5
    expected_result = num1*num2

    for i in range(total_trials):
        # Determine whether the probabilistic algorithm returned the correct result
        if multiplyNums(num1, num2) == expected_result:
            num_correct += 1
        else:
            num_incorrect += 1

    print(f'\nTotal Trials:       {total_trials}')
    print(f'Correct Results:    {num_correct}')
    print(f'Incorrect Results:  {num_incorrect}\n')
    print(f'Probability of being correct: {round(num_correct / total_trials * 100, 2)}%\n')

if __name__ == "__main__":
    main()
