import string
import random

def generate_password(length=8, include_numbers=True, include_special_chars=True, include_uppercase=True):
    """
    Genera una contraseña segura.

    :param length: Longitud de la contraseña. Por defecto es 8.
    :param include_numbers: Incluir números en la contraseña. Por defecto es True.
    :param include_special_chars: Incluir caracteres especiales. Por defecto es True.
    :param include_uppercase: Incluir mayúsculas. Por defecto es True.
    :return: La contraseña generada como una cadena.
    """
    # Definir los bloques de construcción de la contraseña
    letters = string.ascii_lowercase
    numbers = string.digits if include_numbers else ''
    special_chars = string.punctuation if include_special_chars else ''
    uppercase = string.ascii_uppercase if include_uppercase else ''

    # Combinar todos los posibles caracteres
    possible_chars = letters + numbers + special_chars + uppercase

    # Generar la contraseña
    password = ''.join(random.choice(possible_chars) for _ in range(length))

    return password

# Interacción con el usuario
if __name__ == "__main__":
    length = int(input("Longitud de la contraseña (por defecto 8): ") or 8)
    include_numbers = input("Incluir números? (S/n): ").lower() != 'n'
    include_special_chars = input("Incluir caracteres especiales? (S/n): ").lower() != 'n'
    include_uppercase = input("Incluir mayúsculas? (S/n): ").lower() != 'n'

    password = generate_password(length, include_numbers, include_special_chars, include_uppercase)
    print(f"Tu nueva contraseña es: {password}")
