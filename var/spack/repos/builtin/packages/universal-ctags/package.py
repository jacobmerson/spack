# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class UniversalCtags(AutotoolsPackage):
    """A maintained ctags implementation"""

    homepage = "https://ctags.io"
    git      = "https://github.com/universal-ctags/ctags"

    version('master', branch='master')
    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('pkg-config', type='build')
    depends_on('libtool', type='build')
