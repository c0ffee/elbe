# ELBE - Debian Based Embedded Rootfilesystem Builder
# Copyright (c) 2020 Olivier Dion <dion@linutronix.de>
#
# SPDX-License-Identifier: GPL-3.0-or-later

import doctest
import unittest

import elbepack.shellhelper as shellhelper
import elbepack.filesystem as filesystem

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(shellhelper))
    fs = filesystem.TmpdirFilesystem()
    tests.addTests(doctest.DocTestSuite(filesystem, extraglobs={"this":fs}))

    return tests
