# SteamActivityTracker

**SteamActivityTracker** - это утилита для отслеживания активности пользователей Steam. Программа позволяет мониторить статус пользователя, его текущую игру, а также активность его друзей для определения совместной игры. Вся информация записывается в лог-файл для последующего анализа.

## Требования

- Python 3.x
- Установленные пакеты:
  - `configparser`
  - `requests`
  - `colorama`

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/badxprogramm/SteamActivityTracker.git
   ```
   ```bash
    cd SteamActivityTracker
   ```
2. Установите необходимые пакеты:
   ```bash
   pip install -r requirements.txt
   ```

## Настройка

1. При первом запуске программа создаст файл конфигурации `config.ini` в текущей директории, никому не передавайте этот файл.
2. Введите свой Steam API ключ, когда программа запросит его.

## Использование

1. Запустите программу:

   ```bash
   python main.py
   ```
2. Следуйте инструкциям на экране:
   - Введите URL профиля Steam, который вы хотите отслеживать.
   - Выберите метод отслеживания:
     - `1` для отслеживания только активности цели.
     - `2` для отслеживания активности цели и её друзей.
   - Введите интервал проверки в секундах.

## Прерывание

Чтобы остановить программу, нажмите `Ctrl+C`.

## Пример вывода

```

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

Введите ваш Steam API ключ: [ваш ключ]
Введите URL профиля Steam: https://steamcommunity.com/id/username/
Выберите метод отслеживания:
1. Отслеживание только активности цели.
2. Отслеживание активности цели и её друзей для определения совместной игры.
Введите номер метода отслеживания (1 или 2): 1
Введите интервал проверки в секундах (например, 10): 10
Начало отслеживания. Нажмите Ctrl+C для выхода.
```

## Описание функций

- **get_config**: Получение объекта конфигурации. Если файл конфигурации не существует, создается новый.
- **create_default_config**: Создание файла конфигурации с пустым значением для API ключа.
- **set_steam_api_key**: Установка Steam API ключа в конфигурационном файле.
- **get_steam_api_key**: Получение Steam API ключа из конфигурационного файла.
- **setup_config**: Настройка конфигурационного файла. Запрашивает API ключ у пользователя, если он не указан.
- **print_welcome_message**: Печать приветственного сообщения с цветами.
- **get_tracking_method**: Получение метода отслеживания от пользователя.
- **sanitize_filename**: Удаление недопустимых символов из имени файла.
- **write_status_to_file**: Запись сообщения в файл отслеживания.
- **log_new_tracking**: Запись разрыва в файл отслеживания.
- **Tracker**: Основной класс для отслеживания активности пользователя.
  - **extract_user_id**: Извлечение Steam ID из кастомного URL профиля Steam.
  - **get_username**: Получение имени пользователя.
  - **get_friends**: Получение списка друзей пользователя.
  - **get_player_summaries**: Получение информации о пользователях.
  - **check_status**: Проверка текущего статуса пользователя и запись в лог.
- **main**: Основная функция программы.
#
# EN


# SteamActivityTracker

**SteamActivityTracker** is a utility for tracking Steam users' activity. The program allows you to monitor a user's status, their current game, and their friends' activities to identify potential joint gaming opportunities. All information is logged into a file for later analysis.

## Requirements

- Python 3.x
- Installed packages:
  - `configparser`
  - `requests`
  - `colorama`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/badxprogramm/SteamActivityTracker.git
   ```
   ```bash
    cd SteamActivityTracker
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. On the first run, the program will create a `config.ini` file in the current directory. Do not share this file with anyone.
2. Enter your Steam API key when prompted by the program.

## Usage

1. Run the program:

   ```bash
   python main.py
   ```
2. Follow the on-screen instructions:
   - Enter the Steam profile URL you want to track.
   - Choose the tracking method:
     - `1` for tracking only the target's activity.
     - `2` for tracking the target's and their friends' activity.
   - Enter the check interval in seconds.

## Stopping the Program

To stop the program, press `Ctrl+C`.

## Sample Output

```

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

Enter your Steam API key: [your key]
Enter Steam profile URL: https://steamcommunity.com/id/username/
Choose tracking method:
1. Track only the target's activity.
2. Track the target's and their friends' activity for joint gaming opportunities.
Enter tracking method number (1 or 2): 1
Enter check interval in seconds (e.g., 10): 10
Starting tracking. Press Ctrl+C to exit.
```

## Function Descriptions

- **get_config**: Retrieves the configuration object. If the configuration file does not exist, a new one is created.
- **create_default_config**: Creates a configuration file with an empty value for the API key.
- **set_steam_api_key**: Sets the Steam API key in the configuration file.
- **get_steam_api_key**: Retrieves the Steam API key from the configuration file.
- **setup_config**: Configures the configuration file. Prompts the user for the API key if it is not provided.
- **print_welcome_message**: Prints a welcome message with colors.
- **get_tracking_method**: Gets the tracking method from the user.
- **sanitize_filename**: Removes invalid characters from the filename.
- **write_status_to_file**: Writes a message to the tracking file.
- **log_new_tracking**: Logs a break in the tracking file.
- **Tracker**: The main class for tracking user activity.
  - **extract_user_id**: Extracts the Steam ID from a custom Steam profile URL.
  - **get_username**: Retrieves the username.
  - **get_friends**: Retrieves the user's friends list.
  - **get_player_summaries**: Retrieves information about users.
  - **check_status**: Checks the user's current status and logs it.
- **main**: The main function of the program.
