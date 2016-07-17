Basic script to upload file to sftp or ftp strategy
===================================================

Usage:

        ./bin/cronUpload.py <options>
        Options:
            -h, --host: FTP hostname
            -p, --port: FTP username
            -s, --secret: FTP account password
            -l, --local-path: Local path where files are
            -e, --files-extension:[optional] file extension default csv
            -r, --remote-path: Remote path where files will be uploaded
            -o, --prefix:[optional] Initial characters to files name
            -c, --is-secure:[optional] 1 for sftp or 2 for ftp
            
##TODO in development branch

* Create application appUpload.py containing the yml configuration:
        
        * app.yml [directories and other settings]
        * connections.yml [external ftp and sftp settings]
        * Use object ConfigApp inmutable
        
* Upload.py to cronUpload.py rename so that it can be used with parameters for planners systems (schedulers) such as jenks, cron,...
* Unit Testing and Refactor with Dependency Injection Pattern 
        
        * Create unitary testing [https://docs.python.org/2.7/library/unittest.html]
        * Dependency Injection Pattern [https://wiki.python.org/moin/DependencyInjectionPattern]
            - Dependency container with  container
            - Use factory to create strategy
...
