import unittest
import matplotlib.pyplot as plt
from disk_visualizer.core.disk_visualizer import DiskVisualizer

class TestDiskVisualizer(unittest.TestCase):
    """Тесты для визуализатора дискового пространства."""

    def test_plot_disk_usage(self):
        """Проверяет, что метод plot_disk_usage не вызывает ошибок."""
        try:
            DiskVisualizer.plot_disk_usage(100, 50, 50)
        except Exception as e:
            self.fail(f"Метод plot_disk_usage вызвал ошибку: {e}")

    def test_plot_output(self):
        """Проверяет, что график создается (не закрываем plt сразу)."""
        DiskVisualizer.plot_disk_usage(100, 50, 50)
        fig = plt.gcf()
        self.assertIsNotNone(fig)

if __name__ == "__main__":
    unittest.main()
