#!flask/bin/python
from flask import Flask, jsonify
import requests

app = Flask(__name__)


def get_user_names():
    """get the current firstName and lastName from Blazemeter API"""
    url = "https://a.blazemeter.com:443/api/v4/user"

    headers = {
        'authorization': "Basic NjkyMDAyNmVjY2E3NGYwY2M0YTE4NDJjOjY3Y2RkNDNlZjBmMjU5MTA3MTEwZDRlNmQ1YzIxYzE2Y2JhYzAwMjViYTh"
                         "jY2QyZWYzN2U4YTNjZTVlODEzMDA5MjZmNTc4MA=="
    }

    response = requests.request("GET", url, headers=headers)
    response = response.json()
    # print(response)
    first_name = response["result"]["firstName"]
    last_name = response["result"]["lastName"]

    return jsonify({
        'firstName': first_name,
        'lastName': last_name
    })


def patch_user_names():
    """change the current firstName and lastName using Blazemeter API PATCH"""
    url = "https://a.blazemeter.com:443/api/v4/user"

    payload = "{\n\t\"firstName\": \"ABC\",\n    \"lastName\": \"XYZ\"\n}"
    headers = {
        'content-type': "application/json",
        'authorization': "Basic NjkyMDAyNmVjY2E3NGYwY2M0YTE4NDJjOjY3Y2RkNDNlZjBmMjU5MTA3MTEwZDRlNmQ1YzIxYzE2Y2JhYzAwMjViYThjY2QyZWYzN2U4YTNjZTVlODEzMDA5MjZmNTc4MA==",
    }

    requests.request("PATCH", url, data=payload, headers=headers)


def post_user_names():
    """change the current firstName and lastName using Blazemeter API POST"""
    url = "https://a.blazemeter.com:443/api/v4/user"

    payload = "{\n\t\"firstName\": \"API\",\n    \"lastName\": \"Tester\"\n}"
    headers = {
        'content-type': "application/json",
        'authorization': "Basic NjkyMDAyNmVjY2E3NGYwY2M0YTE4NDJjOjY3Y2RkNDNlZjBmMjU5MTA3MTEwZDRlNmQ1YzIxYzE2Y2JhYzAwMjViYThjY2QyZWYzN2U4YTNjZTVlODEzMDA5MjZmNTc4MA==",
        'cache-control': "no-cache",
        'postman-token': "4ed1b6d1-1e7a-3041-9dae-e722937dc4a8"
    }

    requests.request("POST", url, data=payload, headers=headers)


@app.route('/qa_test/api/v1.0/user', methods=['GET'])
def get_names():
    return get_user_names()


@app.route('/qa_test/api/v1.0/user', methods=['PATCH'])
def patch_names():
    patch_user_names()
    return get_user_names()


@app.route('/qa_test/api/v1.0/user', methods=['POST'])
def post_names():
    post_user_names()
    return get_user_names()


if __name__ == '__main__':
    app.run(debug=True)
