class RequestParams:
    def __init__(self):
        self.connectionInfo = ''
        self.localPath = ''
        self.remotePath = ''
        self.prefix = ''
        self.pattern = ''

    def __str__(self):
        return {
            'connectionInfo:' + self.connectionInfo,
            'localPath:' + self.localPath,
            'remotePath' + self.remotePath,
            'prefix:' + self.prefix,
            'pattern:' + self.pattern
        }
