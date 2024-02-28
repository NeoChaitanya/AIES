import itertools

def solution(word1, word2, word3, result):
    letters = set(word1 + word2 + word3 + result)
    if len(letters) > 50:
        print("Invalid input: Too many unique letters.")
        return None

    digits = range(10)

    for perm in itertools.permutations(digits, len(letters)):
        sol = dict(zip(letters, perm))
        if sol[word1[0]] == 0 or sol[word2[0]] == 0 or sol[result[0]] == 0 or sol[word3[0]] == 0:
            continue

        num1 = int(''.join(str(sol[char]) for char in word1))
        num2 = int(''.join(str(sol[char]) for char in word2))
        num3 = int(''.join(str(sol[char]) for char in word3))
        result_num = int(''.join(str(sol[char]) for char in result))

        if num1 + num2 + num3 == result_num:
            print(f"\n\n\n  {word1}\n+ {word2}\n+ {word3}\n----------\n{result}")
            return num1, num2, num3, result_num

    print("No solution")
    return None

word1 = input("Enter the first word: ").upper()
word2 = input("Enter the second word: ").upper()
word3 = input("Enter the third word: ").upper()
result = input("Enter the result word: ").upper()

solution_result = solution(word1, word2, word3, result)

if solution_result is not None:
    print(f"{solution_result}")