from kedro.pipeline import Pipeline, node
from .nodes import (
    cargar_datos,
    procesar_datos,
    transformar_datos,
    calcular_estadisticas
)

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        node(
    func=cargar_datos,
    inputs=None,
    outputs="datos_cargados",
    name="cargar_datos_node"
)
,
        node(
            func=transformar_datos,
            inputs="datos_cargados",
            outputs="datos_transformados",
            name="transformar_datos_node"
        ),
        node(
            func=procesar_datos,
            inputs="datos_transformados",
            outputs="datos_procesados",
            name="procesar_datos_node"
        ),
        node(
            func=calcular_estadisticas,
            inputs="datos_procesados",
            outputs="estadisticas",
            name="calcular_estadisticas_node"
        )
    ])
