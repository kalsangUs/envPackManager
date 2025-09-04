
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
