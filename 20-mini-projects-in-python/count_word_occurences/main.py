from collections import OrderedDict

# opening the file in read mode
my_file = open(
    "20-mini-projects-in-python/count_word_occurences/file.txt", "r")

# SOLUTION 1: file content into a list

file_content_into_list = []
for line in my_file:
    file_content_into_list += line.strip().replace('.', '').split(' ')
    # print(f'{line}')

# SOLUTION 2: file content into a list

# reading the file content
# file_content = my_file.read()

# replacing end of line('/n') with ' ', '.' with '' and
# splitting the text it further when '.' is seen.

# file_content_into_list = file_content.strip().replace(
#     '\n', ' ').replace('.', '').split(' ')

# print(file_content_into_list)  # display the list

# empty dictionary
word_counter = {}

print("\n\n")

for word in file_content_into_list:
    # counting unique words
    word_to_lower = word.lower()
    # print(word_to_lower) # print each word
    word_counter[word_to_lower] = word_counter.get(word_to_lower, 0) + 1

# print the dictionary containint the different words as keys
# and occurences as values
# print(word_counter)

# create a sorted dict by keys
sorted_dict = OrderedDict(sorted(word_counter.items()))

for word, value in sorted_dict.items():
    print("{}: {}".format(word, value))  # print words and occurences

# close the file descriptor
my_file.close()
