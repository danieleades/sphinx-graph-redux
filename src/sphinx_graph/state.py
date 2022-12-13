"""Shared state for the sphinx-graph extension."""

from __future__ import annotations

from contextlib import contextmanager
from dataclasses import dataclass
from typing import Iterator

from networkx import DiGraph
from sphinx.environment import BuildEnvironment
from sphinx.errors import DocumentError
from sphinx.util import logging

from sphinx_graph.info import Info as VertexInfo

logger = logging.getLogger(__name__)


class DuplicateIdError(DocumentError):
    """Raised when a vertex with the same ID is added to the graph twice."""

    category = "Document Error"


@dataclass
class State:
    """State object for Sphinx Graph vertices."""

    all_vertices: dict[str, VertexInfo]

    def insert_vertex(self, uid: str, info: VertexInfo) -> None:
        """Insert a vertex into the context.

        Raises:
            DuplicateIdError: If the vertex already exists.
        """
        if uid in self.all_vertices:
            raise DuplicateIdError(f"Vertex {uid} already exists.")
        self.all_vertices[uid] = info

    @classmethod
    @contextmanager
    def get(cls, env: BuildEnvironment) -> Iterator[State]:
        """Get the GraphContext object for the given environment."""
        all_vertices = getattr(env, "graph_all_vertices", {})
        state = State(all_vertices)
        yield state
        env.graph_all_vertices = state.all_vertices  # type: ignore[attr-defined]


def build_graph(vertices: dict[str, VertexInfo]) -> DiGraph:
    """Build the graph from the list of vertices.

    This is called during setup, and doesn't need to be called again.
    """
    graph = DiGraph()
    for uid, vertex_info in vertices.items():
        # add each node
        graph.add_node(uid)

        # add all 'parent' edges
        for parent_uid, fingerprint in vertex_info.parents.items():
            graph.add_edge(uid, parent_uid, fingerprint=fingerprint)
    return graph
