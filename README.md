 [![Code Issues](https://www.quantifiedcode.com/api/v1/project/059551fbe726481faff6265f90b82af3/badge.svg)](https://www.quantifiedcode.com/app/project/059551fbe726481faff6265f90b82af3)
 [![Python versions](https://img.shields.io/badge/python-3.3,%203.4,%203.5-blue.svg?style=flat)](https://www.python.org/download/releases/3.0/)
 [![Coverage Status](https://coveralls.io/repos/github/acostasg/upload/badge.svg?branch=master&no=cache)](https://coveralls.io/github/acostasg/upload?branch=master)
 [![Build Status](https://travis-ci.org/acostasg/upload.svg?branch=master&no)](https://travis-ci.org/acostasg/upload)


Basic script to upload file to sftp or ftp strategy
===================================================

Usage App with config:

        ./upload/appUpload.py
        
     Config:
            - In config/app.yml
                Configuration path local and remote, pattern and prefix from upload files in before local path, and default strategy (1 secure and 2 unsecured)
  
            - In config/connections.yml
                Connections for secure (sftp) and unsecured (ftp) strategies:
                Host, port, username and secret.       
                 
Remember for secure sftp create in your system: ssh-keygen -R sftp.example.com
                        
Usage Cron with params:        

        ./upload/cronUpload.py <options>
        Options:
            -h, --host: FTP hostname
            -p, --port: FTP username
            -s, --secret: FTP account password
            -l, --local-path: Local path where files are
            -e, --files-extension:[optional] file extension default csv
            -r, --remote-path: Remote path where files will be uploaded
            -o, --prefix:[optional] Initial characters to files name
            -c, --is-secure:[optional] 1 for sftp or 2 for ftp

            
#Historic:

* Create application appUpload.py containing the yml configuration:
        
        * app.yml [directories and other settings]
        * connections.yml [external ftp and sftp settings]
        
* Upload.py to cronUpload.py rename so that it can be used with parameters for planners systems (schedulers) such as jenks, cron,...
* Unit Testing and Refactor with Dependency Injection Pattern 
        
        * Create unitary testing [https://docs.python.org/2.7/library/unittest.html]
        * Dependency Injection Pattern [https://wiki.python.org/moin/DependencyInjectionPattern]
            - Dependency Injection with container
            - Use factory to create strategy

* Coverage unittest
    * /upload 100% files, 100% lines
