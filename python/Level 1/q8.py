def solution(nums):
    """t"""
    distinct_nums = set(nums)

    answer = min(len(distinct_nums), len(nums) / 2)
    return answer
