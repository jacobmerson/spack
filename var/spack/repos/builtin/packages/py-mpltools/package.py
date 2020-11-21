# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyMpltools(PythonPackage):
    """
    As the name implies, mpltools provides tools for working with matplotlib.
    For the most part, these tools are only loosely-connected in functionality,
    so the best way to get started is to look at the example gallery.
    """

    homepage = "http://tonysyu.github.io/mpltools/"
    url      = "https://pypi.io/packages/source/m/mpltools/mpltools-0.2.0.tar.gz"

    # notify when the package is updated.
    maintainers = ['jacobmerson']
    import_modules = ['mpltools', 'mpltools.annotation', 'mpltools.widgets',
                      'mpltools.style', 'mpltools.sphinx', 'mpltools.special',
                      'mpltools.io']

    version('0.2.0', sha256='1b983fa046cb599a11d14d57f14913a473ab0fdda5851209d62bb78bcfd29a1c')

    depends_on('py-matplotlib@1.0:', type=('build', 'run'))
    depends_on('py-configobj@4.4.0:', type=('build', 'run'))
    depends_on('py-future@0.12.4:', type=('build', 'run'))
