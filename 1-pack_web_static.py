#!/usr/bin/python3
"""
    Fabric script that generates a .tgz archive from the contents of the
    web_static folder of your AirBnB Clone repo.
"""

import tarfile
import os
from datetime import datetime


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
