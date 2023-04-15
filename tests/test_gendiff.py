from gendiff import generate_diff


def test_generate_diff():
    file_path1 = 'file1.json'
    file_path2 = 'file2.json'
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
    file_path1 = 'file1.json'
    file_path2 = 'file1.json'
    diff = generate_diff(file_path1, file_path2)
    expected_output = '''{
    follow: false
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}'''
    assert diff == expected_output


def test_generate_diff3():
    file_path1 = 'file1.json'
    file_path2 = 'file3.json'
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
    file_path1 = 'file1.json'
    file_path2 = 'file4.json'
    diff = generate_diff(file_path1, file_path2)
    expected_output = '''{
  - follow: false
  - host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
}'''
    assert diff == expected_output
