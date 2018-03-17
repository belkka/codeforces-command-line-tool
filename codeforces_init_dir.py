#!/usr/bin/env python3
import sys
import os

from codeforces_api import contest_standings


def main(contest_id):
    standings = contest_standings(contestId=contest_id)
    contest_name = standings['contest']['name']
    os.mkdir(contest_name);
    os.chdir(contest_name);
    for problem in standings['problems']:
        os.mkdir(u"{}. {}".format(problem['index'], problem['name']))


progname, *args = sys.argv
if len(args) != 1:
    print("Usage: {0} <contest_id>".format(os.path.basename(progname)))
else:
    main(*args)
