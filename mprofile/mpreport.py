# -*- coding: utf-8 -*-
import json
import fileinput
from collections import defaultdict

def main():
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

if __name__ == '__main__':
    main()
