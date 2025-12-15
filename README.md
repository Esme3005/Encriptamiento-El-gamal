### 🔐 Cifrado y Descifrado de Mensajes con el Algoritmo ElGamal en Python

Este proyecto implementa una versión educativa y simplificada del algoritmo criptográfico ElGamal, utilizando Python para demostrar los procesos de generación de claves, cifrado y descifrado de mensajes.
+ **El objetivo es comprender el funcionamiento de la criptografía de clave pública.**

+ **Se emplea exponenciación modular para garantizar seguridad matemática.**

+ **El proyecto está enfocado en fines académicos y de aprendizaje.**

### Características
+ **Generación de claves (ElGamal)**

+ **Generación de un número primo p dentro de un rango definido.**

+ **Selección de un generador g y una clave privada x.**

+ **Cálculo de la clave pública y = g^x mod p.**

+ **Separación clara entre clave pública y clave privada.**

+ **Cifrado de mensajes**

+ **Conversión de caracteres a valores ASCII.**

+ **Uso de un valor aleatorio efímero k por cada carácter.**

+ **Aplicación de las fórmulas del algoritmo ElGamal.**

+ **El mensaje cifrado se almacena como pares (c1, c2).**

+ **Descifrado de mensajes**

+ **Cálculo del secreto compartido s = c1^x mod p.**

+ **Uso del inverso modular para recuperar el mensaje original.**

+ **Reconversión de valores numéricos a caracteres.**

+ **Verificación automática de la integridad del mensaje.**

### Tecnologías utilizadas 💻

+ **Python 3**

+ **Random: Generación de valores aleatorios.**

+ **Exponenciación modular: Uso eficiente de pow(base, exp, mod).**

+ **Criptografía de clave pública: Implementación del algoritmo ElGamal.**

### Funcionamiento general

+ **Se generan claves públicas y privadas automáticamente.**

+ **El usuario define un mensaje a cifrar.**

+ **Cada carácter del mensaje es cifrado individualmente.**

+ **El mensaje cifrado es descifrado usando la clave privada.**

+ **Se valida que el mensaje original y el descifrado coincidan.**

### Aplicaciones

+ **Proyectos escolares y universitarios.**

+ **Introducción a la criptografía y seguridad informática.**

+ **Demostraciones educativas de algoritmos criptográficos.**

+ **Comprensión de sistemas de cifrado de clave pública.**

### 📞 Contacto 👩🏻‍💻

+ **WhatsApp: +52 7491148***

+ **Instagram: @esme.blossom.xo**
