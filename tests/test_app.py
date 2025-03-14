import argparse
import unittest
from unittest.mock import patch
from disk_visualizer.app import DiskUsageApp

class TestDiskUsageApp(unittest.TestCase):
    """Тесты для основного класса приложения."""

    @patch("argparse.ArgumentParser.parse_args", return_value=argparse.Namespace(path="/"))
    @patch("disk_visualizer.core.disk_info.DiskInfo.get_usage", return_value=(100, 50, 50))
    def test_run(self, mock_get_usage, mock_args):
        """Проверяет, что приложение запускается без ошибок."""
        app = DiskUsageApp()
        try:
            app.run()
        except Exception as e:
            self.fail(f"Метод run вызвал ошибку: {e}")

if __name__ == "__main__":
    unittest.main()
