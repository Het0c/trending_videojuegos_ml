from kedro.pipeline import Pipeline, node
from .nodes import cargar_datos, procesar_datos, calcular_estadisticas

def create_pipeline():
    return Pipeline([
        node(cargar_datos, inputs=None, outputs="datos_crudos"),
        node(procesar_datos, inputs="datos_crudos", outputs="datos_procesados"),
        node(calcular_estadisticas, inputs="datos_procesados", outputs="resultados")
    ])


from kedro.pipeline import Pipeline, node
from .nodes import transformar_datos

def create_pipeline(**kwargs):
    return Pipeline([
        node(func=transformar_datos, inputs="datos_crudos", outputs="datos_limpios", name="transformar_datos")
    ])
