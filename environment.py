import subprocess
import os
from pathlib import Path
from typing import List


class Environment():
    def __init__(self, name, path, packageType, packageManager=None):
        self.__name = name
        self.__path = path
        self.__packageManager = packageManager
        self.__packages = []
        self.__packageType = packageType

    def getName(self):
        return self.__name

    def getPath(self):
        return self.__path

    def __repr__(self):
        return f"Environment(name={self.__name}, path={self.__path}, packageType={self.__packageType})"


class PackageManager():
    def __init__(self, environment):
        self.__environment = environment

    def listPackages(self):
        pass


class EnvironmentManager():
    def __init__(self):
        self.__environments = []
        self.__environmentReader = None

    def addEnvironmentReader(self, reader):
        self.__environmentReader = reader

    def loadEnvironments(self):
        results = self.__environments.read_conda_environments()
        for i in results:
            name, path = i.split()[:2]
            env = Environment(name, path, 'conda')
            self.__environments.append(env)

    def addEnvironment(self, environment):
        pass

    def getEnvironments(self):
        return self.__environments

    def removeEnvironment(self, environment):
        pass


class Package():
    def __init__(self, name, version):
        self.__name = name
        self.__version = version

    def getName(self):
        return self.__name

    def getVersion(self):
        return self.__version


class EnvironmentReader:
    def __init__(self):
        pass

    def read_conda_environments(self):
        environments = []
        result = subprocess.run(
            ['conda', 'env', 'list'],
            capture_output=True, text=True
        ).stdout
        return result.splitlines()[3:-1]


if __name__ == "__main__":
    reader = EnvironmentReader()

    # Find venv environments in current directory
    envs = reader.find_virtual_environments("~")
    print("Found venv virtual environments:")
    for env in envs:
        print(env)
