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
        self.__pyenvs = []
        self.__condaenvs = []
        self.__environmentReader = None

    def setEnviromentReader(self, reader):
        self.__environmentReader = reader

    def loadCondaEnvironments(self):
        results = self.__environmentReader.read_conda_environments()
        for i in results:
            name, path = i.split()[:2]
            env = Environment(name, path, 'conda')
            self.__environments.append(env)
            self.__condaenvs.append(env)

    def loadVirtualEnvironments(self):
        results = self.__environmentReader.find_virtualenvs(
            ["/Users/kal/code"])
        for i in results:
            name, path = i.split()[:2]
            env = Environment(name, path, 'virtualenv')
            self.__environments.append(env)
            self.__pyenvs.append(env)

    def addEnvironment(self, environment):
        pass

    def getEnvironments(self):
        return self.__environments

    def removeEnvironment(self, environment):
        pass

    def getCondaEnvironments(self):
        return self.__condaenvs

    def getVirtualEnvironments(self):
        return self.__pyenvs


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

    def find_virtualenvs(self, root_paths):
        """
        Scan given root directories for virtual environments and return as strings.

        Args:
            root_paths (list of str or Path): Directories to scan.

        Returns:
            list of str: Each string is "{envname} {envpath}".
        """
        env_list = []

        for root in root_paths:
            root = Path(root)
            if not root.exists():
                continue

            for dirpath, dirnames, filenames in os.walk(root):
                dirpath = Path(dirpath)

                # Check for virtualenv signature
                bin_path = dirpath / "bin" / "python"       # Mac/Linux
                scripts_path = dirpath / "Scripts" / "python.exe"  # Windows

                if bin_path.exists() or scripts_path.exists():
                    env_name = dirpath.name
                    env_list.append(f"{env_name} {str(dirpath)}")

                    # Skip deeper scanning inside this env
                    dirnames.clear()

        return env_list


if __name__ == "__main__":
    reader = EnvironmentReader()
    manager = EnvironmentManager()
    manager.setEnviromentReader(reader)
    manager.loadCondaEnvironments()
    manager.loadVirtualEnvironments()
    print(manager.getVirtualEnvironments())
    print(manager.getCondaEnvironments())
