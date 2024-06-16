#!/usr/bin/python3
""" Fabric script that generates a .tgz archive from the contents of the web_static folder of your AirBnB Clone repo, using the function do_pack."""

from datetime import datetime
from fabric.api import loacal
import os.path

def do_pack():
    """create a tar of web dir"""
    time = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(time.year,
                                                         time.month,
                                                         time.day,
                                                         time.hour,
                                                         time.minute,
                                                         time.second)

    if os.path.isdir(versions) is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
