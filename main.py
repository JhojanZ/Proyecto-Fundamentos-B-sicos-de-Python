from api.api import obtain_api
from ui.ui import show_data
from graficas.graficas import graficas
from limpieza.limpieza import limpiar_datos

def main():
    department = (input("Ingrese el departamento: ")).upper()
    registration_limits = int(input("Ingrese el número de registro: "))

    if registration_limits > 1000:
        print("Procesar más de mil datos podria provocar errores.", "¿Seguro que quieres proceder [S/N]?", sep="\n")
        proceder = input()
        
        if proceder.upper() != 'S':
            return 1
        

    api = obtain_api(registration_limits, department)
    limpiar_datos(api)
    show_data(api)

    respuesta = input("¿Quieres ver algunas graficas en base de estos datos? [S/N]\n")
    if(respuesta.upper() == 'S'):
        graficas(api)

    return 0


if __name__ == "__main__":
    main()