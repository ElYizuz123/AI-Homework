# Análisis de las 4 IAs

Para evaluar el desempeño, primero establecemos los **Hechos Reales (Ground Truth)** del archivo CSV, que son los únicos datos válidos matemáticamente:
* **Volumen:** 200 registros exactos.
* **Distribución:** 50% Generación Z / 50% Frankenstein.
* **Cronología:** Datos de Agosto, Octubre y Noviembre de 2025. **No hay Diciembre.**
* **Pico de Actividad:** 16 de Noviembre de 2025 (28 registros).
* **Caso "El Financiero":** 4 registros reales (todos de Frankenstein).

### 1. Perfiles de las Inteligencias

#### **IA 1: LLama 3.2**
* **Perfil:** Intenta leer el texto plano pero tiene una "ventana de atención" muy corta. Lee los primeros registros y olvida el resto.
* **Comportamiento:** No inventa datos agresivamente, pero omite masivamente información existente.
* **Resultado Clave:** Acertó la proporción 50/50 de pura suerte o estimación temprana, pero falló en encontrar datos específicos (como los de *El Financiero*).

#### **IA 2: Phi 3**
* **Perfil:** La más peligrosa. Al no encontrar datos en su memoria, los inventa para complacer al usuario.
* **Comportamiento:** Rompe la realidad temporal. Inventó un mes entero (**Diciembre**) que no existe en el archivo.
* **Resultado Clave:** Dijo que el día pico fue el 18 de diciembre, lo cual es imposible. Calculó un total de 206 registros (6 más de los que existen).

#### **IA 3: Gemma 3**
* **Perfil:** Caótica. Mezcla aciertos puntuales con alucinaciones masivas y fallos técnicos.
* **Comportamiento:** Infló el dataset a **286 registros** (inventando 86 inexistentes). Sufrió un colapso técnico (bucle infinito) al intentar listar palabras clave.
* **Resultado Clave:** Fue la única IA de texto que acertó el día pico (**16 de Noviembre**), aunque erró en la cantidad de registros (dijo 9, son 28).

#### **IA 4: Gemini**
* **Perfil:** No lee, **ejecuta**. Utiliza código Python para analizar la estructura matemática del archivo.
* **Comportamiento:** Determinista y preciso. Si el dato existe, lo cuenta; si no, marca cero.
* **Resultado Clave:** Identificó los 200 registros exactos, la fecha pico correcta con su volumen real (28) y filtró correctamente los medios sin alucinar.

---

### 2. Tabla Comparativa de Rendimiento

| Métrica Crítica | IA 1 (Texto) | IA 2 (Texto) | IA 3 (Texto) | **IA 4 (Código)** | **Veredicto** |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Total de Registros** | *No calculó* (Muestra <10) | 206 (Falso) | 286 (Muy Falso) | **200 (Exacto)** | **IA 4 Gana** |
| **Proporción (GenZ / Frank)** | **50% / 50%** | 62% / 37% | 46% / 53% | **50% / 50%** | **Empate IA 1 y IA 4** |
| **Fecha de Mayor Actividad** | 15 Nov (Incorrecto) | 18 Dic (**Inexistente**) | **16 Nov** (Correcto) | **16 Nov** (Correcto) | **IA 3 y IA 4 Ganan** |
| **Conteo del Día Pico** | 3 registros | N/A | 9 registros | **28 registros** | **IA 4 Gana** |
| **Registros "El Financiero"** | "No hay" (Ceguera) | "Cero" (Error lógico) | "2 GenZ, 3 Frank" (Falso) | **4 de Frankenstein** | **IA 4 Gana** |
| **Registros Frank < 7 Nov** | "Solo 1" | "Cero" | 11 registros | **34 registros** | **IA 4 Gana** |
| **Alucinación de Datos** | Baja (Omisión) | **Crítica** (Invención) | **Alta** (Invención + Glitch) | **Nula** | **IA 4 Gana** |

---

### 3. Argumentación y Análisis Forense

#### **¿Por qué fallaron IA 1, 2 y 3?**
1.  **Saturación de Contexto:** Al leer el CSV como texto, perdieron el hilo después de las primeras 20-50 líneas. Por eso la IA 1 dice "solo encontré 1 registro" cuando había 34.
2.  **Relleno Probabilístico:** Cuando la IA 2 y 3 no recordaban el dato, su entrenamiento las obligó a generar una respuesta "plausible" pero falsa (como inventar fechas en diciembre para sonar coherentes).

#### **¿Por qué triunfó la IA 4?**
La IA 4 operó bajo un modelo de **Razonamiento Computacional**. No intentó memorizar el archivo; generó un script (una herramienta) para procesarlo.
* **Filtrado Real:** Para encontrar "El Financiero", la IA 4 no leyó el texto; aplicó un filtro `df[df['Medio'] == 'El Financiero']`. Esto garantiza 100% de precisión.
* **Sin Sentimientos:** La IA 4 no tiene sesgos de "completar" información. Si el código dice 200 filas, reporta 200 filas.

---

### 4. Conclusión Definitiva

El ranking final basado en **Fiabilidad para Análisis de Datos**:

1. **IA 4 (Campeona Indiscutible):** La única capaz de ofrecer una verdad objetiva. Demostró precisión matemática, coherencia temporal y capacidad de filtrado profundo. **Es la única opción válida para trabajar con CSVs.**
2. **IA 1 (La "Menos Peor"):** Aunque es ciega a los detalles (falló en conteos específicos), acertó la métrica macro más importante (50/50). Es "segura" porque sus errores son por omisión ("no sé") en lugar de invención.
3. **IA 3 (El Peligro Inestable):** Acertó la fecha, lo cual es meritorio, pero inventar casi 100 registros fantasma y entrar en bucles técnicos la hace inútil para reportes serios.
4. **IA 2 (Descalificada):** Inventar datos temporales (Diciembre) en un análisis cronológico es un error fatal que invalida cualquier conclusión. Es activamente engañosa.