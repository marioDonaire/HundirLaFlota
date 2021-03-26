# Hundir la Flota

_Juego de hundir la Flota hecho en python de forma distribuida con pyro4 en italiano y español._

## Comenzando 🚀

_Necesitas tener instalado python y las librerías puestas en pre requisitos,funciona en Windows y en Mac/Linux puede dar problemas_


### Pre-requisitos 📋

_Librerias necesarias:_

* [Pyro4](https://pypi.org/project/Pyro4/)


### Instalación 🔧


_Una vez que tienes instalado Pyro4 ejecuta el archivo **GUIMAIN.py**_


### Intrucciones  🎮

Una vez ejecutado el archivo *GUIMAIN.py* puedes crear una partida o unirte a una partida,para unirte a una partida el otro jugador tiene que pasarte el codigo de la partida que aparece en la parte inferior del que crea la partida.
El Juego de hundir la flota consiste en un tablero de 10x10 en el que se colocan barcos que **se pueden rotar con el boton izquierdo del ratón**, los barcos son los siguientes:
* 1 barco de 4 casillas
* 2 barcos de 3 casillas
* 3 barcos de 2 casillas
* 4 barcos de 1 casilla

Una vez colocados los barcos en el tablero inferior y se conecte el otro jugador y los 2 hayais puestos todos los barcos empezará la partida,que consistirá en intentar adivinar donde están los barcos del otro jugador y hundirlos. En cada turno podrás elegir en el tablero superior una casilla del tablero del enemigo, si la casilla está en azul es que no la has seleccionado aún,si aparece en rojo es que has tocado un barco y si es amarillo es que no había un barco en esa casilla. Una vez elegido una casilla el otro adversario elegirá otra casilla,la casilla que haya elegido tu adversario se verá reflejado en el tablero inferior con los mismos colores y significado.
El juego irá cambiando de turnos hasta que uno de los 2 haya hundido todos los barcos del otro jugador y se informará al usuario si ha perdido o no y el juego terminará.


## Construido con 🛠️

* Python 3
* [Pyro4](https://pypi.org/project/Pyro4/) - Para la parte distribuida.
* [tkinter](https://docs.python.org/3/library/tkinter.html) - Para la interfaz gráfica.


## Autores ✒️

* **Mario Donaire Becerra** - *Creador* 

## Licencia 📄

Este proyecto está bajo la Licencia CC - mira el archivo [LICENSE.md](LICENSE.md) para detalles