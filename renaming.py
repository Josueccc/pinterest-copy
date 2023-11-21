import os

def renombrar_archivos(directorio):
  """
  Renombra todos los archivos de un directorio con números consecutivos.

  Args:
    directorio: La ruta al directorio a renombrar.
  """

  # Obtenemos una lista de todos los archivos en el directorio.
  archivos = os.listdir(directorio)

  numero = 1

  for archivo in archivos:
    nuevo_nombre = str(numero) + ".jpg"
    os.rename(os.path.join(directorio, archivo), os.path.join(directorio, nuevo_nombre))

    numero += 1

if __name__ == "__main__":
  #Cambiando nombre a las imagenes
  directorio = "./img/" 
  renombrar_archivos(directorio)

