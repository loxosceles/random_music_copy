import pytest

#import crm

def test_get_dir_size(tmpdir):
    a_sub_dir = tmpdir.mkdir('testdir')
    a_file = tmpdir.join('sometext.txt')
    assert a_sub_dir + a_file




