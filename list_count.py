def count_occurrences(nums, target):
    count = 0
    for num in nums:
        if num == target:
            count += 1
    return(count)

# 以下のリストから目標値 7 の出現回数を数える例
# 以下のリストから目標値appleの出現回数を数える例
numbers = [7, 2, 7, 8, 7, 1, 5, 7]
words = ["apple", "peach", "apple", "Mos", "Mac", "apple"]
target_value = 2
target_word = "apple"
count_value = count_occurrences(numbers, target_value)
count_word = count_occurrences(words, target_word)
print(f"{target_value} の出現回数は: {count_value} 回")
print(f"{target_word} の出現回数は: {count_word} 回")