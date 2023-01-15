# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

# TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
# e.g.
# plain_text = "hello"
# shift = 5
# cipher_text = "mjqqt"
# print output: "The encoded text is mjqqt"

##HINT: How do you get the index of an item in a list:
# https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

direction = input("Enter 'encode' for encryption and 'decode' for decryption: \n")

text = input("Type your message: \n").lower()  # dog

shift = int(input("Type the shift number: \n")) % 26

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def cipher(user_direction, user_text, shift_number):
    if user_direction == 'encode':
        encrypt(user_text, shift_number)
    elif user_direction == 'decode':
        decrypt(user_text, shift_number)


def encrypt(user_text, shift_number):
    encoded_list = []
    encoded_string = ''
    for i in user_text:  # vish
        encoded_list.append(alphabet[alphabet.index(i) + int(shift_number)])
        encoded_string += alphabet[alphabet.index(i) + int(shift_number)]
    print(''.join(encoded_list))


def decrypt(user_text, shift_number):
    decoded_list = []
    for i in user_text:  # vish
        decoded_list.append(alphabet[alphabet.index(i) - int(shift_number)])
    print(''.join(decoded_list))


cipher(direction, text, shift)
