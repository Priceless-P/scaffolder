#!/usr/bin/env python3
"""Main"""
from projects.fastapi_scaffolder import FastAPIScaffolder
from projects.flask_scaffolder import FlaskScaffolder
from projects.nodejs_scaffolder import NodeJSScaffolder
from projects.sinatra_scaffolder import SinatraScaffolder


def main():
    """Creates a Project structure for given type pf application"""
    project_type = input("Enter project type (fastapi, flask, "
                     "nodejs, expressjs, sinatra): ")
    project_directory = input("Enter project directory: ")

    if project_type == "fastapi":
        scaffolder = FastAPIScaffolder(project_directory)
    elif project_type == "flask":
        scaffolder = FlaskScaffolder(project_directory)
    elif project_type == "nodejs" or project_type == "expressjs":
        scaffolder = NodeJSScaffolder(project_directory)
    elif project_type == "sinatra":
        scaffolder = SinatraScaffolder(project_directory)
    else:
        print("Unsupported Format. Enter fastapi,"
              "flask, nodejs, expressjs, or sinatra")
        return
    scaffolder.scaffold_project()
    print("Project structure Created.")


if __name__ == "__main__":
    main()
