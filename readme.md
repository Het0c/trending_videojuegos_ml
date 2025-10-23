## README — Proyecto Kedro: Tendencias en la Industria del Gaming
# Descripción del Proyecto

[![Powered by Kedro](https://img.shields.io/badge/powered_by-kedro-ffc900?logo=kedro)](https://kedro.org)

Video Explicativo:
https://drive.google.com/file/d/1Ve77Tgy7ZtvgMHceRnu_3xNI784bnAxa/view?usp=sharing

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

# estructura

.
|-- Examen_1
|   |-- Bella_Beats_Analysis_Master_Dataset_Raw.csv
|   |-- CRISP_DM_Gaming_Trends_2024.ipynb
|   |-- Ev\ Parcial\ 1\ -\ MLY0100.docx
|   |-- Gaming-Trends-2024\ -\ Copy.txt
|   |-- Gaming-Trends-2024.csv
|   |-- Limpieza.ipynb
|   |-- Untitled.png
|   `-- analisis_gaming_trend.ipynb
|-- conf
|   |-- README.md
|   |-- base
|   |   |-- catalog.yml
|   |   `-- parameters.yml
|   `-- local
|-- data
|   |-- 01_raw
|   |-- 02_intermediate
|   |-- 03_primary
|   |-- 04_feature
|   |-- 05_model_input
|   |-- 06_models
|   |-- 07_model_output
|   `-- 08_reporting
|-- docs
|   `-- source
|       |-- analisis_gaming_trend(1).ipynb
|       `-- gaming.csv
|-- notebooks
|-- pyproject.toml
|-- readme.md
|-- requirements.txt
|-- src
|   `-- trenging_videojuegos
|       |-- __init__.py
|       |-- __main__.py
|       |-- pipeline_registry.py
|       |-- pipelines
|       |   |-- __init__.py
|       |   `-- gaming_analysis
|       |       |-- nodes.py
|       |       `-- pipeline.py
|       `-- settings.py

# Autores:

Héctor López
Estudiante de Ingeniería, desarrollador backend y analista técnico.
Duoc UC, 2025.

Bárbara Álveal
Estudiante de igeniería, desarrolladora Frontend y diseñadora de entornos.
Duoc UC, 2025.


Proyecto realizado para el curso de Machine Learning.
