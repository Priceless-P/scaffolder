#!/usr/bin/env python3
import os
from utils import create_project_structure


class SinatraScaffolder:
    """
    A class to sinatra a FastAPI project structure.

    Attributes:
        project_directory (str): The directory where
        the project structure will be generated.
    """

    def __init__(self, project_directory):
        """
        Initializes the SinatraScaffolder with the project directory.

        Parameters:
            project_directory (str): The directory where the
            project structure will be generated.
        """
        self.project_directory = project_directory

    def scaffold_project(self):
        """
        Creates the directory structure and
        placeholder files for a Sinatra project.
        """
        # Define the directory structure for a Sinatra project
        sinatra_project_structure = {
            'Gemfile': '',
            'README.md': '',
            'app': {
                'controllers': {
                    'application_controller.rb': ''
                },
                'models': {
                    'model.rb': ''
                },
                'views': {
                    'index.erb': ''
                }
            },
            'config': {
                'environment.rb': '',
            },
            'config.ru': '',
            'public': {
                'stylesheets': {}
            },
            'spec': {
                'controllers': {},
                'features': {},
                'models': {},
                'spec_helper.rb': ''
            },
            'test': {},
            'docker-comose.yaml': '',
            'Dockerfile': '',
            '.dockerignore': '',
            '.gitignore': '',
            '.sample.env': ''
        }

        # Creates Project structure
        create_project_structure(sinatra_project_structure,
                                 self.project_directory)
