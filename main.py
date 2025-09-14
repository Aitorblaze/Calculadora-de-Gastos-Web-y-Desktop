import csv
import os

ARCHIVO_DATOS = "database.csv"

# Función para agregar registro (ingreso o gasto)
def agregar_registro(tipo):
    while True:
        try:
            monto = float(input(f"Introduce el monto del {tipo}: "))
            break
        except ValueError:
            print("Por favor, introduce un número válido.")
    
    descripcion = input("Descripción: ")
    
    archivo_existe = os.path.exists(ARCHIVO_DATOS)
    
    with open(ARCHIVO_DATOS, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not archivo_existe:
            writer.writerow(["tipo", "monto", "descripcion"])
        writer.writerow([tipo, monto, descripcion])
    
    print(f"{tipo.capitalize()} agregado correctamente!\n")

# Función para mostrar resumen
def ver_resumen():
    if not os.path.exists(ARCHIVO_DATOS):
        print("No hay registros aún.\n")
        return
    
    total_ingresos = 0
    total_gastos = 0
    
    with open(ARCHIVO_DATOS, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            monto = float(row["monto"])
            if row["tipo"] == "ingreso":
                total_ingresos += monto
            elif row["tipo"] == "gasto":
                total_gastos += monto
    
    saldo = total_ingresos - total_gastos
    print("===== Resumen =====")
    print(f"Total ingresos: {total_ingresos:.2f}")
    print(f"Total gastos:   {total_gastos:.2f}")
    print(f"Saldo actual:   {saldo:.2f}\n")

# Menú principal
def mostrar_menu():
    print("===== Calculadora de Gastos =====")
    print("1. Añadir ingreso")
    print("2. Añadir gasto")
    print("3. Ver resumen")
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_registro("ingreso")
        elif opcion == "2":
            agregar_registro("gasto")
        elif opcion == "3":
            ver_resumen()
        elif opcion == "4":
            print("¡Adiós!")
            break
        else:
            print("Opción no válida, intenta de nuevo.\n")

if __name__ == "__main__":
    main()
