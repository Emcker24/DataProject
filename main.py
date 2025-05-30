import pandas as pd
def process_sales_data(costumers_path, orders_path, items_path):
    """
    Procesa los datos para generar un reporte mensual de ingresos y clientes unicos
    """
    # 1. Leer los archivos CSV
    try:
        custromers_df = pd.read_csv(costumers_path)
        orders_df = pd.read_csv(orders_path)    
        order_items_df = pd.read_csv(items_path)
    except FileNotFoundError as e:
        print(f"Error: {e}. Archivo no encontrado.")
        return None
    print("Archivos leídos correctamente.")
    print("- - - Muestra de los datos originales - - -")
    print("Customers head: \n", custromers_df.head(2))
    print("Orders head: \n", orders_df.head(2))
    print("Order Items head: \n", order_items_df.head(2))
    print("-----------------------------------------------\n")

    # 2. Limpiar y validar los datos 

    # Convertir los 