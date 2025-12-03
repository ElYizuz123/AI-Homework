### Análisis comparativo de las 3 IAS

#### 1. IA 1: LLama 3.2
* **Formato:** Cumple técnicamente con JSONL (un objeto JSON por línea sin comas al final).
* **Contenido:** Tiene un sesgo enorme hacia el *Machine Learning*. Interpretó "algoritmos" únicamente como "modelos de predicción" (Random Forest, SVM, etc.), ignorando algoritmos clásicos de ciencias de la computación (ordenamiento, búsqueda, grafos).
* **Problema principal:** Su estructura (`nombre`, `características`, `descripción`) es una base de datos, **no una conversación**.
    * *Por qué falla para Fine-Tuning:* Si entrenas a tu modelo con esto, aprenderá a escupir definiciones técnicas, pero no sabrá cómo responder a una pregunta de un estudiante. No tiene el formato "Pregunta -> Respuesta".

#### 2. IA 2: Phi 3
* **Formato:** **Falló**. Entregó un `JSON Array` (comienza con `[` y separa objetos con `,`). JSONL requiere que cada línea sea un objeto independiente sin envoltorio de lista.
* **Contenido:** El contenido era correcto (Bubble Sort, Merge Sort), pero la IA se rindió.
* **Problema principal:** Alucinó o fue "perezosa" al poner `// More entries here...`. Esto hace que el dataset sea basura inservible sin edición manual masiva.

#### 3. IA 3: Gemma 3:
* **Formato:** JSONL Correcto.
* **Estructura:** Utilizó el formato estándar de **Instrucción (Alpaca/Vicuna)**:
    * `"instruction"`: La pregunta que haría el usuario.
    * `"input"`: (Opcional) Contexto adicional.
    * `"output"`: La respuesta ideal del tutor.
* **Contenido:** Es la única que entendió el rol de **"Tutor experto"**.
    * No solo define, sino que explica *cómo funciona* (ej. "divide y vencerás", "LIFO", "FIFO").
    * Abarca un espectro real de algoritmos: Ordenamiento, Búsqueda, Estructuras de Datos, Complejidad (Big O), Grafos.
* **Utilidad para Fine-Tuning:** Este dataset está listo para usarse. La estructura `instruction` -> `output` es exactamente lo que los modelos Llama, Mistral o GPT necesitan para aprender a comportarse como asistentes.

