from .base import Base

class Hello(Base):
    def run(self):
        hello = 'Hello, World!'
        return ['echo'] + hello.split(' ')
