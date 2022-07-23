from tornado.options import define, options


# command line params || default params
define("port", default=9096, help="app listen port")

# database conf
port = options.port