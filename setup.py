#!/usr/bin/env python2

# python setup.py sdist --format=zip,gztar

from setuptools import setup
import os
import sys
import platform
import imp
import argparse

version = imp.load_source('version', 'lib/version.py')

if sys.version_info[:3] < (2, 7, 0):
    sys.exit("Error: Electrum-ion requires Python version >= 2.7.0...")

data_files = []

if platform.system() in ['Linux', 'FreeBSD', 'DragonFly']:
    parser = argparse.ArgumentParser()
    parser.add_argument('--root=', dest='root_path', metavar='dir', default='/')
    opts, _ = parser.parse_known_args(sys.argv[1:])
    usr_share = os.path.join(sys.prefix, "share")
    if not os.access(opts.root_path + usr_share, os.W_OK) and \
       not os.access(opts.root_path, os.W_OK):
        if 'XDG_DATA_HOME' in os.environ.keys():
            usr_share = os.environ['$XDG_DATA_HOME']
        else:
            usr_share = os.path.expanduser('~/.local/share')
    data_files += [
        (os.path.join(usr_share, 'applications/'), ['electrum-ion.desktop']),
        (os.path.join(usr_share, 'pixmaps/'), ['icons/electrum-ion.png'])
    ]

setup(
    name="Electrum-ion",
    version=version.ELECTRUM_VERSION,
    install_requires=[
        'slowaes>=0.1a1',
        'ecdsa>=0.9',
        'pbkdf2',
        'requests',
        'qrcode',
        'protobuf',
        'dnspython',
        'jsonrpclib',
        'trezor>=0.6.3',
        'x11_hash>=1.4',
    ],
    dependency_links=[
        'git+https://github.com/mazaclub/x11_hash@1.4#egg=x11_hash-1.4',
        'git+https://github.com/electrum-ion/python-trezor@v0.6.13#egg=trezor',
    ],
    packages=[
        'electrum_ion',
        'electrum_ion_gui',
        'electrum_ion_gui.qt',
        'electrum_ion_plugins',
        'electrum_ion_plugins.audio_modem',
        'electrum_ion_plugins.cosigner_pool',
        'electrum_ion_plugins.email_requests',
        'electrum_ion_plugins.exchange_rate',
        'electrum_ion_plugins.hw_wallet',
        'electrum_ion_plugins.keepkey',
        'electrum_ion_plugins.labels',
        'electrum_ion_plugins.ledger',
        'electrum_ion_plugins.plot',
        'electrum_ion_plugins.trezor',
        'electrum_ion_plugins.virtualkeyboard',
    ],
    package_dir={
        'electrum_ion': 'lib',
        'electrum_ion_gui': 'gui',
        'electrum_ion_plugins': 'plugins',
    },
    package_data={
        'electrum_ion': [
            'www/index.html',
            'wordlist/*.txt',
            'locale/*/LC_MESSAGES/electrum.mo',
        ]
    },
    scripts=['electrum-ion'],
    data_files=data_files,
    description="Lightweight Ion-pay Wallet",
    author="mazaclub",
    license="MIT License",
    url="https://ionomy.com/electrum",
    long_description="""Lightweight Ion-pay Wallet"""
)
