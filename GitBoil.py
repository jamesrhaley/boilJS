from subprocess import call
import shutil
import simplejson
from collections import OrderedDict
import os
import sys


# this is almost done but there is something wrong with the
# updating of the package.json file

## Helpers
# performs git clone into a new directory
def _clone_mkdir(git_url, new_name):
    hole_path = git_url + ' ' + new_name
    call('git clone '+ hole_path, shell=True)

def _remove_git(new_name):
    git_path = new_name + '/.git'
    shutil.rmtree(git_path)

    def _prep_json(path):
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

# object to collect appropriate data and to then use it 
class Boil(object):

    def _keywords(pack_keys):
        if ',' in pack_keys:
            return pack_keys.split(',')
        else:
            return pack_keys.split()

    @classmethod
    def git_clone(cls, git_url, new_name):
        _clone_mkdir(git_url, new_name)
        _remove_git(new_name)      

    @classmethod
    def cleanup_packagejson(cls, new_name, author, description, version,
                            license, pack_keys):
        # package.json path
        pack_path = new_name + '/package.json'

        data = _prep_json(pack_path)

        # update feilds.  Need to update keywords
        data["name"] = new_name
        data["author"] = author
        data["description"] = description
        data["version"] = version
        data["license"] = license
        data["keywords"] = self._keywords(pack_keys)

        # convert OrderedDict into a json string
        outfile = simplejson.dumps(data, indent=4)

        # remove old package.json and create/write a new one
        os.remove(pack_path)
        new_pack = open(pack_path, 'w')
        new_pack.write(outfile)
        new_pack.close()

    @classmethod
    def remove_licence(cls, new_name):
        license_path = new_name + '/LICENCE'

        try:
            os.remove(license_path)

        except:
            print('Something went wrong when removing the license! Can\'t tell what?')
            sys.exit(0) # quit Python   

    @classmethod
    def clean_readme(cls, new_name):
        readme_path = new_name + '/README.md'
        # readme_path = 'new-JS' + '/README.md'
        try:
            os.remove(readme_path)
            readme = open(readme_path,'w')
            readme.close()

        except:
            print('Something went wrong when updating the readme! Can\'t tell what?')
            sys.exit(0) # quit Python   
