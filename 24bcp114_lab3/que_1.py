def count_vowels(string):
  vowels = "aeiouAEIOU"
  count = 0
  for char in string:
    if char in vowels:
      count += 1
  return count
str = input("Enter a string: ")
vowel_count = count_vowels(str)
print(vowel_count)
