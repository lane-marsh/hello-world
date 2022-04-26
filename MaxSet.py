# Author: Lane Marsh
# Date: 4/26/2022
# Description:  Given a list of numbers, return a subsequence of non-consecutive
#               numbers in the form of a list that would have the maximum sum.


def max_independent_set(nums):

    if len(nums) == 0:
        return []

    result = []

    arr_back_1 = []
    score_back_1 = 0
    arr_back_2 = []
    score_back_2 = 0
    arr_back_3 = []
    score_back_3 = 0

    for index, this_num in enumerate(nums):

        if this_num < 0:
            pass
        elif index == 0:
            arr_back_3.append(this_num)
            score_back_3 = this_num
            continue
        elif index == 1:
            arr_back_2.append(this_num)
            score_back_2 = this_num
            continue
        elif index == 2:
            if len(arr_back_3) < 1:
                arr_back_1.append(this_num)
                score_back_1 = this_num
            else:
                arr_back_1.append(arr_back_3[0])
                arr_back_1.append(this_num)
                score_back_1 = score_back_3 + this_num
            continue

        if this_num < 0:
            this_score = max(score_back_2, score_back_3)
            this_arr = arr_back_2.copy()
            continue
        elif score_back_2 > score_back_3:
            this_score = score_back_2 + this_num
            this_arr = arr_back_2.copy()
            this_arr.append(this_num)
        else:
            this_score = score_back_3 + this_num
            this_arr = arr_back_3.copy()
            this_arr.append(this_num)

        score_back_3 = score_back_2
        arr_back_3 = arr_back_2.copy()
        score_back_2 = score_back_1
        arr_back_2 = arr_back_1.copy()
        score_back_1 = this_score
        arr_back_1 = this_arr.copy()

    if score_back_3 > score_back_2 and score_back_3 > score_back_1:
        result = arr_back_3
    elif score_back_2 > score_back_1:
        result = arr_back_2
    else:
        result = arr_back_1

    return result


if __name__ == "__main__":

    test_set = [7, 2, 5, 8, 6, 18, -1, 2, 20, 4, 5, 6]
    print(max_independent_set(test_set))
    test_set = [-1, -2, -1, 5, -2, -1, -2, 5, 7]
    print(max_independent_set(test_set))
