import requests


class api:

    def __init__(self, url, header=None, data=None, file=None, params=None):

        if url is None:
            print("Please add api Url")
        else:
            self.__url = url
        if header is not None:
            self.__header = header
        else:
            self.__header = None

        if header is not None:
            self.__data = data
        else:
            self.__data = None

        if file is not None:
            self.__file = file
        else:
            self.__file = None

        if params is not None:
            self.__params = params
        else:
            self.__params = None

    def get_request(self):
        with requests.get(self.__url, headers=self.__header, data=self.__data, files=self.__file,
                                 params=self.__params) as response:
            return response

    def post_request(self, api_client):
        with requests.post(self.__url, headers=self.__header, data=self.__data, files=self.__file,
                             params=self.__params) as response:
            return response

    def put_request(self, api_client):
        with requests.put(self.__url, headers=self.__header, data=self.__data, files=self.__file,
                            params=self.__params) as response:
            return response

    def delete_request(self, api_client):
        with requests.delete(self.__url, headers=self.__header, data=self.__data, files=self.__file,
                               params=self.__params) as response:
            return response

    def option_request(self, api_client):
        with requests.options(self.__url, headers=self.__header, data=self.__data, files=self.__file,
                                params=self.__params) as response:
            return response

    def patch_request(self, api_client):
        with requests.patch(self.__url, headers=self.__header, data=self.__data, files=self.__file,
                              params=self.__params) as response:
            return response
