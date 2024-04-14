#!/usr/bin/env python3
"""FastAPIScaffolder class"""
from utils import create_project_structure


class FastAPIScaffolder:
    """
    A class to scaffold a FastAPI project structure.

    Attributes:
        project_directory (str): The directory where
        the project structure will be generated.
    """

    def __init__(self, project_directory):
        """
        Initializes the FastAPIScaffolder with the project directory.

        Parameters:
            project_directory (str): The directory where the
            project structure will be generated.
        """
        self.project_directory = project_directory

    def scaffold_project(self):
        """
        Creates the directory structure and
        placeholder files for a FastAPI project.
        """
        # Define the directory structure for a FastAPI project
        fastapi_project_structure = {
            '__init__.py': '',
            'main.py': '',
            'core': {
                'models': {
                    'database.py': '',
                    '__init__.py': ''
                },
                'schemas': {
                    '__init__.py': '',
                    'schema.py': ''
                },
                'settings.py': ''
            },
            'tests': {
                '__init__.py': '',
                'v1': {
                    '__init__.py': '',
                    'test_v1.py': ''
                }
            },
            'v1': {
                'api.py': '',
                'endpoints': {
                    '__init__.py': '',
                    'endpoint.py': ''
                },
                '__init__.py': ''
            },
            'docker-comose.yaml': '',
            'Dockerfile': '',
            '.dockerignore': '',
            '.gitignore': '',
            'env.sample': ''
        }

        # Creates Project structure
        create_project_structure(fastapi_project_structure,
                                 self.project_directory)
