

class Environment():
    def __init__(self, name, path, package_manager, packageType):
        self.__name = name
        self.__path = path
        self.__package_manager = package_manager
        self.__packages = []
        self.__packageType = packageType

    def getName(self):
        return self.__name

    def getPath(self):
        return self.__path


class PackageManager():
    def __init__(self, environment):
        self.__environment = environment

    def listPackages(self):
        pass


class EnvironmentManager():
    def __init__(self):
        self.__environments = []

    def addEnvironment(self, environment):
        pass

    def getEnvironments(self):
        pass

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
        # code to list all conda envs
        return []

    def read_virtualenvs(self, path):
        # code to list all virtualenvs in a path
        return []
