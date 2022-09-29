#!/usr/bin/python3
"""
    Fabric script that generates a .tgz archive from the contents of the
    web_static folder of your AirBnB Clone repo.
"""

import tarfile
import os
from datetime import datetime
from fabric.api import *

env.hosts = ["44.200.186.181", "3.236.123.155"]
env.user = "ubuntu"


def deploy():
    """Calls all relevant functions in archive deployment"""
    tar = do_pack()
    if not tar:
        return False
    return do_deploy(tar)


def do_pack():
    """ Creates a .tgz archive using assoc files"""
    destdir = "versions/"
    filename = "web_static_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".tgz"
    if not os.path.exists(destdir):
        os.mkdir(destdir)
    with tarfile.open(destdir + filename, "w:gz") as tar:
        tar.add("web_static", arcname=os.path.basename("web_static"))
    if os.path.exists(destdir + filename):
        return destdir + filename
    else:
        return None


def do_deploy(archive_path):
    """ Deploys an archive to the servers"""
    if not os.path.exists(archive_path):
        return False

    results = []

    res = put(archive_path, "/tmp")
    results.append(res.succeeded)

    basename = os.path.basename(archive_path)
    if basename[-4:] == ".tgz":
        name = basename[:-4]
    newdir = "/data/web_static/releases/" + name
    run("mkdir -p " + newdir)
    run("tar -xzf /tmp/" + basename + " -C " + newdir)

    run("rm /tmp/" + basename)
    run("mv " + newdir + "/web_static/* " + newdir)
    run("rm -rf " + newdir + "/web_static")
    run("rm -rf /data/web_static/current")
    run("ln -s " + newdir + " /data/web_static/current")

    return True
