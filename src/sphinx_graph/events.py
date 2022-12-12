"""Lifecycle events specific to the Vertex node."""

from __future__ import annotations

from docutils import nodes
from sphinx.application import Sphinx
from sphinx.environment import BuildEnvironment

from sphinx_graph import layout
from sphinx_graph.node import Node as VertexNode
from sphinx_graph.state import State

__all__ = [
    "process",
    "purge",
    "merge",
]


def process(_app: Sphinx, doctree: nodes.document, _fromdocname: str) -> None:
    """Process Vertex nodes by formatting and adding links to graph neighbours."""
    for vertex_node in doctree.findall(VertexNode):
        uid = vertex_node["graph_uid"]
        vertex_node.replace_self(layout.default(uid, vertex_node.deepcopy()))


def purge(_app: Sphinx, env: BuildEnvironment, docname: str) -> None:
    """Clear out all vertices whose docname matches the given one from the graph_all_vertices list.

    If there are vertices left in the document, they will be added again during parsing.
    """
    with State.get(env) as state:
        state.all_vertices = {
            id: vert
            for id, vert in state.all_vertices.items()
            if vert.docname != docname
        }


def merge(
    _app: Sphinx, env: BuildEnvironment, _docnames: list[str], other: BuildEnvironment
) -> None:
    """Merge the vertices from multiple environments during parallel builds."""
    with State.get(env) as state, State.get(other) as other_state:
        state.all_vertices.update(other_state.all_vertices)
