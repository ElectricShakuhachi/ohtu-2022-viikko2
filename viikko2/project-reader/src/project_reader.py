from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        poetry_data = toml.loads(content)["tool"]["poetry"]
        name = poetry_data["name"]
        description = poetry_data["description"]
        dependencies = poetry_data["dependencies"]
        dev_dependencies = poetry_data["dev-dependencies"]
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies, dev_dependencies)
