from logo import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text, shift, direction):
    uppercase_indices = [i for i, char in enumerate(text) if char.isupper()]

    if direction == "decode":
        shift *= -1

    m = ""
    text = text.lower()
    for i in range(len(text)):
        if text[i] in alphabet:
            n = (alphabet.index(text[i]) + shift) % len(alphabet)
            m += alphabet[n]
        else:
            m += text[i]

    m = list(m)
    for index in uppercase_indices:
        m[index] = m[index].upper()

    joined_m = "".join(m)

    if direction == "decode":
        print(f"Plain text after being decoded: {joined_m}")
    else:
        print(f"Plain text after being encoded: {joined_m}")


print(logo)
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    while direction != 'encode' and direction != 'decode':
        print("Please just input encode or decode")
        direction = input(
            "Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    userInput = input(
        "Do you want to continue? If yes, type 'yes'. If no, type 'no': ").lower()
    if userInput != "yes":
        print("Goodbye!!!!")
        break
