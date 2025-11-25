# Comparativa de IAs: Análisis de Datos "Generación Z vs Frankenstein"

Esta comparativa evalúa el desempeño de dos modelos de IA al enfrentarse a un conjunto de datos periodísticos. Se utiliza el archivo CSV completo (200 registros) como la **"Verdad Absoluta" (Ground Truth)** para verificar la precisión de las respuestas.

  * **IA 1 (Enfoque Conversacional):** Muestra limitaciones severas en el manejo de datos estructurados. Analiza una **muestra minúscula** (solo 6 registros visibles o alucinados) y extrapola conclusiones erróneas para todo el dataset. Falla en identificar patrones macro y alucina información sobre IDs específicos.
  * **IA 2 (Enfoque Programático - Python):** Actúa como un Analista de Datos experto. Detecta errores de formato en el CSV original (líneas malformadas), escribe código para corregirlos y carga la totalidad de los datos (200 registros). Sus respuestas son precisas y basadas en evidencia matemática.

-----

## 2\. Verificación de Resultados: IA vs Realidad

A continuación, contrastamos las respuestas dadas por cada IA frente a los datos reales calculados directamente del CSV.

### Pregunta 1: Proporción de Categorías

*¿Cuál es la proporción de registros entre "Generación Z" y "Frankenstein"?*

| Métrica | Verdad Absoluta (CSV) | Respuesta IA 1 | Respuesta IA 2 |
| :--- | :--- | :--- | :--- |
| **Registros Totales** | **200** | 6 (3 de cada una) | 200 |
| **Proporción** | **50% vs 50%** (100 c/u) | 50% vs 50% | 50% vs 50% |
| **Veredicto** | - | **Engañoso**: Acierta el % por casualidad, pero ignora el 97% de los datos. | **Correcto**: Calculado sobre el total real. |

### Pregunta 2: Medios con mayor cobertura (Top 3)

*Sin contar "El País", ¿cuáles son los medios con más registros?*

| Ranking | Verdad Absoluta (CSV) | Respuesta IA 1 | Respuesta IA 2 |
| :--- | :--- | :--- | :--- |
| **1º Lugar** | **Milenio** (6 registros) | Televisa (2) | Milenio (6) |
| **2º Lugar** | **Reuters / El Universal** (4 c/u) | Box Office Guru (1) | Reuters (4) |
| **3º Lugar** | **Varios con 3** | Netflix Data (1) | El Universal (4) |
| **Veredicto** | - | **Incorrecto**: Inventa un ranking basado en su micro-muestra. | **Correcto**: Coincide con la data real. |

### Pregunta 3: Día de Mayor Actividad

*¿Cuál fue el día con más noticias publicadas?*

| Métrica | Verdad Absoluta (CSV) | Respuesta IA 1 | Respuesta IA 2 |
| :--- | :--- | :--- | :--- |
| **Fecha** | **2025-11-16** | 2025-11-04 | 2025-11-16 |
| **Volumen** | **28 registros** | "Mayoría" (de su muestra) | 28 registros |
| **Veredicto** | - | **Incorrecto**: Selecciona una fecha arbitraria de sus pocos datos. | **Correcto**: Identifica el pico real de actividad. |

-----

## 3\. Análisis Técnico y de Errores

### IA 1: Alucinaciones y Contexto Limitado

  * **Error Crítico de Lectura:** La IA 1 afirma explícitamente: *"Hay 3 registros sobre Generación Z... y 3 registros sobre Frankenstein"*. Esto indica que no leyó el archivo completo o que su ventana de contexto le impidió procesar las 200 filas, limitándose a un "snippet" inicial.
  * **Alucinación de Datos:** En su intento de justificar respuestas, la IA 1 asigna fechas incorrectas a ciertos IDs (ej. asocia registros del 16 de nov al 4 de nov) para que cuadren con su narrativa.
  * **Incapacidad de Procesamiento:** No detectó el error de sintaxis en el archivo CSV (línea 185 malformada) porque nunca llegó a leer hasta esa línea.

### IA 2: Robustez y Código

  * **Limpieza de Datos:** La IA 2 detectó que el CSV tenía líneas con errores (comas dentro de títulos sin comillas, ej. *"Mi Frankenstein no tiene miedo, tiene dolor"*). Escribió una función en Python (`fix_csv_line`) para reparar esto antes de cargar el DataFrame, lo cual es una habilidad avanzada de manejo de datos.
  * **Análisis de Sentimiento:** Al no poder "leer" subjetivamente 200 textos uno por uno, la IA 2 implementó un algoritmo basado en diccionarios de palabras positivas/negativas, lo cual es la aproximación escalable correcta para datasets grandes.

## 4\. Conclusión

La **IA 2 es inmensamente superior** para esta tarea. Mientras que la IA 1 actúa como un chatbot conversacional que intenta "adivinar" basándose en fragmentos, la IA 2 actúa como un entorno de ejecución de código (Python) que garantiza:

1.  **Integridad de los datos** (carga el 100% del archivo).
2.  **Precisión matemática** (cálculos exactos vs estimaciones).
3.  **Reproducibilidad** (el código puede auditarse).
