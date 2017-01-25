#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "yunsite.settings")
=======
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
>>>>>>> ac476e71e84edb7cb900edceb0c62888b3433ff9

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
