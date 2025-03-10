def read_file(filename):
    """Reads a text file and returns the content as a string."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return ""

def clean_text(text):
    """Removes punctuation and converts text to lowercase."""
    # List of punctuation to remove
    punctuation = ",.?!'/\":;()[]{}-*<>"
    for p in punctuation:
        text = text.replace(p, "")
    return text.lower()

def get_unique_words(text):
    """Splits text into words and returns the set of unique words."""
    words = text.split()
    return set(words)  # Set keeps only unique values

def compare_books(file1, file2):
    """Compares the number of unique words in two books."""
    # Read and clean both books
    text1 = clean_text(read_file(file1))
    text2 = clean_text(read_file(file2))

    # Get unique words from both books
    unique_words1 = get_unique_words(text1)
    unique_words2 = get_unique_words(text2)

    # Print out the results
    print(f"Book 1 ('{file1}') has {len(unique_words1)} unique words.")
    print(f"Book 2 ('{file2}') has {len(unique_words2)} unique words.")

    # Compare the results
    if len(unique_words1) > len(unique_words2):
        print(f"The author of '{file1}' used more unique words.")
    elif len(unique_words1) < len(unique_words2):
        print(f"The author of '{file2}' used more unique words.")
    else:
        print("Both authors used the same number of unique words.")

# Call the function with the updated file names
compare_books("stf.txt", "sf.txt")
