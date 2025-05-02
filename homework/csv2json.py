"""Script para convertir un archivo CSV a JSON"""

import csv
import json

# Importamos NiceGUI para hacer una simple interfaz gráfica
from nicegui import ui

# Define la función que se ejecutará para hacer la conversión
def convert_csv_2_json(input_file):
    """Converts a CSV file to a JSON file"""

    # Toma el nombre del archivo CSV y lo convierte a JSON
    output_file = input_file.replace(".csv", ".json")
    data = []

    # Abre el archivo CSV en modo lectura
    with open(input_file, "r", encoding="utf-8") as f:
        # Usa DictReder para convertir el CSV en un iterable DictReader de diccionarios
        # donde cada fila del csv es un diccionario y las claves son los
        # nombres de las columnas, mientras que los valores son los valores
        # de cada fila para esa columna.
        reader = csv.DictReader(f)
        for row in reader:
            # Itera sobre cada fila del iterable reader y las almacena en una lista
            # de diccionarios.
            data.append(row)

    # Abre el archivo JSON que se creó al principio en modo escritura.
    with open(output_file, "w", encoding="utf-8") as f:
        # Pasa la lista data al archivo JSON usando el método dump de la librería json.
        # El argumento indent=4 hace que el archivo JSON sea más legible.
        json.dump(data, f, indent=4)

    # Notifica en la interfaz gráfica que la conversión se ha realizado
    # correctamente.
    ui.notify("The file was transformed successfully!")

# La función app crea la interfaz gráfica
def app():
    # Crea un label con el estilo de classes
    ui.label("CSV to JSON Converter").classes("text-4xl font-bold")
    ui.label("")

    # Crea un input para el nombre del archivo CSV
    filename = ui.input(
        label="CSV file to convert:",
        placeholder="filename",
    )
    ui.label("")
    ui.label("")

    # Crea el botón que llama a la función convert_csv_2_json
    # y le pasa el nombre del archivo CSV como argumento.
    ui.button(
        "Convert", 
        on_click=lambda: convert_csv_2_json(filename.value),
    )
    # Ejecuta la función run para crear la interfaz gráfica
    ui.run()

# Hace la llamada a la función app, que contiene toda la especificación
# de la interfaz gráfica.
app()
convert_csv_2_json("files/drivers.csv")