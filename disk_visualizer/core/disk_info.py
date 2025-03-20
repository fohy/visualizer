import subprocess

class DiskInfo:
    """Получает информацию о дисковом пространстве."""

    def __init__(self, path="/"):
        """Инициализирует путь к диску."""
        self.path = path

    def get_usage(self):
        """Возвращает общий, использованный и свободный объем диска в байтах."""
        try:
            result = subprocess.run(["df", self.path], capture_output=True, text=True, check=True)
            data = result.stdout.split("\n")[1].split()
            total, used, free = int(data[1]) * 1024, int(data[2]) * 1024, int(data[3]) * 1024
        except Exception as e:
            raise RuntimeError(f"Ошибка получения данных: {e}")

        return total, used, free