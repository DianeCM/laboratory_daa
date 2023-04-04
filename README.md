# El Lab (DAA Project)

En un laboratorio de la BIOFAM quieren modificar genéticamente una gallina para que sea más resistente a las enfermedades. Para esto deben de cambiar la secuencia de aminoácidos presentes en su genoma. La secuencia que quieren reproducir es la de los cocodrilos, que se sabe que son animales que han existido por millones de años.  
Entonces, dado que una secuencia de aminoácidos se puede codificar como una secuencia de caracteres se tiene:  

- $T$ es la secuencia de aminoácidos de los cocodrilos (tamaño $m$)  
- $S$ es la secuencia de aminoácidos de la gallina original (tamaño $n$)
- $A$ es la secuencia de aminoácidos de la galllina a crear (inicialmente vacía)

Para lograr que la gallina modificada adquiera la resistencia de un cocodrilo se sabe que su secuencia de aminoácidos $A$, debe contener como prefijo a $T$. Como en la BIOFAM hubo recortes de presupuesto solo cuentan con una máquina que puede hacer dos modificaciones genéticas:  
1. Extrae y elimina el primer aminoácido de $S$ y lo coloca al principio de $A$  
2. Extrae y elimina el primer aminoácido de $S$ y lo coloca al final de $A$  

Encuentre la **cantidad de secuencias de operaciones** posibles tales que la gallina genéticamente modificada sea resistente a las enfermedades.
