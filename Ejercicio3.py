edad = int(input("Bienvenido al Bar Baro, por favor, indique su edad: "))

if edad < 18:
    print("Aún te quedan " , (18 - edad), "años para poder entrar. Vete a casa a jugar a los Pokémon")

elif edad < 25 and edad >= 18:
    print("Puedes pasar, pero aún te faltan ", (25 - edad), "años para poder consumir alcohol, drogas o señoras de la vida.")

elif edad >= 25:
    print("Disfruta del Bar Baro y ponte hasta las cejas.")