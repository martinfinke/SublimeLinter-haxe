#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Martin
# Copyright (c) 2014 Martin
#
# License: MIT
#

"""This module exports the Haxe plugin class."""

from SublimeLinter.lint import Linter, util

from os import path

class Haxe(Linter):

    """Provides an interface to haxe."""

    syntax = 'haxe'
    cmd = None
    executable = 'haxe'
    version_args = '-version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 3.0'
    regex = r'^[^:]+:(?P<line>\d+):\D*(?P<col>\d+)[^:]*(?:(?P<error>:)|(?P<warning>:\s?Warning\s?:))\s?(?P<message>.+)'
    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = '-'
    error_stream = util.STREAM_BOTH
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = None
    def run(self, cmd, code):
        directory, basename = path.split(self.filename)
        command = ['haxe', '--cwd', directory, basename]
        return self.communicate(command, code)

