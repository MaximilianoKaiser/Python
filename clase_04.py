user_first_name = input("Hola! como te llamás? (Solo tu primer nombre)")
# es importante para el próximo paso el strip de espacios, \t y \n 
user_first_name = user_first_name.strip() 

# este while se fija que el nombre tenga 3 letras o más
# y vuelve al input
while len(user_first_name) < 3:
    user_first_name = input("Tu nombre tiene que tener más de 2 letras")
    user_first_name = user_first_name.strip()

#normalización de datos luego del loop
user_first_name = user_first_name.lower()
user_first_name = user_first_name.title()

#greeting
print (user_first_name,", que lindo nombre!")

#mismo que first name

user_last_name = input("Y cual es tu apellido?")
user_last_name = user_last_name.strip()
while len(user_last_name) < 3:
    user_last_name = input ("Tu apellido no puede tener menos de 3 letras")
    user_last_name = user_last_name.strip()

user_last_name = user_last_name.lower()
user_last_name = user_last_name.title()


print (f"Un gusto {user_first_name} {user_last_name}, mi nombre es Botty \n y estoy acá para ayudarte")
user_full_name = user_first_name + " " + user_last_name



user_age = input("Podrías decirme cuántos años tenés? ")
user_age = user_age.strip()
while not user_age.isdigit():
    user_age = input("Podrías decirme cuántos años tenés usando solo números? ")
    user_age = user_age.strip()

user_age = int(user_age)

if user_age < 15:
        print(f"{user_age} años, te clasificamos como un niño, bienvenido al sitio {user_full_name}")
elif user_age <= 18:
     print (f"{user_age} años, te clasificamos como adolescente {user_first_name}, disfrutá el sitio")
elif user_age > 18:
     print (f"{user_age} años te clasifica como adulto, disfrutá el sitio en su totalidad!")

user_email = input (f"Por ultimo, {user_first_name}, te pido un mail")
user_email = user_email.strip()

while user_email.find(".com") == -1 or len(user_email) < 5 or user_email.count("@") != 1 or user_email.find(" ") != -1:
     user_email = input (f"{user_first_name}, tu mail parece que no es válido, revisalo por favor")
     user_email = user_email.strip()
     

