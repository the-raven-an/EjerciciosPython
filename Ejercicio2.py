nombre = input("Estimado alumno, escriba su nombre: ")
nota1 = float(input("Introduzca la nota de su primer exámen: "))
nota2 = float(input("Introduzca la nota de su segundo exámen: "))
nota3 = float(input("Introduzca la nota de su tercer exámen: "))
nota4 = float(input("Introduzca la nota de su cuarto exámen: "))

media = (nota1 + nota2 + nota3 + nota4)/4

print("Estimado", nombre, ", su nota media es", round(media,2))