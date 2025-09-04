class Package():
    def __init__(self, name, version):
        self.__name = name
        self.__version = version

    def getName(self):
        return self.__name

    def getVersion(self):
        return self.__version
