# -*- coding: utf-8 -*-
"""SoyCalidadTest.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18EVHxzviZ_kK_aw82YIEA6iE4z8IzAs2

##Ejercicio 2:
Se desea desarrollar un prototipo del software empotrado de una máquina
expendedora de café. La interacción con el usuario será a través de consola.
La máquina dispone de un tanque de agua, un depósito de azúcar y un
cargador de cartuchos de café.
El menú del prototipo tiene opciones para la selección de cada producto y opciones
de gestión.
Tras la selección de cualquier producto se presenta un submenú para la selección
del azúcar: nada; poco; medio; mucho; muchísimo.

#####Importante:
Tras la venta de cualquier producto, la máquina verifica los niveles de los
dispositivos (tanque de agua, depósito de azúcar y cargador de cartuchos de café).
Si cualquiera de estos dispositivos queda por debajo de su umbral mínimo de
operación, se desactivarán todas las opciones de productos, impidiendo nuevas
selecciones hasta que se recargue el recurso correspondiente.
"""

import os, sys
from google.colab import output

def clear_console():
  if os.name == 'nt':
    os.system('cls')
    output.clear()
  else:
    os.system('clear')
    output.clear()


############################# NIVELES################################
# no se detalla como ingresar nuevos valores en el documento
# se puede editar manualmente para la prueba de los límites
product_levels = {
    "water":1000,
    "coffe":10,
    "suggar":500
}
#############################################################

list_coffe = {"1":"Espresso", "2":"Capuccino", "3":"Mocaccino"}
list_suggar ={1:"sin", 2:"poca", 3:"media", 4:"mucha", 5:"muchisima"}
product_selected = "" #tipo de cafe, no se detalla, pero igual se coloca para diferenciar el producto

def read_option(menu,n):
  #print("n: ", n)
  while ( int(a := input("Opción [{}, {}]:".format("1",n)))  not in range(n+1) ) :
    print('Opción incorrecta, vuelva a intentarlo.')
  return int(a)

def espresso():
  global product_selected
  product_selected = "1"
  sel_sugar()

def capuchino():
  global product_selected
  product_selected = "2"
  sel_sugar()

def mocachino():
  global product_selected
  product_selected = "3"
  sel_sugar()

def show_menu(menu,exit,run):
  clear_console()
  i=0
  for opt in (menu):
    if opt[2]:
      i+=1
      print("{}. {}".format(i, opt[0]))
  #print( "I i:", i)
  option = ""
  while option != exit:
    option = read_option(menu, i)
    if run:
      run_option(option, menu)
    else:
      drop_coffe(option,menu)


def run_option(option, menu):
  k=0
  for txt,fun,en in menu:
    #print(txt, fun, en)
    if en:
      k+=1
    if k == option:
      #print(fun)
      return fun()

def drop_coffe(suggar, menu):
  print("SUGGAR:", suggar)
  product_levels["water"] = product_levels["water"] - 60
  product_levels["coffe"] = product_levels["coffe"] - 1
  product_levels["suggar"] = product_levels["suggar"] - (suggar-1)*5
  check_levels()
  clear_console()
  print("Disfruta tu {} con {} azucar...".format(list_coffe[product_selected],list_suggar[suggar] ))
  print("\n\n\n\n Presiona una tecla para continuar")
  input()
  main()

def add_coffe():return main()
def add_suggar():return main()
def add_water(): return main()

def gestion():
  gest_menu = [
      ["Añadir cartuchos de café", add_coffe, 1],
      ["Añadir azucar", add_suggar, 1],
      ["Añadir agua", add_water, 1],
      ["Cancelar", main, 1]
  ]

  show_menu(gest_menu, "Cancelar", True)

def check_levels():
  #print(init_menu)

  if product_levels["water"] < 200 or product_levels["coffe"] < 1 or product_levels["suggar"] < 10:
    init_menu[0][2] = 0
    init_menu[1][2] = 0
    init_menu[2][2] = 0
    #print(init_menu)

def sel_sugar():
  sug_menu = [
      ["Nada", "sin", 1],
      ["Algo", "poca", 1],
      ["Medio", "media", 1],
      ["Mucho", "mucha", 1],
      ["Muchísima", "muchisima", 1]
  ]
  show_menu(sug_menu, "q", False)

def main():

  show_menu(init_menu, "Salir", True)

def salir():
  print("Salida...")
  sys.exit(0)

init_menu = [
      ["Comprar un Café Espresso", espresso, 1],
      ["Comprar un Capuchino", capuchino, 1],
      ["Comprar un Mocaccino", mocachino, 1],
      ["Gestión", gestion, 1],
      ["Salir", salir, 1]
  ]

main()