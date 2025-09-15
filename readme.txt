README — Proyecto Kedro: Tendencias en la Industria del Gaming
Descripción del Proyecto

Este proyecto analiza las tendencias económicas en la industria de los videojuegos entre 2010 y 2024. Utilizando estadísticas descriptivas y visualizaciones, se identifican patrones de ingresos diarios, mensuales y anuales, con el objetivo de comprender la evolución del sector y anticipar escenarios futuros.
Objetivo

Explorar las tendencias del gaming mediante análisis estadístico, identificando patrones de ingresos, comportamiento temporal y distribución de datos relevantes para la industria.
Estructura del Proyecto

El proyecto está desarrollado con kedro, siguiendo una arquitectura modular y reproducible:

 Cómo ejecutar el pipeline

    Instalar dependencias:

pip install -r src/requirements.txt

Ejecutar el pipeline:

kedro run

(Opcional) Abrir Jupyter Notebook:

kedro jupyter notebook

Parámetros configurables

En parameters.yml puedes definir valores como:

media_umbral: 100000

Estos se pueden usar en los nodos para condicionar lógica o filtrar resultados.

Autores:

Héctor López
Estudiante de Ingeniería, desarrollador backend y analista técnico.
Duoc UC, 2025.

Bárbara Álveal
Estudiante de igeniería, desarrolladora Frontend y diseñadora de entornos.
Duoc UC, 2025.

Proyecto realizado para el curso de Machine Learning.