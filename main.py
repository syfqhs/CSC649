# CSC649: My first Python experiment

sentence = input("Enter a sentence: ")

if sentence.strip() == "":
    print("You did not enter a sentence.")
else:
    word_count = len(sentence.split())
    character_count = len(sentence)

    print("\n--- Sentence Analysis ---")
    print("Sentence:", sentence)
    print("Word count:", word_count)
    print("Character count:", character_count)

    if word_count <= 3:
        print("Sentence type: Short")
    else:
        print("Sentence type: Long")

    print("\nThank you for using the sentence counter!")