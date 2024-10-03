import numpy as np
from scipy.integrate import quad
from monte_carlo import monte_carlo_integration

limite_inferior = 2
limite_superior = 3

def integral(x):
    return (3 * x + 2) * (1/3) * np.log(16)

def main():

    resultado, error = quad(integral, limite_inferior, limite_superior)

    return resultado, error


if __name__ == '__main__':
    resultado, error = main()
    monte_carlo_result = monte_carlo_integration(integral,limite_inferior,limite_superior)
    print(f"El resultado de la integral es: {resultado}")
    print(f'el resultado con montecarlo es: {monte_carlo_result}')
    print(f"Error estimado: {error}")
