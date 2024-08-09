from Utils import api_methods as ap


def test_api(api_client):
    url = "https://reqres.in/api/users?page=2"
    request = ap.api(url=url, header=None, data=None, file=None, params=None)
    res = request.get_request()
    print(res.status_code)
