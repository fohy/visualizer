import os
import psutil

class DiskInfo:
    """Получает информацию о дисковом пространстве."""

    def __init__(self, path="/"):
        """Инициализирует путь к диску."""
        self.path = path

    def get_usage(self):
        """Возвращает общий, использованный и свободный объем диска в байтах."""
        if not os.path.exists(self.path):
            raise FileNotFoundError(f"Ошибка: путь {self.path} не существует.")

        try:
            """Получаем информацию о диске"""
            usage = psutil.disk_usage(self.path)
            total = usage.total
            used = usage.used
            free = usage.free
        except Exception as e:
            raise RuntimeError(f"Ошибка получения данных: {e}")

        return total, used, free