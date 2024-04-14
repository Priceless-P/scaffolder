#!/usr/bin/env python3
"""FlaskScaffolder Class"""
from utils import create_project_structure


class FlaskScaffolder:
    """
    A class to scaffold a Flask project structure.

    Attributes:
        project_directory (str): The directory where
        the project structure will be generated.
    """

    def __init__(self, project_directory):
        """
        Initializes the FlaskScaffolder with the project directory.

        Parameters:
            project_directory (str): The directory where the
            project structure will be generated.
        """
        self.project_directory = project_directory

    def scaffold_project(self):
        """
        Creates the directory structure and
        placeholder files for a Flask project.
        """
        # Define the directory structure for a Flask project
        flask_project_structure = {
            'app': {
                '__init__.py': '',
                'module1': {
                    '__init__.py': '',
                    'views.py': '',
                    'models.py': ''
                },
                'module2': {
                    '__init__.py': '',
                    'views.py': '',
                    'models.py': ''
                }
            },
            'static': {
                'css': {},
                'js': {},
                'images': {}
            },
            'templates': {
                'base.html': '',
                'header.html': '',
                'footer.html': '',
                'module1': {},
                'module2': {}
            },
            'config': {},
            'tests': {},
            'forms': {},
            'Dockerfile': '',
            '.dockerignore': '',
            'env.sample': '',
            '.gitignore': '',
            'app.py': ''
        }

        # Create Project structure
        create_project_structure(flask_project_structure,
                                 self.project_directory)
