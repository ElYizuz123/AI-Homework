# Análisis comparativo de entrenamientos CNN
## Primeros entrenamientos bajo mismas condiciones

<img src="Prueba_original_1.png" alt="Imagen_1" width="700"> <img src="Prueba_original_2.png" alt="Imagen_2" width="700"> <img src="Prueba_original_3.png" alt="Imagen_3" width="700">

Se observa un resultado similar, en algunas clases se obtiene un mejor puntaje y se contraresta con un menor puntaje en otras, la diferencia se debe a que en cada entrenamiento se realizó una distribución diferente en el grupo de testeo y entrenamiento, pero el tratamiento de las imagenes es exactamente el mismo.

## Prueba con parámetros distintos

### Prueba con 20 epochs
<img src="Captura de pantalla 20 epochs.png" alt="Imagen_alter_1" width="700"> 
Se observa una ligera mejora con respecto a los entrenamientos originales que solo tenían 6 epochs, la diferencia en algunos casos como la clase 9 es insignificante, pero en otros como la clase 8 se nota una mejora significativa.
En este caso se da un mejor resultado debido a que estamos permitiendo al modelo generar mas rondas de entrenamiento en la que los pesos se ajustan de forma mas precisa.

### Prueba con 20 epochs, x10-4 LR y batch size de 128
<img src="Captura de pantalla 20 epochs x10-4 LR.png" alt="Imagen_alter_2" width="700"> 
En este ejemplo se observa un resultado que empeora significativamente los originales, se puede notar una reducción significativa en la mayoría de las clases. 
Esto sucede debido a que al reducir el learning rate podemos tener un ajuste mas preciso, pero requería un entrenamiento mucho mayor para llegar a resultados faborables, al mantener la misma cantidad de epochs, la misma cantidad de imágenes, la misma cantidad de capas y solo reducir el LR estamos consiguiendo un resultado mucho peor.

### Prueba de 3 capas con 40 epochs y batch size de 128
<img src="Captura 40 epochs 3 capas.png" alt="Imagen_alter_3" width="700"> 
En este otro ejemplo se ve un resultado ligeramente superior al conseguido con x10-4 en el LR, sin embargo continua siendo mucho peor que las pruebas originales, esto se debe a que al añadir 3 capas se está y gracias al tamaño de la imagen se está perdiendo demasiada información, por lo que los resultados no son faborables.

### Prueba de 1 capa, batch size de 128 y 40 epochs
<img src="Captura 40 epochs 1 capa.png" alt="Imagen_alter_3" width="700"> 
Esta prueba resulto ser la mas efectiva, al configurarlo con 40 epochs y una sola capa le damos información y tiempo suficiente para tener lo que necesita el modelo y conseguir resultados mucho mejores.






