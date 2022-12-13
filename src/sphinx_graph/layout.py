"""Tools and methods for formatting vertex nodes into docutils nodes."""

from docutils import nodes


def default(uid: str, content: nodes.Node) -> nodes.Node:
    """Format a vertex Node as a docutils node."""
    new_content = nodes.Element()
    new_content.append(nodes.Text(f"---start vertex {uid}---"))
    new_content.append(content)
    new_content.append(nodes.line(f"---end vertex {uid}---", f"---end vertex {uid}---"))
    return new_content


def transparent(_uid: str, content: nodes.Node) -> nodes.Node:
    """Format a vertex Node as a docutils node."""
    return content
