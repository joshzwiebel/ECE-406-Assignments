#!/usr/bin/env python3
"""
Assignment #4, dynamic programming
"""
def cut_cloth(prices, rod_length):
    """
    Input: a list values[0 ... L], where value[i] contains value of a
    piece of length i, and values[0] = 0.  An integer L giving
    the total length of cloth.
    Output: a list pieces[0 ... L] and an integer K, where pieces[i]
    gives number of pieces of length i used in the solution, and K
    is the total value obtained.
    """
    memo = [0] * (rod_length + 1) # +1 for 0
    subcuts = [[] for _ in range(rod_length+1)]
    for i in range(rod_length+1):
        for j in range(i):
            with_cut = prices[i-j] + memo[j]
            without_cut = memo[i]

            if with_cut > without_cut:
                memo[i] = with_cut
                subcuts[i] = subcuts[j] + [i-j]
            else:
                memo[i] = without_cut


    num_cuts = [0] * (rod_length + 1)
    for i in subcuts[rod_length]:
        num_cuts[i] += 1

    return num_cuts,memo[rod_length]




def main():
    """
    Testing the cut_cloth function
    """
    # example in question where we use one piece of length 1
    # and one of length 3.
    if cut_cloth([0, 2, 3, 7, 7], 4) == ([0, 1, 0, 1, 0], 9):
        print("your output is correct for the example in the question")
    else:
        print("Something is wrong in your output format or algorithm")
    # second input example
    print(cut_cloth([0, 2, 3, 7, 7], 4))


if __name__ == '__main__':
    main()
    # print(cut_cloth([1, 5,8,9,10,17,17,20], 7))
