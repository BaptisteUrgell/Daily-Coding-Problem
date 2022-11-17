import argparse

def valid_s(s: str, default_s: str) -> str:
    if s is None:
        return default_s
    return s

def get_args(default_args: dict):
    parser = argparse.ArgumentParser(description="Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).")

    parser.add_argument('--string', nargs='?', type=str, metavar='str', default=default_args['string'], help=f'String to transform into a palindrome. By default his param is equal to "{default_args["string"]}"')

    args = parser.parse_args()

    args.string = valid_s(args.string, default_args['string'])

    return args

def lcs(X: str, Y: str, l: int) :

    L = [[0 for i in range(l + 1)] for j in range(l + 1)]

    for i in range(l + 1) :	
        for j in range(l + 1) :	
            if (i == 0 or j == 0) :
                L[i][j] = l

            elif (X[i - 1] == Y[j - 1]) :
                L[i][j] = L[i - 1][j - 1] - 1
            else :
                L[i][j] = min(L[i - 1][j], L[i][j - 1])

    return L

def findInsertionsArray(string: str) -> list[list[int]]:
    l = len(string)
    charArray = list(string)
    charArray.reverse()
    revString = "".join(charArray)
    insertionArray = lcs(string, revString, l)
    return insertionArray

def reconstructPalindrome(insertions: list[list[int]], string: str) -> str:
    palindrome = ['.'] * (len(string) + insertions[-1][-1])

    i, j, k = 0, len(string) - 1, 0

    while i <= j:
        if string[i] == string[j]:
            palindrome[k], palindrome[-k-1] = string[i], string[j]
            i += 1
            j -= 1
        elif insertions[i+1][j] > insertions[i][j-1]:
            palindrome[k], palindrome[-k-1] = string[i], string[i]
            i += 1
        elif insertions[i+1][j] < insertions[i][j-1]:
            palindrome[k], palindrome[-k-1] = string[j], string[j]
            j -= 1
        elif string[i] < string[j]:
            palindrome[k], palindrome[-k-1] = string[i], string[i]
            i += 1
        else:
            palindrome[k], palindrome[-k-1] = string[j], string[j]
            j -= 1
        k += 1
    
    return "".join(palindrome)

def daily(string: str):
    insertions = findInsertionsArray(string)
    palindrome = reconstructPalindrome(insertions, string)
    
    print(palindrome)

if __name__ == "__main__":

    default_args = {
        "string" : "race"
    }

    args = get_args(default_args)
    daily(args.string)