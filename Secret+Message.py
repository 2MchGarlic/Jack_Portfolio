from tkinter import messagebox, simpledialog, Tk
from random import choice
def get_task():
    task= simpledialog.askstring('Task','Do you want to perform encryption or decryption? (Type encrypt or decrypt)')
    return task

def get_message():
    message = simpledialog.askstring('Secret Message','Enter the secret message')
    return message

def is_even(number):
    return number % 2 == 0

def get_even_letters(message):
    even_letters = []
    for counter in range(0, len(message)):
        if is_even(counter):
            even_letters.append(message[counter])
    return even_letters

def get_odd_letters(message):
    odd_letters = []
    for counter in range(0, len(message)):
        if not is_even(counter):
            odd_letters.append(message[counter])
    return odd_letters

def swap_letters(message):
    letter_list = []
    if not is_even(len(message)):
        message = message + 'x'
    even_letters = get_even_letters(message)
    odd_letters = get_odd_letters(message)
    for counter in range (0, int(len(message)/2)):
        letter_list.append(odd_letters[counter])
        letter_list.append(even_letters[counter])
    new_message = ' '.join(letter_list)
    return new_message

def encrypt(message):
    encrypted_list = []
    fake_letters = ['a','c','e','g','i','k','m','o','q','s','u','w','y']
    for counter in range(0, len(message)):
        encrypted_list.append(message[counter])
        encrypted_list.append(choice(fake_letters))
    new_message = ''.join(encrypted_list)
    swapped_message = swap_letters(new_message)
    encrypted_message = ''.join(reversed(swapped_message))
    return new_message

def decrypt(message):
    even_letters = get_even_letters(message)
    #unreversed_message = ''.join(reversed(even_letters))
    #decrypted_message = swap_letters(unreversed_message)
    new_message = ''.join(even_letters)
    return new_message

root = Tk()

while True:
    task = get_task()
    if task == 'encrypt':
        message = get_message()
        encrypted = encrypt(message)
        messagebox.showinfo('Ciphertext of the secret message is: ',encrypted)
    elif task == 'decrypt':
            message = get_message()
            decrypted = decrypt(message)
            messagebox.showinfo('Plaintext of the secret message is: ', decrypted)
    else:
        break

root.mainloop()

