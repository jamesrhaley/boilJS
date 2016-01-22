#!/usr/bin/env python
from subprocess import call
import shutil
import simplejson
from collections import OrderedDict
import os
from GitBoil import Boil

### TODO
# make README.md blank
# update key words

# https://github.com/jamesrhaley/es2015-babel-gulp-jasmine.git

new_name = raw_input("what should the project be called now: ")
if not os.path.isdir(new_name):


    ######## ------ gather info and download files ------ ############
    # get all of the needed info to down load the file and update it
    url = raw_input("what github url should we clone: ")

    Boil.git_clone(url, new_name)

    author = raw_input("new author: ")
    description = raw_input("new description: ")
    version = raw_input("version?(1.0.0): ")
    licence = raw_input("licence?(MIT): ")



    ######## ------ edit package.json ------- ###########
    # package.json path
    pack_path = new_name + '/package.json'

    # overkill but I was having issues.  The following steps load and clean up
    # the package.json string before loading it into simplejson
    json_file = open(pack_path, 'r+')
    f = json_file.read()
    g = f.split('\n')

    for i, item in enumerate(g):
        print item
        print item.strip()
        g[i] = item.strip()

    together = ''.join(g)

    # load json into as an OrderedDict to retain original order
    data = simplejson.loads(together, object_pairs_hook=OrderedDict)

    # update feilds.  Need to update keywords
    data["name"] = new_name
    data["author"] = author
    data["description"] = description

    # convert OrderedDict into a json string
    outfile = simplejson.dumps(data, indent=4)

    # remove old package.json and create/write a new one
    os.remove(pack_path)
    new_pack = open(pack_path, 'w')
    new_pack.write(outfile)
    new_pack.close()

    Boil.remove_licence(new_name)

    Boil.clean_readme(new_name) 

else:
    string = '\nThat directory already exits!!\nPlease come up with a new name.\n'
    print(string)





