# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyPynvim(PythonPackage):
    """Python client to neovim"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/neovim/pynvim/blob/master/setup.py"
    url      = "https://pypi.io/packages/source/p/pynvim/pynvim-0.4.1.tar.gz"

    version('0.4.1', sha256='55e918d664654cfa1c9889d3dbe7c63e9f338df5d49471663f78d54c85e84c58')

    depends_on('py-msgpack@0.5.0:')
    depends_on('py-pytest@3.4.0:', type='test')
    depends_on('py-greenlet')
