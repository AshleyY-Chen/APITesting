import requests
import json
import jsonpath

def test_add_student_data():
    student_url = "http://thetestingworldapi.com/api/Students"
    file = open('C:/Users/yingh/PycharmProjects/StudentAPIAutomation/NewStudent.json','r')
    json_request = json.loads(file.read())
    response = requests.post(student_url, json_request)
    id = jsonpath.jsonpath(response.json(), "id")


    tech_api_url = "http://thetestingworldapi.com/api/technicalskills"
    file = open('C:/Users/yingh/PycharmProjects/StudentAPIAutomation/NewTechnial.json','r')
    json_request = json.loads(file.read())
    json_request["id"] = int(id[0])
    json_request["st_id"] = id[0]
    response = requests.post(tech_api_url,json_request)

    address_url = "http://thetestingworldapi.com/api/addresses"
    file = open('C:/Users/yingh/PycharmProjects/StudentAPIAutomation/NewAddress.json', 'r')
    json_request = json.loads(file.read())
    json_request["stId"] = id[0]
    response = requests.post(address_url, json_request)

    final_detail_url = "http://thetestingworldapi.com/api/FinalStudentDetails/" + str(id[0])
    response = requests.get(final_detail_url)
    print(response.text)