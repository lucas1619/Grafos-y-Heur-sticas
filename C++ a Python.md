# Introduccion
---
- Antes de comenzar a codear primero les agradezco la confianza de elegirme como su delegado, les prometo que hare todo mi esfuerzo para cumplir los 3 puntos que me e propuesto a hacer.
- En este markdown explicare no solo como pasar de C++ a Python de manera exitosa, lo estoy escribiendo pensando en cuales son los pasos a seguir para pasar de un lenguaje a otro sin complicaciones,
- Sin más que añadir, empezare con esta guia.
# Primeros pasos
---
- Lo primero que debes de hacer antes de migrar de un lenguaje a otro es investigar las caracteristicas de el lenguaje al que te quieres pasar y compararlas con el lenguaje que mas dominas. Las caracteristicas que yo considero mas importantes son:
    1. Tipado fuerte o débil
    2. Compilado o Interpretado
    3. Paradigmas de programacion soportados.
## Tipado fuerte o debil
---
- Esto hace referencia a que tan flexible es el lenguaje con las **violaciones de datos**.
- Las **violaciones de datos** ocurren cuando declaras una variable, le asignas un tipo de dato inicial y luego en otra parte de tu codigo le asignas otro tipo de dato distinto al inicial. Ejemplo en **Javascript**:
```
let foo = 120; //aca declaro una variable con nombre 'foo' y le asigno un numero entero
foo = 'Hello world' // a la variable 'foo' lee asigne un string
```
- Tambien se puede dar una violacion de dato cuando una funcion no retorna siempre un mismo tipo de dato. Ejemplo en **PHP**:
```
<?php //para que no digan: no compila :v
    function foo($bar)
    {
        return $bar;
    }
    echo foo(120); //la funcion 'foo' me retornara un numero entero
    echo foo('Hello world') //la funcion foo mereturnara un string
?>
```
- Un lenguaje con **tipado débil** es aquel lenguaje que es flexible en cuando a las **violaciones de datos**. Es decir, cuando el compilador o interprete detecte algun tipo de **violacion de datos** no se hace problemas con ello. Ejemplo de ello son los 2 códigos anteriores.
- Un lenguaje con **tipado fuerte** es aquel lenguaje que no te permite una **violacion de un dato**. Es decir, cuando el compilador o interprete detecte algun tipo de **violacion de datos** nos arrojara un error. Ejemplo en **C++**:
```
#include<iostream>
#include<string>
using namespace std;
int main(){
    auto a = 120;
    a = "Hello world"; //Cuando el compilador llegue a esta linea de codigo nos arrojara un error
    return 0;
}
```
## Compilado o interpretado
---
- Esta es para mi la caracteristica más importante que tiene un lenguaje de programación y comprender esto a profundidad va a marcar una diferencia muy grande entre ser un programador y un desarrollador.
- Un lenguaje compilado es aquel que antes de ser ejecutado, **todo el código** pasa por un proceso de **traspilacion** a **lenguaje máquina**. El encargado de esta **traspilacion o traduccion** a **lenguaje máquina** es el **COMPILADOR**.
- Mientras que, un lenguaje interpretado es aquel que va traduciendo a **lenguaje maquina** a medida que se va ejecutando, es decir que **solo traspila las lineas de codigo que sean necesarias en ese momento**. El encargado de esta **traspilacion o traduccion** a **lenguaje máquina** a medida que lo necesite es el **INTERPRETE**.
## Paradigmas de programacion soportados
---
- Es para mi lo menos importante dentro de lo mas importante, hace referencia a que tan 'adatable' es el lenguaje para soportar distintos tipos de **paradigmas de programacion**.
- Un **paradigma de programacion** es la filosofia que vas a usar para resolver un requerimiento o problema. Existen varios paradigmas pero yo destaco 3:
    +  Programacion orientada a objetos (POO)
    +  Programacion funcional
    +  Programacion estocastica
    +  Programacion orientada a eventos
