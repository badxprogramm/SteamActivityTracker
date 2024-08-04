import configparser
import os
import time
import sys
import requests
from datetime import datetime
from typing import Optional, Dict, List
from colorama import Fore, Style, init

# Инициализация colorama
init(autoreset=True)

CONFIG_FILE = 'config.ini'

def get_config() -> configparser.ConfigParser:
    """
    Получение объекта конфигурации. Если файл конфигурации не существует, создается новый.
    
    :return: Объект конфигурации.
    """
    config = configparser.ConfigParser()
    if not os.path.exists(CONFIG_FILE):
        create_default_config(config)
    config.read(CONFIG_FILE)
    return config

def create_default_config(config: configparser.ConfigParser) -> None:
    """
    Создание файла конфигурации с пустым значением для API ключа.
    
    :param config: Объект конфигурации.
    """
    config['Steam'] = {
        'API_KEY': ''
    }
    with open(CONFIG_FILE, 'w') as configfile:
        config.write(configfile)

def set_steam_api_key(api_key: str) -> None:
    """
    Установка Steam API ключа в конфигурационном файле.
    
    :param api_key: Steam API ключ.
    """
    config = get_config()
    config['Steam']['API_KEY'] = api_key
    with open(CONFIG_FILE, 'w') as configfile:
        config.write(configfile)

def get_steam_api_key() -> str:
    """
    Получение Steam API ключа из конфигурационного файла.
    
    :return: Steam API ключ.
    """
    config = get_config()
    return config.get('Steam', 'API_KEY', fallback='')

def setup_config() -> None:
    """
    Настройка конфигурационного файла. Запрашивает API ключ у пользователя, если он не указан.
    """
    api_key = get_steam_api_key()
    if not api_key:
        api_key = input("Введите ваш Steam API ключ: ")
        set_steam_api_key(api_key)

