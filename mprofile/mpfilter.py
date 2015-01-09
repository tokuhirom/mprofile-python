# -*- coding: utf-8 -*-
"""
Replace parameters
"""
import json
import fileinput
import re

INFO1 = re.compile(r'''(?<=\W)-?(?:0x[0-9a-f]+|[0-9\.]+)|'.*?[^'\\]'|".*?[^\\]"''', re.IGNORECASE)
INFO2 = re.compile(r'''(\s+IN\s+)\([\?,\s]+\)''', re.IGNORECASE)
INFO3 = re.compile(r'''(\s+VALUES\s+)[\(\)\?\,\s]+''', re.IGNORECASE)

def main():
    for line in fileinput.input():
        rows = json.loads(line)
        for row in rows:
            if not row['Info']:
                pass
            info = row['Info']
            info = INFO1.sub('?', info)
            info = INFO2.sub(r'\1(...)', info)
            info = INFO3.sub(r'\1...', info)
            row['Info'] = info
        print json.dumps(rows)

if __name__ == '__main__':
    main()
