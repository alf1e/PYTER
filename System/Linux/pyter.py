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