- Si un lenguaje soporta mas de un tipo de paradigma le llamaremos **multiparadigma** (lo se, somos pocos creativos los del software para los nombres XD).
# Hello world
---
- Una vez habiendo investigado y comparado las características de el lenguaje que mas dominas con el lenguaje que quieres aprender, es casi un ritual escribir tu primer "hello world" en el nuevo lenguaje.
- Aprender a escribir un "hello world" no solo hay que tomarlo como parte de un ritual, tambien lo podemos tomar como una oportunidad para conocer la sintaxis basica que hay que tener para que un programa en un lenguaje funcione correctamente.
- Por ejemplo en **C++**, a la hora de escribir el "hello world" aprendemos no sólo a imprimir en consola ese mensaje, tambien aprendemos que siempre debemos incluir a la libreria principal  (iostream) y el namespace principal (std) del lenguaje y tambien siempre debemos incluir una funcion de nombre main y si usamos el compilador g++ o clang esta debe ser de tipo entero y me debe retornar 0 y si uso el compilador de Visual C++ esta funcion puede ser de tipo void y no retornar algun valor.
```
#include<iostream>
using namespace std;
int main(){
    cout<< "Hello world";
    return 0;
}
```
- En **Python** cambian un poco las cosas. No existe una libreria principal, no existe un espacio de nombres standard, no existe una funcion obligatoria. Solo basta con escribir la instruccion de imprimir en consola. Esta instruccion en  **C++** es 'cout<<' mientras que en **Python** 3.x es:
```
print("Hello world")
```
- Otra cosa importante para destacar es que **no es necesario** el uso del famoso ';' al final de una linea de código.
# Variables
---
- Uno de los pilares básicos de la progrmacion, las variables son espacios de memoria donde vas a almacenar datos. 
- En los lenguajes de **tipado fuerte** el tipo de dato asignado inicialmente a una variable **no puede cambiar** mientras que los lenguajes de **tipado debil** si se puede cambiar el tipo de dato pero por buenas prácticas **no debes cambiarlo**.
- En **C++** la sintaxis para declarar una variable es:
> (Palabra reservada del tipo de dato) (nombre de la variable);
```
int foo;
```
- Mientras que en **Python** es:
> (nombre de la variable)
```
foo
```
- Asi es tal cual lo leiste, no necesito poner alguna palabra reservada para poder crear una variable, es suficiente con solo escribir el nombre que le vamos a poner y del resto se encarga el **interprete** de **Python**. Esto es posible gracias a que **Python** es un lenguaje con **tipado débil e interpretado**.
- En lo que respecta a la asignacion de un dato a las variables en ambos lenguajes utilizamos el operador '='.
- En **C++**
```
int foo = 10;
```
- En **Python**
```
foo = 10;
```
- Una analogia que nos va a permitir entender la diferencia en el uso de las variables es la siguiente: Imagina que te estas mudando quieres almacenar objetos y tienes 2 cajas para poder hacer dicha tarea. A la primera le escribes con un plumon antes de almacenar tus objetos que tipo de objetos va a contener tu caja, por ejemplo: juguetes y luego para diferenciar esa caja de otras que tengan el tipo de objetos rotulados le colocas un nombre para que puedas diferenciarla del resto por ejemplo: jueguetes de la infancia y una vez rotulado de esa forma recien comienzas a meter tus juguetes de la infancia dentro de tu caja. Mientras que en la otra caja por apuros de tiempo simplemente le colocas un nombre que te permita diferenciar que caja es y metes los objetos que quieras. Sin embargo si colocaste multiples objetos de distinto tipo en la segunda caja a la hora de desempacar se te vas a demorar mas en colocar en su sitio los objetos que almacenaste mientras que en la primera caja se te va a hacer muy facil desempacar porque ya sabes de ante mano que tipo de objetos hay dentro de esa caja. 
# Operaciones Aritmeticas
---
