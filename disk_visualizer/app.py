import argparse
from disk_visualizer.core import DiskInfo, DiskVisualizer


class DiskUsageApp:
    """Основной класс приложения для работы с аргументами и запуском программы."""

    def __init__(self):
        """Инициализирует парсер аргументов."""
        self.parser = argparse.ArgumentParser(description="Визуализатор свободного места на диске.")
        self.parser.add_argument("-p", "--path", type=str, default="/", help="Путь к диску (по умолчанию корневой '/').")

    def run(self):
        """Запускает программу, получает данные и строит график."""
        args = self.parser.parse_args()

        try:
            disk_info = DiskInfo(args.path)
            total, used, free = disk_info.get_usage()

            print(f"Диск: {args.path}")
            print(f"Общий размер: {total / (1024 ** 3):.2f} ГБ")
            print(f"Использовано: {used / (1024 ** 3):.2f} ГБ")
            print(f"Свободно: {free / (1024 ** 3):.2f} ГБ")

            DiskVisualizer.plot_disk_usage(total, used, free)

        except Exception as e:
            print(f"Ошибка: {e}")
