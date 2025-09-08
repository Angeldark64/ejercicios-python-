def generar_subconjuntos(n):

    """
    Genera todos los subconjuntos de un conjunto de N elementos.
    """
    elementos = list(range(1, n + 1))  # Elementos del 1 a N elementos
    subconjuntos = []
    
    # 2^n subconjuntos posibles

    for i in range(2**n): #los doble ** significa potencia en python
        subconjunto = []
        # Convertir i a binario y usar cada bit para incluir/excluir elementos
        for j in range(n):
            if i & (1 << j):  # Si el bit j está activado
                
                subconjunto.append(elementos[j])
        subconjuntos.append(subconjunto)
    
    return subconjuntos

def mostrar_subconjuntos():
    """
    Función principal que maneja la entrada del usuario y muestra los resultados.
    """
    try:
        # Solicitar entrada del usuario
        entrada = input("Ingresa el número de elementos del conjunto: ")
        
        # Validar que sea un número entero
        n = int(entrada)
        
        # Validar que no sea negativo
        if n < 0:
            print(" Error: No se pueden generar subconjuntos con números negativos.")
            print("   Por favor, ingresa un número entero positivo.")
            return
        
        # Validar que no sea demasiado grande (esto se hace con el fin de evitar problemas de memoria)
        if n > 20:
            print(" Advertencia: Un conjunto de más de 20 elementos generará muchos subconjuntos.")
            continuar = input("¿Deseas continuar? (s/n): ").lower()
            if continuar != 's':
                return
        
        # Generar subconjuntos
        subconjuntos = generar_subconjuntos(n)
        
        # Mostrar resultados
        print(f"\n Conjunto original: {{{', '.join(map(str, range(1, n + 1)))}}}")
        print(f" Número total de subconjuntos: {len(subconjuntos)} (2^{n})")
        print("\n Lista de todos los subconjuntos:")
        print("=" * 50)
        
        for i, subconjunto in enumerate(subconjuntos, 1):
            if len(subconjunto) == 0:
                print(f"{i:2d}. ∅ (conjunto vacío)")
            else:
                print(f"{i:2d}. {{{', '.join(map(str, subconjunto))}}}")
        
        print("=" * 50)
        print(f" Total: {len(subconjuntos)} subconjuntos generados exitosamente.")
        
    except ValueError:
        print(" Error: Entrada inválida.")
        print("   Por favor, ingresa solo números enteros positivos.")
        print("   Ejemplos válidos: 1, 2, 3, 4, 5...")
        
    except Exception as e:
        print(f" Error inesperado: {e}")

# Función adicional para mostrar la fórmula matemática
def mostrar_teoria():
    """
    Explica la teoría detrás del cálculo de subconjuntos.
    """
    print("\n TEORÍA DE SUBCONJUNTOS")
    print("=" * 40)
    print("• Para un conjunto de n elementos:")
    print("• Número de subconjuntos = 2^n")
    print("• Esto incluye el conjunto vacío (∅) y el conjunto completo")
    print("\nEjemplos:")
    print("• n=0 → 2^0 = 1 subconjunto: {∅}")
    print("• n=1 → 2^1 = 2 subconjuntos: {∅, {1}}")
    print("• n=2 → 2^2 = 4 subconjuntos: {∅, {1}, {2}, {1,2}}")
    print("• n=3 → 2^3 = 8 subconjuntos")

if __name__ == "__main__":
    print(" GENERADOR DE SUBCONJUNTOS")
    print("=" * 40)
    
    while True:
        print("\nOpciones:")
        print("1. Generar subconjuntos")
        print("2. Ver teoría")
        print("3. Salir")
        
        opcion = input("\nElige una opción (1-3): ").strip()
        
        if opcion == "1":
            mostrar_subconjuntos()
        elif opcion == "2":
            mostrar_teoria()
        elif opcion == "3":
            print(" ¡Hasta luego")
            break
        else:
            print(" Opción inválida. Por favor, elige 1, 2 o 3.")

            
            

