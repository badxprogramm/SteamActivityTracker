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
   git clone https://github.com/yourusername/SteamActivityTracker.git
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
