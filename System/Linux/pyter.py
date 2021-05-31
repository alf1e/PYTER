#!/usr/bin/env python
import json
import os

import sys

arg = sys.argv

if arg[1] == "load":
    with open(".json", "r") as f:
        data = json.load(f)
    try:
        pkg_name = arg[2]
        path = data[pkg_name]
        with open(path["cnf_path"], "r") as e:
            cnf = json.load(e)

        args = arg
        del args[0]
        del args[1]
        del args[2]

        os.system(f"python3 {cnf['path']} {''+' '.join(args)}")
    except KeyError:
        print("No package found")
elif arg[1] == "install":
    with open(arg[2], "r")as f:
        data = json.load(f)
    pkg_name = data["name"]
    file_name = data["file_name"]
    os.system(f"pip3 install {''+' '.join(data['packages'])}")

    with open(".json", "r") as e:
        cnf = json.load(e)
    cnf[pkg_name] = {}
    cnf[pkg_name]["cnf_path"] = arg[2]
    os.system(f"mkdir /etc/PYTER/{pkg_name}")
    os.system(f"mv {arg[2]} /etc/PYTER/{pkg_name}")
    os.system(f"mv {file_name} /etc/PYTER/{pkg_name}")
    print(f"Installed '{pkg_name}'")
