import requests
import json
import jsonpath


def test_add_student_data():
    url = "http://thetestingworldapi.com/api/Students"
    file = open('C:\\Users\\yingh\\PycharmProjects\\StudentAPIAutomation\\NewStudent.json', 'r')
    str1 = file.read()
    json_request = json.loads(str1)
    print(json_request)
    response = requests.post(url, json_request)
    print(response.status_code)
    print(response.text)


def get_student_data():
    url = "http://thetestingworldapi.com/api/Students/3034"
    response = requests.get(url)
    json_response = json.loads(response)
    id = jsonpath.jsonpath(json_response,'data.id')
    assert id[0] == 3034

def test_update_student_data():
    url = "http://thetestingworldapi.com/api/Students/3034"
    file = open('C:\\Users\\yingh\\PycharmProjects\\StudentAPIAutomation\\NewStudent.json', 'r')
    str1 = file.read()
    json_request = json.loads(str1)
    print(json_request)
    response = requests.put(url, json_request)
    print(response.status_code)
    print(response.text)