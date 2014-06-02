#!/usr/bin/env python3
import sys
import time
import requests

try:
    out = open(sys.argv[1], "wb")
except IndexError:
    sys.exit("Usage: reged2icalendar.py output.ics < reged")

r=sys.stdin.read()
csv= ",\n".join([ l.split()[0] for l in r.splitlines() ])

# XXX
fn = "RSReferCsv.csv"
with open(fn, "w") as f: f.write(csv)

# TwinCalに作ってもらう
with open(fn) as f:
    user_agent = {"User-Agent": "Mozilla/5.0 (iPhone; U; CPU iPhone OS 2_0 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5A345 Safari/525.20"}
    r = requests.post("http://gam0022.net/app/twincal/parse.rb", headers=user_agent, files={"file": f})

out.write(r.content)
