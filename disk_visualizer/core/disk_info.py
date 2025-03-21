import ctypes
import os
import subprocess


class DiskInfo:
    """Получает информацию о дисковом пространстве."""

    def __init__(self, path="/"):
        """Инициализирует путь к диску."""
        self.path = path

    def get_usage_windows(self):
        """Возвращает общий, использованный и свободный объем диска в байтах для Windows."""
        if not os.path.exists(self.path):
            raise FileNotFoundError(f"Ошибка: путь {self.path} не существует.")

        free_bytes = ctypes.c_ulonglong(0)
        total_bytes = ctypes.c_ulonglong(0)
        available_bytes = ctypes.c_ulonglong(0)

        ctypes.windll.kernel32.GetDiskFreeSpaceExW(
            ctypes.c_wchar_p(self.path),
            ctypes.byref(free_bytes),
            ctypes.byref(total_bytes),
            ctypes.byref(available_bytes)
        )

        total = total_bytes.value
        used = total_bytes.value - free_bytes.value
        free = free_bytes.value

        return total, used, free

    def get_usage(self):
        """Возвращает общий, использованный и свободный объем диска в байтах."""
        if not os.path.exists(self.path):
            raise FileNotFoundError(f"Ошибка: путь {self.path} не существует.")

        if os.name == "nt":  # Windows
            return self.get_usage_windows()
        else:  # Linux/macOS
            try:
                result = subprocess.run(["df", self.path], capture_output=True, text=True, check=True)
                data = result.stdout.split("\n")[1].split()
                total, used, free = int(data[1]) * 1024, int(data[2]) * 1024, int(data[3]) * 1024
            except Exception as e:
                raise RuntimeError(f"Ошибка получения данных: {e}")

        return total, used, free
