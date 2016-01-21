from subprocess import call
import shutil
import simplejson
from collections import OrderedDict
import os




# object to collect appropriate data and to then use it 
class GitBoil(object):
    @staticmethod
    def _keywords(pack_keys):
        if ',' in pack_keys:
            return pack_keys.split(',')
        else:
            return pack_keys.split()

    def __init__(self, name, git_url, author, 
                 description, version, license, pack_keys):
        self.name = name
        self.git_url = git_url
        self.author = author
        self.description = description
        self.version = version
        self.license = license
        self.pack_keys = self._keywords(pack_keys)

    # performs git clone into a new directory
    def clone_mkdir(self):
        hole_path = self.url + ' ' + self.new_name
        call('git clone '+ hole_path, shell=True)

    def remove_git(self):
        git_path = self.new_name + '/.git'
        shutil.rmtree(git_path)

    def git_calls(self):
        self.clone_mkdir()
        self.remove_git()

    def prep_json(self, path):
        # overkill but I was having issues.  The following steps load and clean up
        # the package.json string before loading it into simplejson
        json_file = open(path, 'r+')
        f = json_file.read()
        g = f.split('\n')

        for i, item in enumerate(g):
            print item
            print item.strip()
            g[i] = item.strip()

        together = ''.join(g)

        # load json into as an OrderedDict to retain original order
        return simplejson.loads(together, object_pairs_hook=OrderedDict)        

    def cleanup_packagejson(self):
        # package.json path
        pack_path = self.name + '/package.json'

        data = self.prep_json(pack_path)

        # update feilds.  Need to update keywords
        data["name"] = self.name
        data["author"] = self.author
        data["description"] = self.description
        data["version"] = self.version
        data["license"] = self.license
        data["keywords"] = self.pack_keys

        # convert OrderedDict into a json string
        outfile = simplejson.dumps(data, indent=4)

        # remove old package.json and create/write a new one
        os.remove(pack_path)
        new_pack = open(pack_path, 'w')
        new_pack.write(outfile)
        new_pack.close()





