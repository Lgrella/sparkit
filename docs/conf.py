"""Sphinx configuration."""
project = "Sparkit Temp"
author = "Lgrella"
copyright = "2024, Lgrella"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
