from environment import Environment


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
