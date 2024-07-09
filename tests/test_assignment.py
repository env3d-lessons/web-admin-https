import os
import pathlib
import pytest

@pytest.fixture
def my_server_name():
    server_name = os.popen("sudo apachectl -S | grep -o -P '\\S+wmdd4950.com'").read()
    if not pathlib.Path('server_name.txt').is_file():
        f = open('server_name.txt','w')
        f.write(server_name)
        f.close()

    return open('server_name.txt').read().strip()


def test_server_name(my_server_name):
    assert len(my_server_name) > 0


def test_http(my_server_name):
    content = os.popen(f'curl -s --head http://{my_server_name}').read()
    assert '301' in content

def test_https(my_server_name):
    content = os.popen(f'curl -s --head https://{my_server_name}').read()
    assert '200' in content
    
