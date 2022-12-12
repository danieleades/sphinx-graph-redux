"""Custom configuration for Sphinx Graph."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class VertexConfig:
    """Optional additional configuration for a vertex directive.

    Args:
        require_fingerprints:
            Whether parent links *must* provide fingerprints.
            If ``False`` (the default) then link fingerprints are checked
            if set, and ignored otherwise.
    """

    require_fingerprints: bool | None = False
    layout: str | None = None

    def _override(self, other: "VertexConfig") -> VertexConfig:
        return VertexConfig(
            require_fingerprints=self.require_fingerprints if other.require_fingerprints is None else other.require_fingerprints,
            layout=self.layout if other.layout is None else other.layout,
        )


@dataclass
class Config:
    """Configuration object for Sphinx Graph.

    This class is the entry point for all configuration.

    Example:
        Configuration should be set in the ``conf.py`` file:

        .. code:: python

            from sphinx_graph import Config

            graph_config = Config()

    Args:
        vertex_config
            Default configuration to apply to all vertices.

            Can be overriden for specific vertices, or 'types' of vertices (see below)

            Example:
            .. code:: python

                from sphinx_graph import Config, DirectiveConfig
                import re

                graph_config = Config(
                    vertex_config = DirectiveConfig(
                        require_fingerprints = True,
                    ),
                )
        types:
            Set default directive configuration for 'types' of vertices.

            Example:
            .. code:: python

                from sphinx_graph import Config, DirectiveConfig
                import re

                graph_config = Config(
                    types = {
                        "req": DirectiveConfig(
                            require_fingerprints = True,
                        )
                    },
                )
    """

    vertex_config: VertexConfig = VertexConfig()
    types: dict[str, VertexConfig] = field(default_factory=dict)
