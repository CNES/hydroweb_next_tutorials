# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import sys
from pathlib import Path

# find project
sys.path.insert(0, str(Path(__file__).parents[1]))

from sphinx_gallery.sorting import FileNameSortKey

# -- Project information -----------------------------------------------------

project = 'hydroweb.next tutorials'
copyright = '2023, CNES'
author = 'CNES'

# The full version, including alpha/beta/rc tags
#release = '1.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx_gallery.gen_gallery',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'sphinx_rtd_theme'
html_theme = 'pydata_sphinx_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_logo = "_static/hydrowebnext.png"

html_theme_options = {
    "logo": {
        "alt_text": "hydroweb.next tutorials"
    },
    "favicons": [
        {
           "rel": "icon",
           "sizes": "32x32",
           "href": "hydrowebnext-32x32.png",
        },
    ],
    "icon_links": [
        {
            "name": "CNES",
            "url": "https://cnes.fr",
            "icon": "_static/cnes-logo-blue.png",
            "type": "local",
        },
        {
            "name": "Theia",
            "url": "https://www.theia-land.fr/en/homepage-en/",
            "icon": "_static/theia-logo-vertical.png",
            "type": "local",
        },
        {
            "name": "hydroweb.next",
            "url": "https://hydroweb.next.theia-land.fr",
            "icon": "_static/hydrowebnext.png",
            "type": "local",
        },
   ]
}




# --- sphinx-gallery configuration ---------------------------------------
sphinx_gallery_conf = {
    # path to your example scripts
    'examples_dirs': ['../first_steps_with_swot', '../general_tips'],
    # path to where to save gallery generated output
    'gallery_dirs': ['swot_gallery','tips'],
    # specify that examples should be ordered according to filename
    'within_subsection_order': FileNameSortKey,
    # directory where function granular galleries are stored
    'backreferences_dir': 'gen_modules/backreferences',
    # Modules for which function level galleries are created.  In
    # this case sphinx_gallery and numpy in a tuple of strings.
    #'doc_module': ('SampleModule'),
    'show_memory': True,
}

# configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'python': ('https://docs.python.org/{.major}'.format(sys.version_info), None),
    'matplotlib': ('https://matplotlib.org/', None),
    'pandas': ('https://pandas.pydata.org/', None),
}
