from fabric.api import local

def init():
    local('virtualenv --no-site-packages .')
    local('source bin/activate; pip install -r requirements.pip')
