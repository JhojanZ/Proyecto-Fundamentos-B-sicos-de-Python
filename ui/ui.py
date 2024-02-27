from tabulate import tabulate

def show_data(data):
    head = ['N° Dato', 'Ciudad de Ubicación', 'Edad', 'Tipo de Recurperación', 'Fuente de contagio', 'Estado', 'País viaje']
    
    print("\n\n", tabulate(data, headers=head, tablefmt='mixed_grid', showindex=True), sep="")

# heavy_grid, fancy_grid, mixed_grid
