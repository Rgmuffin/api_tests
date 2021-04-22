import pytest
import requests

passed='Passed'
failed='Failed'

def logs(func_name, status, error='No errors'):
    with open('logs.log', 'a+', encoding='utf-8') as f1:
        line=f'{func_name}, {status}, {error}\n'
        f1.writelines(line)

def test_endpoint_users():
    func_name = test_endpoint_users.__name__
    resp = requests.get('http://127.0.0.1:8080/api/users')
    if resp.status_code == 200:
            logs(func_name, passed)
    else:
        logs(func_name, failed, "Response == 200")
    assert resp.status_code == 200

def test_endpoint_department():
    func_name = test_endpoint_department.__name__
    resp = requests.get('http://127.0.0.1:8080/api/department')
    if resp.status_code == 200:
            logs(func_name, passed)
    else:
        logs(func_name, failed, "Response == 200")
    assert resp.status_code == 200

def test_users_list():
    func_name = test_users_list.__name__
    r = requests.get('http://127.0.0.1:8080/api/users')
    if r.text == "data: [{'username': 'Artem R', 'email': 'artem_r@gmail.com', 'department': 'Alpha', " \
                 "'date_joined': '2020-02-11'}, {'username" \
                 "': 'Oleg T', 'email': 'oleg_t@gmail.com', 'department': 'A" \
                 "lpha', 'date_joined': '2020-02-11'}, {'username': 'Ivan S', 'email'" \
                 ": 'ivan_s@gmail.com', 'department': 'Delta', 'date_joined': '2020-02-11" \
                 "'}, {'username': 'Vladimir P', 'email': 'vladimir_p@gmail.com', 'departme" \
                 "nt': 'Delta', 'date_joined': '2020-02-11'}, {'username': 'Tatyana V', 'emai" \
                 "l': 'tatyana_v@gmail.com', 'department': 'Omega', 'date_joined': '2020-02-11'}]":
        logs(func_name, passed)
    else:
        logs(func_name, failed, "Wrong users list! and hello docker")
    assert r.text == "data: [{'username': 'Artem R', 'email': 'artem_r@gmail.com', 'department': 'Alpha', 'date_joined': '2020-02-11'}, {'username': 'Oleg T', 'email': 'oleg_t@gmail.com', 'department': 'Alpha', 'date_joined': '2020-02-11'}, {'username': 'Ivan S', 'email': 'ivan_s@gmail.com', 'department': 'Delta', 'date_joined': '2020-02-11'}, {'username': 'Vladimir P', 'email': 'vladimir_p@gmail.com', 'department': 'Delta', 'date_joined': '2020-02-11'}, {'username': '" \
                     "Tatyana V', 'email': 'tatyana_v@gmail.com'" \
                     ", 'department': 'Omega', 'date_joined': '2020-02-11'}]"

def test_user_not_exist():
    func_name = test_user_not_exist.__name__
    r = requests.get('http://127.0.0.1:8080/api/users/1')
    if r.text == "data: []":
        logs(func_name, passed)
    else:
        logs(func_name, failed, "Result must be empty!")
    assert r.text == "data: []"

def test_user_by_full_name():
    func_name = test_user_by_full_name.__name__
    r = requests.get('http://127.0.0.1:8080/api/users/Artem%20R')
    if r.text == "data: [{'username': 'Artem R', 'email': 'artem_r@gmail.com', " \
                 "'department': 'Alpha', 'date_joined': '2020-02-11'}]":
        logs(func_name, passed)
    else:
        logs(func_name, failed, "Oops, users mismatch ;(")
    assert r.text == "data: [{'username': 'Artem R', 'email': 'artem_r@gmail.com', " \
                     "'department': 'Alpha', 'date_joined': '2020-02-11'}]"

def test_username_contains():
    func_name = test_username_contains.__name__
    r = requests.get('http://127.0.0.1:8080/api/users/?username=Art')
    if r.text == "data: [{'username': 'Artem R', 'email': 'artem_r@gmail.com', 'department': 'Alpha', 'date_joined': '2020-02-11'}," \
                 " {'username': 'Arthur K', 'email': 'arthur_k@gmail.com', 'department': 'Omega', 'date_joined': '2020-02-11'}]":
        logs(func_name, passed)
    else:
        logs(func_name, failed, "Oops, users mismatch ;(")
    assert r.text == "data: [{'username': 'Artem R', 'email': 'artem_r@gmail.com', 'department': 'Alpha', 'date_joined': '2020-02-11'}," \
                     " {'username': 'Arthur K', 'email': 'arthur_k@gmail.com', 'department': 'Omega', 'date_joined': '2020-02-11'}]"

def test_department_list():
    func_name = test_department_list.__name__
    r = requests.get('http://127.0.0.1:8080/api/department')
    if r.text == "List of Departments: ['Alpha', 'Delta', 'Omega']":
        logs(func_name, passed)
    else:
        logs(func_name, failed, "Wrong list of departments (")
    assert r.text == "List of Departments: ['Alpha', 'Delta', 'Omega']"

def test_department_full():
    func_name = test_department_full.__name__
    r = requests.get('http://127.0.0.1:8080/api/department/?name=Alpha')
    if r.text == "Similar with Alpha: Alpha":
        logs(func_name, passed)
    else:
        logs(func_name, failed, "Wrong list of departments (")
    assert r.text == "Similar with Alpha: Alpha"

def test_department_contains():
    func_name = test_department_contains.__name__
    r = requests.get('http://127.0.0.1:8080/api/department/?name=Del')
    if r.text == "Similar with Del: Delta":
        logs(func_name, passed)
    else:
        logs(func_name, failed, "Wrong list of departments (")
    assert r.text == "Similar with Del: Delta"

def test_username_with_department():
    func_name = test_username_with_department.__name__
    r = requests.get('http://127.0.0.1:8080/api/users/?username=Art&department=Alpha')
    if r.text == "data: [{'username': 'Artem R', 'email': 'artem_r@gmail.com', 'department': 'Alpha', 'date_joined': '2020-02-11'}]":
        logs(func_name, passed)
    else:
        logs(func_name, failed, "Oops, users mismatch ;(")
    assert r.text == "data: [{'username': 'Artem R', 'email': 'artem_r@gmail.com', 'department': 'Alpha', 'date_joined': '2020-02-11'}]"