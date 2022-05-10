import string

# LCSubStr() (iterative implementation) obtained from:
# https://www.geeksforgeeks.org/longest-common-substring-dp-29/
# accessed on 3/10/22
# author: This code is contributed by Soumen Ghosh

# Python3 implementation of Finding
# Length of Longest Common Substring
# Returns length of longest common
# substring of X[0..m-1] and Y[0..n-1]


def LCSubStr(X, Y, m, n):
    # Create a table to store lengths of
    # longest common suffixes of substrings.
    # Note that LCSuff[i][j] contains the
    # length of longest common suffix of
    # X[0...i-1] and Y[0...j-1]. The first
    # row and first column entries have no
    # logical meaning, they are used only
    # for simplicity of the program.

    # LCSuff is the table with zero
    # value initially in each cell
    LCSuff = [[0 for k in range(n+1)] for l in range(m+1)]

    # To store the length of
    # longest common substring
    result = 0

    # Following steps to build
    # LCSuff[m+1][n+1] in bottom up fashion
    for i in range(m + 1):  # for i in the range of the length of X plus 1
        for j in range(n + 1):  # for j in the range of the length of Y plus one
            if i == 0 or j == 0:
                LCSuff[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                LCSuff[i][j] = LCSuff[i-1][j-1] + 1
                result = max(result, LCSuff[i][j])
            else:
                LCSuff[i][j] = 0
    return result

# This code is contributed by Soumen Ghosh

# A Dynamic Programming based Python program for edit
# distance problem

# checks each character in both strings and fills a table to say how
# many operations need to be performed at each change, if none needed, copy
# however many operations needed in the last step
# parameters are: first word, second word, length of first word, length of second word
def editDistDP(str1, str2, m, n):
    # Create a table to store results of subproblems
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]  # sets the first index of each string in the table to 0

    # Fill d[][] in bottom up manner
    for i in range(m + 1):
        for j in range(n + 1):

            # If first string is empty, only option is to
            # insert all characters of second string
            if i == 0:
                dp[i][j] = j  # Min. operations = j

            # If second string is empty, only option is to
            # remove all characters of second string
            elif j == 0:
                dp[i][j] = i  # Min. operations = i

            # If last characters are same, ignore last char
            # and recur for remaining string
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

            # If last character are different, consider all
            # possibilities and find minimum
            else:
                dp[i][j] = 1 + min(dp[i][j - 1],  # Insert
                                   dp[i - 1][j],  # Remove
                                   dp[i - 1][j - 1])  # Replace

    return dp[m][n]


# gets rid of caps, punctuation, and white space in a string
def clean_str(a_str):
    for p in string.punctuation:
        a_str = a_str.replace(p, "")
    return a_str.lower().split()
