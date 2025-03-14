import matplotlib.pyplot as plt

class DiskVisualizer:
    """Строит график использования дискового пространства."""

    @staticmethod
    def plot_disk_usage(total, used, free):
        """Создает круговую диаграмму использования диска с измененным заголовком окна."""
        labels = ["Использовано", "Свободно"]
        sizes = [used, free]
        colors = ["red", "green"]

        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, autopct="%1.1f%%", colors=colors, startangle=90)

        fig = plt.gcf()
        fig.canvas.manager.set_window_title("Визуализация диска")

        plt.show()
