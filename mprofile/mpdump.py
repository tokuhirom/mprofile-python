# -*- coding: utf-8 -*-
import MySQLdb
import argparse
import json
import sys
import time
from logging import DEBUG, StreamHandler, getLogger


logger = getLogger('mprofile')
_handler = StreamHandler()
_handler.setLevel(DEBUG)
logger.addHandler(_handler)


def parse_argument(argv=None):
    """
    The default settings are here.

    >>> parse_argument([])  # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
    Namespace(host='localhost', interval=0.1...,
    mycnf='/etc/my.cnf', password='', port=3306, samples=1000, socket=None,
    user='root', verbose=False)

    Specify arbitrary parameters with long option

    >>> argv = ['--host', 'myhost', '--interval', '0.5', '--password', 'test']
    >>> parse_argument(argv)  # doctest: +NORMALIZE_WHITESPACE
    Namespace(host='myhost', interval=0.5, mycnf='/etc/my.cnf',
    password='test', port=3306, samples=1000, socket=None, user='root',
    verbose=False)
    """
    parser = argparse.ArgumentParser()
    parser.set_defaults(
        host='localhost',
        interval=0.1,
        mycnf='/etc/my.cnf',
        password='',
        port=3306,
        samples=1000,
        socket=None,
        user='root',
        verbose=False,
    )

    parser.add_argument(
        '--host',
        help='address of MySQL server')
    parser.add_argument(
        '--interval', type=float,
        help='interval between samples (default: 0.1sec)')
    parser.add_argument(
        '--mycnf',
        help='MySQL config file path (default: /etc/my.cnf)')
    parser.add_argument(
        '--password',
        help='MySQL password (default: no password)')
    parser.add_argument(
        '--port', type=int,
        help='port no. of MySQL server (default: 3306)')
    parser.add_argument(
        '--user',
        help='MySQL username (default: root)')
    parser.add_argument(
        '--socket',
        help='unix socket of MySQL server '
             '(by default, connects to the server specified in my.cnf)')
    parser.add_argument(
        '--samples', type=int,
        help='number of samples to take (default: 1000, infinite if set to 0)')
    parser.add_argument(
        '-v', '--verbose', action='store_true',
        help='set verbose mode (loglevel=DEBUG)')
    args = parser.parse_args(sys.argv[1:] if argv is None else argv)

    if args.verbose:
        logger.setLevel(DEBUG)

    return args


def main():
    args = parse_argument()
    logger.debug(args)
    db = MySQLdb.connect(
        host=args.host,
        user=args.user,
        passwd=args.password,
        port=args.port,
        read_default_file=args.mycnf,
    )
    for i in range(args.samples):
        cur = db.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SHOW FULL PROCESSLIST")
        rows = [
            row for row in cur.fetchall()
            if (row['Info'] != 'SHOW FULL PROCESSLIST'
                and row['Command'] == 'Query')
        ]
        print json.dumps(rows)
        time.sleep(args.interval)

if __name__ == '__main__':
    main()
