import unittest
import shutil
import os
import sys
from GitBoil import GitBoil


# python -m unittest test.testGitBoil

class TestGitBoil(unittest.TestCase):

    new_name = 'new-JS'
    url = 'https://github.com/jamesrhaley/es2015-babel-gulp-jasmine.git'
    author = 'Tom Jones'
    description = 'make live easy'
    license = 'MIT'
    version = '1.0.0'
    keywords = 'JS es-2015'
    package_json = None

    new_process = GitBoil(new_name, url, author, description, 
                          version, license, keywords)

    def test_init(self):

        self.assertEqual(self.new_process.name, self.new_name)
        self.assertEqual(self.new_process.git_url, self.url)
        self.assertEqual(self.new_process.author, self.author)
        self.assertEqual(self.new_process.description, self.description)
        self.assertEqual(self.new_process.license, self.license)
        self.assertEqual(self.new_process.pack_keys, 
                        ['JS', 'es-2015'])

    dir_name = 'test/test-files'
    package_process = GitBoil(dir_name, url, author,description, 
                              version, license, keywords)

    if os.path.isfile('test/test-files/package.json'):
        os.remove('test/test-files/package.json')

    shutil.copyfile('test/test-files/sample.json', 
                    'test/test-files/package.json')

    def test_same_packagejson(self):
        f1 = open('test/test-files/sample.json','r+')
        f2 = open('test/test-files/package.json','r+')
        self.assertTrue(f1.read() == f2.read())
        f1.close()
        f2.close()

    package_process.cleanup_packagejson()

    def test_cleanup_packagejson(self):
        f1 = open('test/test-files/sample.json','r+')
        f2 = open('test/test-files/package.json','r+')
        self.assertFalse(f1.read() == f2.read())
        f1.close()
        f2.close()

if __name__ == '__main__':
    unittest.main()