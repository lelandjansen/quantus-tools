class Fuse:
    def value(default, config = None):
        fuse = 0
        for fb in default:
            fuse = fuse << 1
            k = list(fb.keys())[0]
            v = config[k] if config and k in config else fb[k]
            fuse = fuse | 1 if v else fuse
        return fuse
