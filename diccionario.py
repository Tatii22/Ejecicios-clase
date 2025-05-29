score = (["BAJO", 0, 25], ["ACEPTABLE", 26, 50], ["SOBRESALIENTE", 51,80],["EXCELENTE",81,100])
#NOTA DEL 1 AL 100 PEDIR
#CALCULAR CUAL SERIA SU RANGO DE NOTA

def funcion(nota):
    for i, n in enumerate(score, start=1):
        if (nota >= n[1] and nota <= n[2]):
            print(f"La nota es {n[0]}")
            break

def promedios():
    mensaje = "Notas: \n"
    for i, n in enumerate (score,start=1):
        mensaje +=promedioNota(posicion=i,nombre=n[0], rango=n[1:]) + "\n"
        #mensaje += f"{i}.{n[1]} a {n[2]} -> {n[0]}\n"
    return mensaje

def promedioNota(posicion:int, nombre:str, rango:list):
    return f"{posicion}. {rango[0]} a {rango[1]} -> {nombre}"




nota = float(input("Ingrese nota de 1 al 100: "))
funcion(nota)
print=(promedios())

