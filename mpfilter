#!/usr/bin/env python

# Replace parameters

import json
import fileinput
import re

for line in fileinput.input():
    rows = json.loads(line)
    for row in rows:
        if not row['Info']:
            pass
        info = row['Info']
        info = re.compile(r'''(?<=\W)-?(?:0x[0-9a-f]+|[0-9\.]+)|'.*?[^'\\]'|".*?[^\\]"''',
                re.IGNORECASE).sub('?', info)
        info = re.compile(r'''(\s+IN\s+)\([\?,\s]+\)''',
                re.IGNORECASE).sub(r'\1(...)', info)
        info = re.compile(r'''(\s+VALUES\s+)[\(\)\?\,\s]+''',
                re.IGNORECASE).sub(r'\1...', info)
        row['Info'] = info
    print json.dumps(rows)