def print_welcome_message():
    """
    Печать приветственного сообщения с цветами.
    """
    message = '''
▄▄▄▄    ▄▄▄      ▓█████▄  ▒██   ██▒ ███▄ ▄███▓ ▄▄▄     ▄▄▄█████▓▄▄▄██▄▄▄▓
▓█████▄ ▒████▄    ▒██▀ ██▌▒▒ █ █ ▒░▓██▒▀█▀ ██▒▒████▄   ▓  ██▒ ▓▒▓  ██▒ ▓▒
▒██▒ ▄██▒██  ▀█▄  ░██   █▌░░  █   ░▓██    ▓██░▒██  ▀█▄ ▒ ▓██░ ▒░▒ ▓██░ ▒░
▒██░█▀  ░██▄▄▄▄██ ░▓█▄   ▌ ░ █ █ ▒ ▒██    ▒██ ░██▄▄▄▄██░ ▓██▓ ░ ░ ▓██▓ ░ 
░▓█  ▀█▓ ▓█   ▓██▒░▒████▓ ▒██▒ ▒██▒▒██▒   ░██▒ ▓█   ▓██▒ ▒██▒ ░   ▒██▒ ░ 
░▒▓███▀▒ ▒▒   ▓▒█░ ▒▒▓  ▒ ▒▒ ░ ░▓ ░░ ▒░   ░  ░ ▒▒   ▓▒█░ ▒ ░░     ▒ ░░   
▒░▒   ░   ▒   ▒▒ ░ ░ ▒  ▒ ░░   ░▒ ░░  ░      ░  ▒   ▒▒ ░   ░        ░    
 ░    ░   ░   ▒    ░ ░  ░  ░    ░  ░      ░     ░   ▒    ░        ░      
 ░            ░  ░   ░     ░    ░         ░         ░  ░                 
      ░            ░
'''
    # Печатаем сообщение по строкам с задержкой
    for line in message.split('\n'):
        print(line)
        time.sleep(0.1)

    # Мерцание красным и белым
    for _ in range(6):
        sys.stdout.write(Fore.RED + message + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write(Fore.WHITE + message + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(0.1)

def get_tracking_method() -> int:
    """
    Получение метода отслеживания от пользователя.
    
    :return: Выбранный метод отслеживания (1 или 2).
    """
    print("Выберите метод отслеживания:")
    print("1. Отслеживание только активности цели.")
    print("2. Отслеживание активности цели и её друзей для определения совместной игры.")
    
    while True:
        try:
            choice = int(input("Введите номер метода отслеживания (1 или 2): "))
            if choice in [1, 2]:
                return choice
            else:
                print("Некорректный выбор. Пожалуйста, введите 1 или 2.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.")

def sanitize_filename(filename: str) -> str:
    """
    Удаление недопустимых символов из имени файла.
    
    :param filename: Исходное имя файла.
    :return: Очищенное имя файла.
    """
    # Список недопустимых символов для Windows
    invalid_chars = '<>:"/\\|?*'
    sanitized = ''.join(char for char in filename if char not in invalid_chars)
    return sanitized

def write_status_to_file(filename: str, message: str) -> None:
    """
    Запись сообщения в файл отслеживания.
    
    :param filename: Имя файла.
    :param message: Сообщение для записи.
    """
    with open(filename, 'a') as file:
        file.write(message + '\n')

def log_new_tracking(filename: str) -> None:
    """
    Запись разрыва в файл отслеживания.
    
    :param filename: Имя файла.
    """
    now = datetime.now()
    timestamp = now.strftime('%d.%m.%Y %H:%M:%S')
    separator = '-' * 10
    message = f"{separator} Новое отслеживание {timestamp} {separator}"
    write_status_to_file(filename, message)

class Tracker:
    def __init__(self, profile_url: str, api_key: str, tracking_method: int) -> None:
        """
        Инициализация Tracker.
        
        :param profile_url: URL профиля Steam.
        :param api_key: API ключ Steam.
        :param tracking_method: Метод отслеживания (1 или 2).
        """
        self.profile_url = profile_url
        self.api_key = api_key
        self.tracking_method = tracking_method
        self.previous_status = None
        self.previous_game = None
        self.user_id = self.extract_user_id(profile_url)
        self.log_filename = sanitize_filename(self.get_username()) + ".txt"
        log_new_tracking(self.log_filename)  # Добавляем разрыв при создании нового файла
        print(f"User ID: {self.user_id}")
        print(f"Log Filename: {self.log_filename}")

    def extract_user_id(self, profile_url: str) -> str:
        """
        Извлечение Steam ID из кастомного URL профиля Steam.
        
        :param profile_url: URL профиля Steam.
        :return: Steam ID пользователя.
        """
        custom_url = profile_url.split('/')[-2]
        try:
            response = requests.get(f"https://api.steampowered.com/ISteamUser/ResolveVanityURL/v1/?key={self.api_key}&vanityurl={custom_url}")
            response.raise_for_status()  # Проверка на успешный ответ
            data = response.json()

            if data.get('response', {}).get('success') == 1:
                return data['response'].get('steamid', 'Unknown')
            else:
                print("Не удалось разрешить кастомный URL. Проверьте правильность URL.")
                return 'Unknown'
        
        except (requests.RequestException, KeyError) as e:
            print(f"Ошибка при извлечении Steam ID: {e}")
            return 'Unknown'

    def get_username(self) -> str:
        """
        Получение имени пользователя.
        
        :return: Имя пользователя или пустая строка, если не удается получить данные.
        """
        try:
            response = requests.get(f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key={self.api_key}&steamids={self.user_id}")
            response.raise_for_status()  # Проверка на успешный ответ
            data = response.json()

            players = data.get('response', {}).get('players', [])
            if not players:
                print("Игрок не найден в get_username.")
                return "Unknown"

            return players[0].get('personaname', "Unknown")
        
        except (requests.RequestException, KeyError) as e:
            print(f"Ошибка при получении имени пользователя: {e}")
            return "Unknown"

    def get_friends(self) -> List[str]:
        """
        Получение списка друзей пользователя.
        
        :return: Список Steam ID друзей.
        """
        url = f"https://api.steampowered.com/ISteamUser/GetFriendList/v1/?key={self.api_key}&steamid={self.user_id}&relationship=friend"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return [friend['steamid'] for friend in data.get('friendslist', {}).get('friends', [])]
        else:
            print(f"Ошибка получения списка друзей: {response.status_code}")
            return []

    def get_player_summaries(self, steamids: List[str]) -> Dict[str, Dict]:
        """
        Получение информации о пользователях.
        
        :param steamids: Список Steam ID пользователей.
        :return: Словарь с информацией о пользователях.
        """
        steamids_str = ",".join(steamids)
        url = f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key={self.api_key}&steamids={steamids_str}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return {player['steamid']: player for player in data.get('response', {}).get('players', [])}
        else:
            print(f"Ошибка получения информации о пользователях: {response.status_code}")
            return {}

    def check_status(self) -> None:
        """
        Проверка текущего статуса пользователя и запись в лог.
        """
        try:
            response = requests.get(f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key={self.api_key}&steamids={self.user_id}")
            response.raise_for_status()  # Проверка на успешный ответ
            data = response.json()

            players = data.get('response', {}).get('players', [])
            if not players:
                print("Игрок не найден в check_status.")
                return

            player = players[0]

            current_status = player.get('personastate', 0)
            current_game = player.get('gameextrainfo', None)

            now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

            # Проверка текущего статуса игрока
            if current_status == 1:
                status_message = f"{now} Пользователь онлайн."
                if current_game:
                    status_message += f" В игре {current_game}."
            else:
                status_message = f"{now} Пользователь не онлайн."

            if self.previous_status is not None:
                if current_status == 1 and self.previous_status == 0:
                    status_message = f"{now} Пользователь зашел в онлайн. (!!!)"
                elif current_status == 0 and self.previous_status == 1:
                    status_message = f"{now} Пользователь вышел из онлайна. (!!!)"
                elif current_status == 1 and current_game != self.previous_game:
                    if self.previous_game:
                        if current_game:
                            status_message = f"{now} Пользователь онлайн, сменил игру {self.previous_game} на {current_game}. (!!!)"
                        else:
                            status_message = f"{now} Пользователь онлайн, вышел из игры {self.previous_game}. (!!!)"
                    else:
                        status_message = f"{now} Пользователь онлайн, зашел в игру {current_game}. (!!!)"
                elif current_status == 1 and self.previous_game and not current_game:
                    status_message = f"{now} Пользователь онлайн, вышел из игры {self.previous_game}. (!!!)"

            self.previous_status = current_status
            self.previous_game = current_game

            # Проверка, играют ли друзья вместе (если выбран метод 2)
            if self.tracking_method == 2:
                friends = self.get_friends()
                if friends:
                    player_summaries = self.get_player_summaries([self.user_id] + friends)
                    if player_summaries:
                        for friend_id, summary in player_summaries.items():
                            if friend_id != self.user_id:
                                friend_game = summary.get('gameextrainfo', None)
                                if friend_game == current_game:
                                    # Сравнение времени входа в игру
                                    friend_last_online = summary.get('lastlogoff', None)
                                    if friend_last_online:
                                        last_online_time = datetime.fromtimestamp(int(friend_last_online))
                                        if abs((datetime.now() - last_online_time).total_seconds()) <= 600:
                                            status_message += f" Друг {friend_id} тоже онлайн в той же игре {current_game}."

            # Запись в лог файл
            write_status_to_file(self.log_filename, status_message)
            print(status_message)
        
        except (requests.RequestException, KeyError) as e:
            print(f"Ошибка при получении статуса пользователя: {e}")

def main():
    # Печать приветственного сообщения
    print_welcome_message()
    
    # Настройка конфигурационного файла
    setup_config()
    
    api_key = get_steam_api_key()
    
    if not api_key:
        print("Не указан API ключ.")
        return
    
    profile_url = input("Введите URL профиля Steam: ")
    
    tracking_method = get_tracking_method()
    
    interval = input("Введите интервал проверки в секундах (например, 10): ")
    
    try:
        interval = int(interval)
    except ValueError:
        print("Неверный формат интервала. Устанавливается значение по умолчанию: 10 секунд.")
        interval = 10
    
    tracker = Tracker(profile_url, api_key, tracking_method)
    print("Начало отслеживания. Нажмите Ctrl+C для выхода.")
    
    try:
        while True:
            start_time = time.time()
            tracker.check_status()
            elapsed_time = time.time() - start_time
            sleep_time = max(0, interval - elapsed_time)  # Учитываем интервал
            time.sleep(sleep_time)
    except KeyboardInterrupt:
        print("Программа завершена пользователем.")

if __name__ == "__main__":
    main()
