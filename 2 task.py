import requests
import os


class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def upload(self, file_path):
        # Функция загружает все файлы из указанного каталога
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        for i, file in enumerate(file_path):
            params = {'path': f'/Загрузки/{file}', 'overwrite': True}
            response_url = requests.get(upload_url, headers=headers, params=params)
            href = response_url.json().get('href', '')
            response = requests.put(href, data=open(directory + file, 'rb'))
            if response.status_code == 201:
                print(f'{i + 1}/{len(file_path)} {file} uploaded!')
            else:
                print(f'{file} {response.status_code}')


if __name__ == '__main__':
    directory = 'C:\\netology\\'
    file_path = os.listdir('C:\\netology\\')
    token = '---'
    uploader = YaUploader(token)
    result = uploader.upload(file_path)


# class YaUploader:
#     def __init__(self, token):
#         self.token = token
#
#     def get_headers(self):
#         return {
#             'Content-Type': 'application/json',
#             'Authorization': 'OAuth {}'.format(self.token)
#         }
#
#
#     def upload_url (self, file_path):
#         # file_path = os.path.normpath(file_path)
#         # print(file_path)
#         upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
#         headers = self.get_headers()
#         params = {'path': '/Загрузки/test.txt', 'overwrite': True}
#         response = requests.get(upload_url, headers=headers, params=params)
#         if response.status_code != 200:
#             print(response.status_code)
#         return response.json()
#
#
#     def upload_file (self, file_path):
#             href = self.upload_url(file_path).get('href', '')
#             response = requests.put(href, data=open(file_path, 'rb'))
#             if response.status_code == 201:
#                 print('Success!')
#             else:
#                 print(response.status_code)
#
#
# if __name__ == '__main__':
#     file_path = os.listdir('C:\\netology\\test.txt'
#     token = '---'
#     uploader = YaUploader(token)
#     result = uploader.upload_file(file_path)
