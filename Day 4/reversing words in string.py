def reverse_individual_words_loop(s):
    words = s.split()
    reversed_words_list = []
    for word in words:
        reversed_word = ""
        for char in word:
            reversed_word = char + reversed_word
        reversed_words_list.append(reversed_word)
    return " ".join(reversed_words_list)

input_string = input("enter a sentence:")
print(f"Original: '{input_string}'")
print(f"Reversed: '{reverse_individual_words_loop(input_string)}'")