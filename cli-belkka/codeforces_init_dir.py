#!/usr/bin/env python3
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from codeforces_api import contest_standings


def init_dir(contest_id):
    standings = contest_standings(contestId=contest_id)
    contest_name = standings['contest']['name']
    os.mkdir(contest_name)
    os.chdir(contest_name)
    for problem in standings['problems']:
        os.mkdir(u"{index}. {name}".format(**problem))


progname, *args = sys.argv
if len(args) != 1:
    print("Usage: {} <contest_id>".format(os.path.basename(progname)))
else:
    init_dir(*args)
