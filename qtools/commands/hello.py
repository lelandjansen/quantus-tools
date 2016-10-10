from .base import Base

class Hello(Base):
    def run(self):
        greeting = 'Hello, World!'
        return [['echo', greeting]]
