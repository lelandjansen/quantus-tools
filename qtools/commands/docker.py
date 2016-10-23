# import os
# from .base import Base
#
# class Docker(Base):
#
#     def run(self):
#         program = ['docker']
#         return [program + self.method_arguments()]
#
#
#     def method_arguments(self):
#         command = list()
#         for k, v in self.options.items():
#             if k.startswith('--') and v:
#                 method = k.strip('-').replace('-', '_')
#                 try:
#                     command += getattr(self, method)()
#                 except AttributeError:
#                     err_msg = '\'{}\' has no method \'{}\''.format(
#                         self.__class__.__name__.lower(), method)
#                     raise NotImplementedError(err_msg)
#
#         return command
#
#     def up():
#         # Start docker
#         return []
#
#     def build():
#         return ['build', os.getcwd()]
#
#     def down():
#         # Stop docker
#         return []
