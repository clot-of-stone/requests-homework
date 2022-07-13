import requests


class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_upload_link(self, yadisk_path):
        link = ''
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Authorization': f'OAuth {self.token}', 'Content-Type': 'application/json'}
        params = {'path': yadisk_path, 'overwrite': True}
        response = requests.get(url, params, headers=headers)
        if response.status_code != 200:
            print(response.text)
        else:
            response_json = response.json()
            link = response_json['href']
        return link

    def upload(self, file_path, file_name):
        upload_link = self.get_upload_link(file_name)
        if upload_link != "":
            with open(file_path) as object:
                response = requests.put(upload_link, object)
                if response.status_code == 201:
                    print('Успешно загружено!')
                else:
                    print('Что-то пошло не так...\n', response.text)


if __name__ == '__main__':
    relative_file_path = 'YAUPLOAD/new_file_hw_requests.txt'  # Ввести относительный путь к файлу, в кавычках
    file_name = 'new_file_hw_requests.txt'  # Ввести название файла с указанием расширения, в кавычках
    token = ''  # Ввести токен для доступа к API Яндекс.Диска, в кавычках
    file = YaUploader(token)
    file.upload(file_path=relative_file_path, file_name=file_name)
