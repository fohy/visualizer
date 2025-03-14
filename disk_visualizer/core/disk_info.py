import os
import shutil
import subprocess

class DiskInfo:
    """Получает информацию о дисковом пространстве."""

    def __init__(self, path="/"):
        """Инициализирует путь к диску."""
        self.path = path

    def get_usage(self):
        """Возвращает общий, использованный и свободный объем диска в байтах."""
        if not os.path.exists(self.path):
            raise FileNotFoundError(f"Ошибка: путь {self.path} не существует.")

        if os.name == "nt":  # Windows
            total, used, free = shutil.disk_usage(self.path)
        else:  # Linux/macOS
            try:
                result = subprocess.run(["df", "-B1", self.path], capture_output=True, text=True, check=True)
                data = result.stdout.split("\n")[1].split()
                total, used, free = int(data[1]), int(data[2]), int(data[3])
            except Exception as e:
                raise RuntimeError(f"Ошибка получения данных: {e}")

        return total, used, free
