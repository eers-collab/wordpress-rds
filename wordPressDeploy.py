#!/usr/bin/env python3
# Assumption 1 : File which stages the deployment manifest is the wordpress-deployment.yaml
# Assumption 2: Clone the repo's ( https://github.com/eers-collab/wordpress-rds or https://github.com/eers-collab/wordpress-localmysql ) and pass the repo directory ( ex: wordpress-rds or wordpress-localmysql as input parameters to the python script)

import argparse
import yaml
import logging
import os
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

def updateWordpressVersion(wordPressVersion=NONE, folder=NONE):
    f_read=open(os.getcwd()+"/"+folder+"/wordpress-deployment.yaml", "r")
    dt=yaml.SafeDumper(ll, f_new)
    f_read=open(os.getcwd()+"/"+folder+"/wordpress-deployment.yaml", "r")
    data = yaml.load_all(f_read, Loader=yaml.SafeLoader)
    ll=list(data)
    f_read.close()
    f_new=open(os.getcwd()+"/wordpress-rds"+"/wordpress-deployment.yaml" , "w")
    f_new.close()
    return "Version Updated"

if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('-w', '--wordPress-version', help='word press image version to deploy ex: wordpress:5.5-apache')
    PARSER.add_argument('-r', '--repository-folder', help='repository_folder  ex: wordpress-rds')
    updateWordpressVersion(wordPressVersion=ARGS.wordPress_version, folder=ARGS.repository_folder)
