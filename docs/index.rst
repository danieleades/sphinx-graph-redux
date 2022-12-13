Welcome to sphinx-graph's documentation!
========================================


here is a glossary term outside a vertex directive

link to :term:`SOME_TERM`

the link works fine.

so do 'ref'-style links. Here's one to the :ref:`glossary`.

.. vertex:: 001

   here is a glossary term inside a vertex directive

   link to :term:`SOME_TERM`

   the link doesn't work

   neither do regular links. Here's one to the :ref:`glossary`.


.. vertex:: 002
   :parents: 001
   :require_fingerprints:

   .. note::

      nested directives seem to work fine

.. vertex:: 003
   :parents: 001, 002

   nested subheadings work fine too

   Subheading
   ----------

   subsection content


Glossary
--------


.. glossary::

    SOME_TERM
      Sphinx is a tool that makes it easy to create intelligent and beautiful docum
