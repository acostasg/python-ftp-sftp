Basic script to upload file to sftp or ftp strategy
===================================================

Usage:

        ./upload.py <options>
        Options:
            -h, --host: FTP hostname
            -p, --port: FTP username
            -s, --secret: FTP account password
            -l, --local-path: Local path where files are
            -e, --files-extension:[optional] file extension default csv
            -r, --remote-path: Remote path where files will be uploaded
            -o, --provider:[optional] Provider name
            -c, --is-secure:[optional] 1 for sftp or 2 for ftp
