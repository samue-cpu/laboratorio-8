#################################
#ejercicio 2 calculdora
#################################
def sumar(a, b):
  return a + b
def restar(a, b):
  return a - b
def multiplicar(a, b):
  return a * b
def dividir(a, b):
  if b == 0:
    return "No se puede dividir entre cero."
  else:
    return a / b

def calculadora():
  try:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    operacion = input("Ingresa la operación (+, -, *, /): ")

    if operacion == "+":
      resultado = sumar(num1, num2)
    elif operacion == "-":
      resultado = restar(num1, num2)
    elif operacion == "*":
      resultado = multiplicar(num1, num2)
    elif operacion == "/":
      resultado = dividir(num1, num2)
    else:
      print("Operación inválida.")
      return

    print(f"El resultado es: {resultado}")

  except ValueError:
    print("Entrada inválida. Por favor, ingresa números válidos.")

if __name__ == "__main__":
  calculadora()
  ##################################3
  #ejercicio 3 generar contraseña
  ####################################3
  
  import random
import string

def generar_contraseña(longitud, mayusculas=True, minusculas=True, numeros=True, especiales=True):
  """Genera una contraseña aleatoria."""

  caracteres = []
  if mayusculas:
    caracteres.extend(string.ascii_uppercase)
  if minusculas:
    caracteres.extend(string.ascii_lowercase)
  if numeros:
    caracteres.extend(string.digits)
  if especiales:
    caracteres.extend(string.punctuation)

  if not caracteres:
    raise ValueError("Al menos un tipo de carácter debe estar habilitado.")

  contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
  return contraseña

if __name__ == "__main__":
  try:
    longitud = int(input("Ingresa la longitud de la contraseña: "))
    contraseña = generar_contraseña(longitud, mayusculas=True, minusculas=True, numeros=True, especiales=True)
    print(f"Contraseña generada: {contraseña}")
  except ValueError as e:
    print(f"Error: {e}")