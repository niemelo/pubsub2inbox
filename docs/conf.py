#   Copyright 2022 Google LLC
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
import sys
import os

sys.path.insert(0, os.path.abspath('../'))

project = 'Pubsub2Inbox'
copyright = '2022, Google Professional Services'
author = 'Google Professional Services'
release = '1.4.1'

extensions = [
    'sphinx.ext.napoleon', 'sphinx_markdown_builder', 'sphinx.ext.autodoc',
    'sphinx_autodoc_typehints', 'sphinx.ext.autosummary'
]

templates_path = ['_templates']
exclude_patterns = ['build/*', 'Thumbs.db', '.DS_Store']

html_theme = 'alabaster'
html_static_path = ['_static']

root_doc = 'docs/index'
