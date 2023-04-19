from gendiff.gendiff import generate_diff
import os


def test_generate_diff():
    file_path1 = os.path.join(os.path.dirname(__file__), 'file1.json')
    file_path2 = os.path.join(os.path.dirname(__file__), 'file2.json')
    diff = generate_diff(file_path1, file_path2)
    expected_output = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''
    assert diff == expected_output


def test_generate_diff2():
    file_path1 = os.path.join(os.path.dirname(__file__), 'file1.json')
    file_path2 = os.path.join(os.path.dirname(__file__), 'file1.json')
    diff = generate_diff(file_path1, file_path2)
    expected_output = '''{
    follow: false
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}'''
    assert diff == expected_output


def test_generate_diff3():
    file_path1 = os.path.join(os.path.dirname(__file__), 'file1.json')
    file_path2 = os.path.join(os.path.dirname(__file__), 'file3.json')
    diff = generate_diff(file_path1, file_path2)
    expected_output = '''{
  - follow: false
  + hoist: hexlet.io
  - host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeowt: 20
  + verboose: true
}'''
    assert diff == expected_output


def test_generate_diff_emptyfile():
    file_path1 = os.path.join(os.path.dirname(__file__), 'file1.json')
    file_path2 = os.path.join(os.path.dirname(__file__), 'file4.json')
    diff = generate_diff(file_path1, file_path2)
    expected_output = '''{
  - follow: false
  - host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
}'''
    assert diff == expected_output
