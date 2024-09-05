"""
    Input: tuples_list is an unsorted list of tuples denoting intervals
    Output: a list of merged tuples sorted by the lower number of the
    interval
"""
import sys


def merge_tuples (tuples_list):
    """Merge the tuples"""

    sorted_tuples = sorted(tuples_list)
    return sorted_tuples



def sort_by_interval_size (tuples_list):
    """
    Input: tuples_list is a list of tuples of denoting intervals
    Output: a list of tuples sorted by ascending order of the
    size of the interval if two intervals have the size then it will sort by the
    lower number in the interval
    """

    interval_sorted_list = sorted(tuples_list, key = lambda x: abs(x[1] - x[0]))
    return interval_sorted_list



def main():
    """
    Open file intervals.in and read the data and create a list of tuples
    """
    sys.stdin.readline()

    tup_list = []
    tup_list = sys.stdin.readlines()

    tuples_list = []
    for m_tuple in tup_list:
        tup = m_tuple.split()
        tuples_list.append(tuple((int(tup[0]), int(tup[1]))))

    # merge the list of tuples
    merged = merge_tuples(tuples_list)

    # sort the list of tuples according to the size of the interval
    sorted_merge = sort_by_interval_size(merge_tuples(tuples_list))

    # write the output list of tuples from the two functions
    print(merged)
    print(sorted_merge)

if __name__ == "__main__":
    main()
