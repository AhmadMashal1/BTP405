def wordCount(file_path):
    word_dict = {}

    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            words = line.strip().split()

            for word in words:
                word = word.lower()  # Convert to lowercase
                if word not in word_dict:
                    word_dict[word] = [line_number]
                else:
                    word_dict[word].append(line_number)

    return word_dict


file_path = 'q3_data.txt'  # sample data for q3 wordcount function 
result = wordCount(file_path)

# Print the result
for word, line_numbers in result.items():
    print(f"{word}: {line_numbers}")

