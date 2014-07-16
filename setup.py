#!/usr/bin/env python
# Author: jiasir (Taio Jia)
# E-Mail: jiasir@icloud.com
# Code: https://github.com/nofdev/puppet-openstack
# License: https://github.com/nofdev/puppet-openstack/blob/master/LICENSE

import os
import sys
import logging
import ConfigParser
import noflib


# Config file
config_file = ConfigParser.RawConfigParser(allow_no_value=True)
config_file.read('puppet-openstack.conf')

# Create logger
logger = logging.getLogger('puppet-openstack')
logging.basicConfig(filename=log_file_path(), level=log_level(), format=log_format())


def log_file_path():
    '''Get log path from config file'''
    logger.info(config_file.get('logging', 'path'))
    return config_file.get('logging', 'path')

def log_level():
    '''Get log level from config file'''
    logger.info(config_file.get('logging', 'level'))
    return config_file.get('logging', 'level')

def log_format():
    '''Get log format from config file'''
    logger.info(config_file.get('logging', 'format'))
    return config_file.get('logging', 'format')

def install_puppetmaster():
    logger.info('install puppetmaster')
    execute_get_output('bash scripts/puppet-installer.sh', 'master')

def install_puppetagent():
    logger.info('install puppetagent')
    execute_get_output('bash scripts/puppet-installer.sh', 'agent')

def gen_cert_controller():
    logger.info('generate controller cert')
    execute_get_output('bash scripts/controller-installer.sh', 'gen-cert', 'openstack_controller')

def deploy_controller():
    logger.info('deploy controller')
    execute_get_output('bash scripts/controller-installer.sh', 'deploy', 'openstack_controller')

def gen_cert_compute(n):
    logger.info('generate compute %s cert' % n)
    execute_get_output('bash scripts/compute-installer.sh', 'gen-cert', 'openstack_compute%s' % n)

def deploy_compute(n):
    logger.info('deploy compute %s' % n)
    execute_get_output('bash scripts/compute-installer.sh', 'deploy', 'openstack_compute%s' % n)

def usage():
    print("""Usage: python setup.py [puppetmaster|puppetagent|gen-cert|deploy|openstack_controller|openstack_compute|n]
To install puppetmaster: python setup.py puppetmaster
To install puppetagent: python setup.py puppetagent
To generate controller cert: python setup.py gen-cert openstack_controller
To deploy controller: python setup.py deploy openstack_controller
To generate compute n cert: python setup.py gen-cert openstack_compute n #notice: n is a number
To deploy compute n: python setup.py deploy openstack_compute n #notice: n is a number
""")

def main():
    option = "validate"
    if len(sys.argv) > 1:
        option1 = sys.argv[1]
        option2 = sys.argv[2]
        option3 = sys.argv[3]
    if option1 == "puppetmaster":
        install_puppetmaster()
    elif option1 == "puppetagent":
        install_puppetagent()
    elif option1 == "gen-cert" and option2 == "openstack_controller":
        gen_cert_controller()
    elif option1 == "deploy" and option2 == "openstack_controller":
        deploy_controller()
    elif option1 == "gen-cert" and option2 == "openstack_compute":
        gen_cert_compute(option3)
    elif option1 == "deploy" and option2 == "openstack_compute":
        deploy_compute(option3)
    else:
        usage()
  
if __name__ == "__main__":
    main()