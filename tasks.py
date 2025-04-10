"""
Pelican tasks.py for automation
"""

import os
import shutil
import sys
from invoke import task
from invoke.main import program
from pelican import main as pelican_main
from pelican.server import ComplexHTTPRequestHandler, RootedHTTPServer
from pelican.settings import DEFAULT_CONFIG, get_settings_from_file

SETTINGS_FILE_BASE = 'pelicanconf.py'
SETTINGS = {}
SETTINGS.update(DEFAULT_CONFIG)
LOCAL_SETTINGS = get_settings_from_file(SETTINGS_FILE_BASE)
SETTINGS.update(LOCAL_SETTINGS)

CONFIG = {
    'settings_base': SETTINGS_FILE_BASE,
    'settings_publish': 'publishconf.py',
    'deploy_path': 'output',
    'host': 'localhost',
    'port': 8000,
}

@task
def clean(c):
    """Remove generated files"""
    if os.path.isdir(CONFIG['deploy_path']):
        shutil.rmtree(CONFIG['deploy_path'])
        os.makedirs(CONFIG['deploy_path'])

@task
def build(c):
    """Build local version of site"""
    pelican_main(['-s', CONFIG['settings_base']])

@task
def rebuild(c):
    """`clean` then `build`"""
    clean(c)
    build(c)

@task
def regenerate(c):
    """Automatically regenerate site upon file modification"""
    pelican_main(['-r', '-s', CONFIG['settings_base']])

@task
def serve(c):
    """Serve site at http://localhost:8000/"""
    from pelican.server import ComplexHTTPRequestHandler, RootedHTTPServer

    class AddressReuseTCPServer(RootedHTTPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(
        CONFIG['deploy_path'],
        (CONFIG['host'], CONFIG['port']),
        ComplexHTTPRequestHandler)

    sys.stderr.write('Serving on {host}:{port} ...\n'.format(**CONFIG))
    server.serve_forever()

@task
def reserve(c):
    """`build`, then `serve`"""
    build(c)
    serve(c)

@task
def preview(c):
    """Build production version of site"""
    pelican_main(['-s', CONFIG['settings_publish']])

@task
def publish(c):
    """Publish to production via rsync"""
    pelican_main(['-s', CONFIG['settings_publish']])
    # Add your deployment commands here
    # Example: c.run('rsync -e "ssh -p {ssh_port}" -P -rvzc --delete {deploy_path}/ {ssh_user}@{ssh_host}:{document_root}'.format(**CONFIG)) 