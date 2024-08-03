import unittest
import requests

# Замените 'TOKEN' на ваш реальный OAuth-токен
OAUTH_TOKEN = 'TOKEN'
BASE_URL = 'https://cloud-api.yandex.net/v1/disk/resources'


class TestYandexDiskAPI(unittest.TestCase):

    def setUp(self):
        # Основной заголовок для авторизации
        self.headers = {
            'Authorization': f'OAuth {OAUTH_TOKEN}'
        }
        self.folder_path = 'test_folder'

    def test_create_folder(self):
        # Тест создания папки
        response = requests.put(f'{BASE_URL}?path={self.folder_path}', headers=self.headers)
        self.assertEqual(response.status_code, 201, "Папка не была создана. Ожидался код 201.")

        # Проверка, что папка действительно была создана
        response = requests.get(f'{BASE_URL}?path={self.folder_path}', headers=self.headers)
        self.assertEqual(response.status_code, 200, "Папка не была найдена после создания.")
        json_response = response.json()
        self.assertIn('name', json_response)
        self.assertEqual(json_response['name'], self.folder_path)

    def test_create_existing_folder(self):
        # Тест попытки создания папки, которая уже существует
        requests.put(f'{BASE_URL}?path={self.folder_path}', headers=self.headers)  # Создаем папку заранее

        response = requests.put(f'{BASE_URL}?path={self.folder_path}', headers=self.headers)
        self.assertEqual(response.status_code, 409, "Ожидался код 409 при создании уже существующей папки.")

    def test_create_folder_invalid_name(self):
        # Тест создания папки с недопустимым именем
        invalid_folder_name = 'test/folder'  # Слэш может быть недопустимым символом в имени папки

        response = requests.put(f'{BASE_URL}?path={invalid_folder_name}', headers=self.headers)
        self.assertEqual(response.status_code, 400, "Ожидался код 400 при создании папки с недопустимым именем.")

    def test_invalid_authorization(self):
        # Тест использования неверного OAuth-токена
        invalid_headers = {
            'Authorization': 'OAuth неверный токен'
        }
        response = requests.put(f'{BASE_URL}?path={self.folder_path}', headers=invalid_headers)
        self.assertEqual(response.status_code, 401, "Ожидался код 401 при неверной авторизации.")

    def tearDown(self):
        # Удаление тестовой папки после тестов (только если тест прошел успешно)
        requests.delete(f'{BASE_URL}?path={self.folder_path}', headers=self.headers)


if __name__ == '__main__':
    unittest.main()

