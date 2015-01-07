#!/usr/bin/env python

import json
import fileinput
import re
from collections import defaultdict

sql_cnt = defaultdict(lambda: 0)
samples = 0.0

for line in fileinput.input():
    samples += 1

    rows = json.loads(line)
    for row in rows:
        if row['Info']:
            sql_cnt[row['Info']] += 1

for sql in sorted(sql_cnt.keys(), key=lambda key: sql_cnt[key]):
    print "%.3f:%s" % (
        sql_cnt[sql] / samples * 100,
        sql
        )

