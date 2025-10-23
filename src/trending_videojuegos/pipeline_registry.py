"""Project pipelines."""
from __future__ import annotations

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline


def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    pipelines = find_pipelines()
    pipelines["__default__"] = sum(pipelines.values())
    return pipelines

from trending_videojuegos.pipelines.gaming_analysis import pipeline as gaming_pipeline

def register_pipelines():
    return {
        "__default__": gaming_pipeline.create_pipeline()
    }
