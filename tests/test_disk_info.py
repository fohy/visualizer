import unittest
import os
from disk_visualizer.core.disk_info import DiskInfo

class TestDiskInfo(unittest.TestCase):
    """Тесты для получения информации о диске."""

    def test_get_usage(self):
        """Проверяет, что метод get_usage возвращает три числа."""
        disk_info = DiskInfo("/")
        total, used, free = disk_info.get_usage()
        self.assertIsInstance(total, int)
        self.assertIsInstance(used, int)
        self.assertIsInstance(free, int)

    def test_invalid_path(self):
        """Проверяет, что метод get_usage вызывает ошибку для неверного пути."""
        with self.assertRaises(FileNotFoundError):
            DiskInfo("/invalid_path").get_usage()

if __name__ == "__main__":
    unittest.main()
