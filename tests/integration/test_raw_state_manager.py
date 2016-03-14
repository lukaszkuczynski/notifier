import unittest
from tests.integration.article import Article
from application.state.raw_state_manager import RawStateManager
import os
from shutil import copyfile


class RawStateManagerTest(unittest.TestCase) :

    TEMP_FOLDER = 'temp'
    FILE_NAME = 'a.txt'
    RES_FOLDER = 'resources'
    FILE_PATH_TEMP = os.path.join(TEMP_FOLDER, FILE_NAME)
    FILE_PATH_RES = os.path.join(RES_FOLDER, FILE_NAME)

    def setUp(self):
        print('setup')
        self._sut = RawStateManager(None)
        self._sut.filename = self.FILE_NAME
        # self.removeFilesFromDir(self.FILE_PATH_TEMP)
        copyfile(self.FILE_PATH_RES, self.FILE_PATH_TEMP)

    def removeFilesFromDir(self, dir):
        map( os.unlink, [os.path.join( dir,f) for f in os.listdir(dir)] )

    def tearDown(self):
        self.removeFilesFromDir(self.TEMP_FOLDER)

    def test_writes_object(self):
        a = Article(3,'aa')
        self._sut.save(a)
        pass