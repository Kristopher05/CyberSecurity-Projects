# Method to count the amount of each letter in the ciphertext
def letter_count(ciphertext):
    # Array that holds the count of each letter
    counts = {}
    
    # Loops through each character in the ciphertext and updates the count
    for char in ciphertext:
        if char.isalpha():
            char = char.lower()
            counts[char] = counts.get(char, 0) + 1

    return counts

def decrypt(ciphertext, key):
    plaintext = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    substitution_key = {}

    # Map each letter in the key to a corresponding letter in the alphabet
    for i, char in enumerate(key):
        if char.isalpha():
            substitution_key[char] = alphabet[i]
    
    # Use the substitution key to decrypt the ciphertext
    for char in ciphertext:
        if char in substitution_key:
            plaintext += substitution_key[char]
        else:
            plaintext += char

    return plaintext

if __name__ == "__main__":
    ciphertext = input("Enter ciphertext: ")
    letter_count = letter_count(ciphertext)

    print("\nLetter Frequency:")
    for letter, count in sorted(letter_count.items()):
        print(f"{letter}: {count}")

    guess = input("Enter a key: ")
    plaintext = decrypt(ciphertext, guess)
    print(f"\nDecrypted Text: {plaintext}")
