import random

# Función para calcular la exponenciación modular (base^exp % mod)
# Python tiene pow(base, exp, mod) que es muy eficiente.

def generar_claves(min_prime=1000, max_prime=5000):
    """
    Genera claves públicas y privadas simples para demostración.
    En un caso real, p debe ser un número primo muy grande (2048 bits).
    """
    # Lista de primos pequeños para el ejemplo
    primes = [i for i in range(min_prime, max_prime) if all(i % n != 0 for n in range(2, int(i**0.5) + 1))]
    
    p = random.choice(primes) # Primo grande
    g = random.randint(2, p-1) # Generador (simplificado para el ejemplo)
    x = random.randint(1, p-2) # Clave Privada (secreto)
    y = pow(g, x, p)           # Clave Pública
    
    # Retornamos la clave pública (p, g, y) y la privada (x)
    return (p, g, y), x

def cifrar(mensaje, public_key):
    p, g, y = public_key
    texto_cifrado = []
    
    print(f"\n--- Iniciando Cifrado ---")
    print(f"Mensaje original: {mensaje}")
    
    for char in mensaje:
        m = ord(char) # Convertir caracter a entero ASCII
        if m >= p:
            raise ValueError(f"El valor del caracter {m} es mayor que el módulo p {p}")
            
        k = random.randint(1, p-2) # Número aleatorio efímero por cada bloque
        
        # Fórmulas de ElGamal
        c1 = pow(g, k, p)
        c2 = (m * pow(y, k, p)) % p
        
        texto_cifrado.append((c1, c2))
        
    return texto_cifrado

def descifrar(texto_cifrado, private_key, p):
    x = private_key
    mensaje_descifrado = ""
    
    for c1, c2 in texto_cifrado:
        # Fórmula de descifrado: m = c2 * (c1^x)^-1 mod p
        
        # Paso 1: Calcular s = c1^x mod p
        s = pow(c1, x, p)
        
        # Paso 2: Calcular el inverso modular de s
        # Python 3.8+ permite pow(base, -1, mod) para el inverso modular
        s_inv = pow(s, -1, p)
        
        # Paso 3: Recuperar el mensaje m
        m = (c2 * s_inv) % p
        
        mensaje_descifrado += chr(m) # Convertir entero a caracter
        
    return mensaje_descifrado

# --- BLOQUE DE EJECUCIÓN PARA TUS 4 EJEMPLOS ---

def ejecutar_prueba(numero_ejemplo, mensaje_custom=None):
    print(f"\n{'='*10} EJEMPLO {numero_ejemplo} {'='*10}")
    
    # 1. Generar claves
    pub_key, priv_key = generar_claves()
    p, g, y = pub_key
    
    print(f"Clave Pública (p, g, y): {pub_key}")
    print(f"Clave Privada (x): {priv_key}")
    
    # 2. Definir mensaje
    if mensaje_custom:
        msg = mensaje_custom
    else:
        msg = f"Prueba {numero_ejemplo}"

    # 3. Cifrar
    cifrado = cifrar(msg, pub_key)
    print(f"Texto Cifrado (pares c1, c2): {cifrado}")
    
    # 4. Descifrar
    descifrado = descifrar(cifrado, priv_key, p)
    print(f"Texto Descifrado: {descifrado}")
    
    # Verificación
    if msg == descifrado:
        print(">> ESTADO: ÉXITO (El mensaje coincide)")
    else:
        print(">> ESTADO: ERROR")

# Ejecutar 4 ejemplos distintos
ejecutar_prueba(1,"años 2024")
ejecutar_prueba(2, "Python")
ejecutar_prueba(3, "Cripto 2025")
ejecutar_prueba(4, "Seguridad Informática")