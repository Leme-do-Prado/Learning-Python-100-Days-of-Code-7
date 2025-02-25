import string

print("Hi! Welcome to Caesar Cypher! \n This program encrypts and decrypts based on the ancient Caesar cypher method.\n"
      "Let's start!")

message_to_be_coded = list(input("What is the message?\n").lower())
shift_number = int(input("What is the shift number?\n"))
choice = int(input("Do you wish to encrypt or decrypt?\n Type 0 for encryption, 1 for decryption.\n"))
alphabet = list(string.ascii_lowercase)

def encrypt(content, number):
    i = 0
    for letter in content:
        content[i]=alphabet[alphabet.index(content[i])+number]
        i+=1
    print("".join(content))

def decrypt(content, number):
    i = 0
    for letter in content:
        content[i]=alphabet[alphabet.index(content[i])-number]
        i+=1
    print("".join(content))

choice_continue=1
while choice_continue!=0:
    if choice == 0:
        encrypt(message_to_be_coded, shift_number)
    elif choice == 1:
        decrypt(message_to_be_coded, shift_number)
    choice_continue = int(input("Do you wish to continue encrypting?\n Type 0 to end program, anything else to continue.\n"))

if choice_continue==0:
    print("Thanks for using the Caesar Cypher program! :)")
