from tkinter import Tk, simpledialog, messagebox
#tKinter helps us have pop up boxes to let the user type things
def read_from_file():
    with open('super_hero_identities.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            superhero, identity = line.split('/')
            superhero = superhero.upper()
            identity = identity.upper()
            superheroes[superhero] = identity

def write_to_file(superhero,identity):
    with open('user_added_heros.txt','a')as file:
        file.write('\n'+ superhero + '/' + identity)
#This allows us to use super heros and identitys
print('Ask the Expert - Superhero Identities')
root = Tk()
root.withdraw()
superheroes = {}
#This allows python to read through a text document with information.
read_from_file()

while True:
    query_hero = simpledialog.askstring('Super Hero','Type the name of a super hero: ')
    query_hero = query_hero.upper()
#This is where the user types in a super hero for their identity
    if query_hero in superheroes:
        result = superheroes[query_hero]
        result = result.upper()
        messagebox.showinfo('Answer','The identity of ' + query_hero + ' is ' + result + '!')
#This gives the identity of the super hero
    else:
        new_identity = simpledialog.askstring('Teach Me',"I don't know. What is the identity of " + query_hero + '?')
        new_identity = new_identity.capitalize()
        superheroes[query_hero] = new_identity
        write_to_file(query_hero,new_identity)

root.mainloop()
#This lets the user to add new information to the text document.
