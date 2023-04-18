import random
import string
import cherrypy


class StringMaker(object):
    @cherrypy.expose
    def index(self):
        return "Hello! How are you?"

    @cherrypy.expose
    def generate(self, length=9):
        return ''.join(random.sample(string.hexdigits, int(length)))


if __name__ == '__main__':
    cherrypy.quickstart(StringMaker())

