# -*- coding: utf-8 -*-
import MySQLdb
import json
import time

# interval between samples
INTERVAL = 0.1
# number of samples to take
SAMPLES = 1000

def main():
    db = MySQLdb.connect(
        # host='localhost',
        user='root',
        passwd='',
        read_default_file="/etc/my.cnf"
    )
    for i in range(SAMPLES):
        cur = db.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SHOW FULL PROCESSLIST")
        rows = [
            row for row in cur.fetchall()
            if (row['Info'] != 'SHOW FULL PROCESSLIST'
                and row['Command'] == 'Query')
        ]
        print json.dumps(rows)
        time.sleep(INTERVAL)

if __name__ == '__main__':
    main()
