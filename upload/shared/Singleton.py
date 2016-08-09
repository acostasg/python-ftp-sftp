class SingleMetaClass(type):
    """
    Pattern singleton class
    """
    instance = None

    def __call__(cls, *args, **kw):
        if not cls.instance:
            cls.instance = super(SingleMetaClass, cls).__call__(*args, **kw)
        return cls.instance
