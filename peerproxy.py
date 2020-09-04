#!/usr/bin/env python3

'''
peerproxy -- makes plugable Squid configs for redirection

peerproxy is template-and-config builder that makes Squid configs from a YAML file and a Jinja2 templte.

It defines yamlconf() and tentacle()

@author:     Dimitry

@copyright:  2019 Securitystandard.org. All rights reserved.

@license:    Apache 2.0

@contact:    gnomon@protonmail.com
@deffield    updated: 20200903
'''


import sys
import jinja2
import yaml
from pprint import pprint


class yamlconf:
    '''Parent class for anything that intersects YAML and Jinja2.'''
    def __init__(self, yamlin=None, j2in=None):
        '''Constructor for yamlconf.'''
        self.genconfig(yamlin, j2in)

    def jenv(self):
        '''Build the Jinja2 processing environment with some defaults.'''
        self.env = jinja2.Environment(
            loader = jinja2.FileSystemLoader('.')
        )

    def yamlup(self, yamlin):
        '''Load the YAML using the yaml module.'''
        yamlin = open(yamlin)
        self.y = yaml.load(yamlin)
        yamlin.close()

    def genconfig(self, yamlin=None, j2in=None):
        '''Generate a config file from a YAML and a template.  This is the meat.'''
        self.jenv()
        self.yamlup(yamlin)
        self.__dict__.update(self.y)
        template = self.env.get_template(j2in)
        self.config = template.render(confdict=self.y)


class tentacle(yamlconf):
    def __init__(self, yamlin=None, j2in=None, outfile=sys.stdout):
        '''Constructor for currentCA.'''
        self.genconfig(yamlin, j2in)
        pprint(self.y, width=80)
        self.outfile = outfile
        self.writeconfig()

    def writeconfig(self):
        '''Creates the config file via yamlconf.'''
        self.outfile.write(self.config)


def usage(retval=0):
    print("Usage:\n  %s <yamlFile.yml> <templateFile.j2> <outputFile.conf>" % (sys.argv[0]))
    sys.exit(retval)

if __name__ == "__main__":
    if len(sys.argv) < 4: usage(255)
    with open(sys.argv[3], 'w') as outfile:
        t = tentacle(sys.argv[1], sys.argv[2], outfile)
