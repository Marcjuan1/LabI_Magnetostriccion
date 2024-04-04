#Resolviendo la ecuación de Laplace método-relajación( Tarea 3 EM1 Uniandes)
#by : Juan Camilo Reales Crespo
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def laplace_relaxation(N, M, dx, dy, V0, tolerance=1e-5, max_iterations=10000):
    """
    Resuelve la ecuación de Laplace utilizando el método de relajación.

    Parámetros:
    - N (int): Número de puntos de la red en la dirección x.
    - M (int): Número de puntos de la red en la dirección y.
    - dx (float): Paso en la dirección x.
    - dy (float): Paso en la dirección y.
    - V0 (function): Función de condiciones de frontera V0(x, y).
    - tolerance (float, opcional): Tolerancia para la convergencia. Valor predeterminado es 1e-5.
    - max_iterations (int, opcional): Número máximo de iteraciones. Valor predeterminado es 10000.

    Retorna:
    - V (numpy.ndarray): Matriz 2D con la solución de la ecuación de Laplace.
    """
    # Inicialización de la matriz de potenciales V
    V = np.zeros((N, M))

    # Condiciones de frontera
    for i in range(N):
        V[i, 0] = V0(i*dx, 0)  # borde inferior
        V[i, -1] = V0(i*dx, b)  # borde superior
    for j in range(M):
        V[0, j] = V0(0, j*dy)  # borde izquierdo
        V[-1, j] = V0(a, j*dy)  # borde derecho

    # Iteraciones hasta convergencia
    for _ in range(max_iterations):
        V_old = V.copy()
        for i in range(1, N - 1):
            for j in range(1, M - 1):
                V[i, j] = 0.25 * (V_old[i+1, j] + V_old[i-1, j] + V_old[i, j+1] + V_old[i, j-1])

        # Comprobación de convergencia
        if np.max(np.abs(V - V_old)) < tolerance:
            break

    return V

def V0(x, y):
    """
    Define las condiciones de frontera V0(x, y).

    Parámetros:
    - x (float): Coordenada en x.
    - y (float): Coordenada en y.

    Retorna:
    - float: Valor del potencial en el punto (x, y).
    """
    if x == 0 or x == a:
        return 0
    elif y == 0:
        return -v0
    elif y == b:
        return v0
    else:
        return 0 #para puntos dentro del dominio D

if __name__ == "__main__":
    # Parámetros del problema
    N = int(input("Ingrese el número de puntos de la red en la dirección x (N): "))
    M = int(input("Ingrese el número de puntos de la red en la dirección y (M): "))
    dx = float(input("Ingrese el paso en la dirección x: "))
    dy = float(input("Ingrese el paso en la dirección y: "))
    a = N * dx  # longitud en x
    b = M * dy  # longitud en y
    v0 = float(input("Ingrese el valor de V0: "))

    # Resolución del problema
    V = laplace_relaxation(N, M, dx, dy, V0)
    print(V)

    # Calcular el promedio de los potenciales en toda la malla
    promedio_potencial = np.mean(V)
    print("El valor final del potencial promedio es:", promedio_potencial)

    x = np.linspace(0, a, N)
    y = np.linspace(0, b, M)
    X, Y = np.meshgrid(x, y)

    plt.contourf(X, Y, V, cmap='coolwarm')
    plt.colorbar()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Solución ec. Laplace Método de relajación (2D)')
    plt.show()



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, V, cmap='coolwarm')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('V')
ax.set_title('Solución ec. Laplace Método de relajación (3D)')
plt.show()
