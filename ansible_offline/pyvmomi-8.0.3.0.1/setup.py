# VMware vSphere Python SDK
#
# Copyright (c) 2009-2024 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from setuptools import setup

version_info_str = '8.0.3.0.1'

def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as fn:
        return fn.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

with open('test-requirements.txt') as f:
    required_for_tests = f.read().splitlines()


def getTypeAnnotationsPackageData():
    allFiles = []
    for root, dirs, files in os.walk(os.path.join(os.path.dirname(__file__), 'pyVmomi')):
        for file in files:
            if file.endswith('.pyi'):
                fileRelPath = os.path.relpath(str(os.path.join(root, file)))
                allFiles.append(fileRelPath.split(os.path.sep, 1)[1])
    allFiles.append('py.typed')
    return allFiles


setup(
    name='pyvmomi',
    version=version_info_str,
    description='VMware vSphere Python SDK',
    # NOTE: pypi prefers the use of RST to render docs
    long_description=read('README.rst'),
    url='https://github.com/vmware/pyvmomi',
    author='Broadcom, VCF Division.',
    author_email='daniel.draganov@broadcom.com, stefan.hristov@broadcom.com',
    packages=['pyVmomi', 'pyVim'],
    py_modules = ['vsanapiutils', 'vsanmgmtObjects'],
    package_data={"pyVmomi": getTypeAnnotationsPackageData()},
    install_requires=required,
    license='License :: OSI Approved :: Apache Software License',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Developers',
        'Environment :: No Input/Output (Daemon)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Distributed Computing',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: MacOS',
    ],
    keywords='pyvmomi, vsphere, vmware, esx',
    platforms=['Windows', 'Linux', 'Solaris', 'Mac OS-X', 'Unix'],
    python_requires='>=2.7.9, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    test_suite='tests',
    tests_require=required_for_tests,
    extras_require={
        'sso': [
            'pyOpenSSL',
            'lxml'
        ]
    },
    zip_safe=True
)
