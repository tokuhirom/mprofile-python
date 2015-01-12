# Python port of mprofile(MySQL profiler)

This is a port of mprofile(written in perl).

Original repo is here: https://github.com/kazuho/mprofile

## DEPENDENCIES

  * Python 2.6+(json module)
  * MySQL-python

## INSTALL

On CentOS:

    % sudo yum install MySQL-python

Other systems:

    % pip install --user git+git://github.com/tokuhirom/mprofile-python.git

## SYNOPSIS

By default, mpdump script connect to localhost database by root user without password.
Following options are available.

```
usage: mpdump [-h] [--host HOST] [--interval INTERVAL] [--mycnf MYCNF]
              [--password PASSWORD] [--port PORT] [--user USER]
              [--socket SOCKET] [--samples SAMPLES] [-v]

optional arguments:
  -h, --help           show this help message and exit
  --host HOST          address of MySQL server
  --interval INTERVAL  interval between samples (default: 0.1sec)
  --mycnf MYCNF        MySQL config file path (default: /etc/my.cnf)
  --password PASSWORD  MySQL password (default: no password)
  --port PORT          port no. of MySQL server (default: 3306)
  --user USER          MySQL username (default: root)
  --socket SOCKET      unix socket of MySQL server (by default, connects to
                       the server specified in my.cnf)
  --samples SAMPLES    number of samples to take (default: 1000, infinite if
                       set to 0)
  -v, --verbose        set verbose mode (loglevel=DEBUG)
```

First, take a dump file. This script runs 'SHOW FULL PROCESSLIST' periodically.

    % ./mpdump > mpdump.txt

Then, replace variable parameters by 'mpfilter' command. And collect the result by mpreport command.

    % mpfilter < mpdump.txt | mpreport | head -100

For more details, here is a kazuho-san's article(In Japanese): http://developer.cybozu.co.jp/archives/kazuho/2009/07/mysql-539d.html

## MOTIVATION

I don't want to install DBI/DBD::mysql and dependent modules for the server.

## FAQ

### How do I install these scripts to servers, that protected by firewall?

Clone this repo and run following command on your OSX machine.

    > shar mp* | pbcopy

Then, paste it on the terminal, that connected to remote server.

## LICENSE

Python version's copyright notice is here:

    The MIT License (MIT)
    Copyright © 2015 Tokuhiro Matsuno, http://64p.org/ <tokuhirom@gmail.com>

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the “Software”), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.

Original mprofile's copyright notice is here:

    Copyright (C) 2009 Cybozu Labs, Inc.
    All rights reserved.

    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions are
    met:

        * Redistributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer.

        * Redistributions in binary form must reproduce the above
    copyright notice, this list of conditions and the following disclaimer
    in the documentation and/or other materials provided with the
    distribution.

        * The names of its contributors may not be used to endorse or
    promote products derived from this software without specific prior
    written permission.

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
    "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
    LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
    A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
    OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
    SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
    LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
    DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
    THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
    (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
