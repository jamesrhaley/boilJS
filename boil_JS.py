#!/usr/bin/env python
from subprocess import call
import shutil
import simplejson
from collections import OrderedDict
import os

### TODO
# make README.md blank
# update key words



# https://github.com/jamesrhaley/es2015-babel-gulp-jasmine.git

new_name = raw_input("what should the project be called now: ")
if not os.path.isdir(new_name):


    ######## ------ gather info and download files ------ ############
    # get all of the needed info to down load the file and update it
    url = raw_input("what github url should we clone: ")

    hole_path = url + ' ' + new_name
    # load git file
    call('git clone '+ hole_path, shell=True)


    author = raw_input("new author: ")
    description = raw_input("new description: ")
    version = raw_input("version?(1.0.0): ")
    licence = raw_input("licence?(MIT): ")


    # # get the name of the git file
    # file_name = ''
    # for i,item in enumerate(url):
    #     if url[-i] == '/':
    #         file_name = url[i+1:].split('.')[0]
    #         break


    ######## ------ remove .git folder ------ ############
    # create the path to the .git directory
    git_path = new_name + '/.git'

    # remove git files
    shutil.rmtree(git_path)


    ######## ------ edit package.json ------- ############
    # test code!!!!!

    # pack_path = 'package.json'
    # new_name = 'ed'
    # author = 'ted'
    # description = 'haha'

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

    os.remove('README.md')

    try:
        readme = open('README.md','r+')
        readme.close()

    except:
        print('Something went wrong! Can\'t tell what?')
        sys.exit(0) # quit Python   


    ######## ------ transfer to new folder ------ ############
    # move files to new folder
    # shutil.move(file_name, new_name)
else:
    string = '\nThat directory already exits!!\nPlease come up with a new name.\n'
    print(string)





