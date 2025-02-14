import numpy as np
import matplotlib.pyplot as plt

# Definir la función que va introducirse en
# el esquema del metodo de biseccion
def f(x):
    return np.cos(x)-x
# Algoritmo numerico del
# Método de Bisección
def biseccion(a, b, tol=1e-5, max_iter=100):
    if f(a) * f(b) >= 0:
        print("El método de bisección no es aplicable en el intervalo dado.")
        return None
    
    iteraciones = []
    errores_abs = []
    errores_rel = []
    errores_cua = []

    c_old = a  # Para calcular errores

    print("\nIteraciones del Método de Bisección:")
    print("Iter |       a       |       b       |       c       |      f(c)      |     Error Absoluto  | Error Relativo  | Error Cuadrático    ")
    print("-" * 85)

    for i in range(max_iter):
        c = (a + b) / 2
        iteraciones.append(c)
        
        error_abs = abs(c - c_old)
        error_rel= error_abs/c
        error_cua = error_abs**2
        errores_abs.append(error_abs)
        errores_rel.append(error_rel)
        errores_cua.append(error_cua)

        print(f"{i+1:4d} | {a:.8f} | {b:.8f} | {c:.8f} | {f(c):.8f} | {error_abs:.8e} | {error_rel:.8e} | {error_cua:.8e}")

        if abs(f(c)) < tol or error_abs < tol:
            break

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        
        c_old = c

    return iteraciones, errores_abs, errores_rel ,  errores_cua

# Parámetros iniciales
# se introduce el intervalo [a, b]
#a, b = 2, 3
#a, b = 0, 1.5
a, b = 0,1
iteraciones, errores_abs, errores_rel ,  errores_cua = biseccion(a, b)

# Crear la figura
fig, ax = plt.subplots(1, 2, figsize=(14, 5))

# Gráfica de la función y la convergencia de iteraciones
x = np.linspace(a - 1, b + 1, 400)
y = f(x)

ax[0].plot(x, y, label=r'$f(x) =cos(x)-x$', color='b')
ax[0].axhline(0, color='k', linestyle='--', linewidth=1)  # Línea en y=0
ax[0].scatter(iteraciones, [f(c) for c in iteraciones], color='red', label='Iteraciones')
ax[0].set_xlabel('x')
ax[0].set_ylabel('f(x)')
ax[0].set_title("Convergencia del Método de Bisección")
ax[0].legend()
ax[0].grid()

# Gráfica de convergencia del error
ax[1].plot(range(1, len(errores_abs)+1), errores_abs, marker='o', linestyle='-',label="Error Absoluto", color='r')
ax[1].plot(range(1, len(errores_rel)+1), errores_rel, marker='s', linestyle='-',label="Error Relativo", color='b')
ax[1].plot(range(1, len(errores_cua)+1), errores_cua, marker='^', linestyle='-',label="Error Cuadratico", color='g')
ax[1].set_yscale("log")  # Escala logarítmica
ax[1].set_xlabel("Iteración")
ax[1].set_ylabel("Error")
ax[1].set_title("En cada Iteración")
ax[1].grid()

ax[1].legend()  # Agrega la leyenda

# Guardar la figura
plt.savefig("biseccion_convergencia.png", dpi=300)
plt.show()