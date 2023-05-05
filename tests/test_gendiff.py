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


def test_generate_diff_yaml_json():
    file_path1 = os.path.join(os.path.dirname(__file__), 'file1.json')
    file_path2 = os.path.join(os.path.dirname(__file__), 'yml_file2.yaml')
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


def test_generate_diff_yaml():
    file_path1 = os.path.join(os.path.dirname(__file__), 'yml_file1.yaml')
    file_path2 = os.path.join(os.path.dirname(__file__), 'yml_file2.yaml')
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


def test_generate_diff4():
    file_path1 = os.path.join(os.path.dirname(__file__), 'file5big.json')
    file_path2 = os.path.join(os.path.dirname(__file__), 'file6big.json')
    diff = generate_diff(file_path1, file_path2)
    expected_output = '''{
    common: {
  + follow: false
    setting1: Value 1
  - setting2: 200
  - setting3: true
  + setting3: None
  + setting4: blah blah
  + setting5: {
    key5: value5
}
    setting6: {
    doge: {
  - wow: 
  + wow: so much
}
    key: value
  + ops: vops
}
}
    group1: {
  - baz: bas
  + baz: bars
    foo: bar
  - nest: {
    key: value
}
  + nest: str
}
  - group2: {
    abc: 12345
    deep: {
        id: 45
    }
}
  + group3: {
    deep: {
        id: {
            number: 45
        }
    }
    fee: 100500
}
}'''
    assert diff == expected_output
