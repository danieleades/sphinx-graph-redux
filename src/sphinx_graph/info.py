"""Dataclass objects will store information about a Vertex directive."""
from dataclasses import dataclass


@dataclass
class Info:
    """Vertex information dataclass."""

    docname: str
