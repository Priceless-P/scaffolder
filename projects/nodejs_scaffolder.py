#!/usr/bin/env python3
"""NodeJSScaffolder class"""
from utils import create_project_structure


class NodeJSScaffolder:
    """
    A class to scaffold a Node.js project structure.

    Attributes:
        project_directory (str): The directory where
        the project structure will be generated.
    """

    def __init__(self, project_directory):
        """
        Initializes the NodeJSScaffolder with the project directory.

        Parameters:
            project_directory (str): The directory where the
            project structure will be generated.
        """
        self.project_directory = project_directory

    def scaffold_project(self):
        """
        Creates the directory structure and
        placeholder files for a Node.js/Express.js project.
        """
        # Define the directory structure for a Node.js/Express.js project
        nodejs_project_structure = {
            'config': {
                'db.js': '',
                'logger.js': ''
            },
            'constants': {},
            'controllers': {},
            'logs': {
                'error.log': '',
                'info.log': ''
            },
            'middlewares': {},
            'models': {},
            'public': {
                'images': {},
                'videos': {},
                'files': {}
            },
            'routes': {
                'indexRoutes.js': ''
            },
            'scripts': {},
            'test': {},
            'utils': {},
            'docker-comose.yaml': '',
            'Dockerfile': '',
            'package.json': '',
            'README.md': '',
            'server.js': '',
            '.dockerignore': '',
            '.env': '',
            '.gitignore': '',
            'env.sample': ''
        }

        # Create the project structure
        create_project_structure(nodejs_project_structure,
                                 self.project_directory)
