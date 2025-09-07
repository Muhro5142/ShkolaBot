import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

def create_table_from_data(data):
    # Разбиение данных на строки и столбцы
    rows = []
    for row in data:
        if not isinstance(row, list):  # Убедимся, что row - это список
            row = []
        processed_row = [item if item != '' else '' for item in row]  # Заменяем пустые элементы на ''
        rows.append(processed_row)
    
    # Проверка: Все строки должны быть одной длины
    max_cols = max(len(row) for row in rows) if rows else 0
    rows = [row + [''] * (max_cols - len(row)) for row in rows]  # Добавляем пустые значения для выравнивания

    # Создание фигуры и оси
    fig, ax = plt.subplots(figsize=(12, len(rows) * 0.5))  # Размер по количеству строк
    ax.axis('tight')  # Убираем оси
    ax.axis('off')  # Убираем оси, так как нам нужна только таблица

    # Установка шрифта для поддержки иврита
    plt.rcParams['font.family'] = 'Arial'  # Или любой другой шрифт, поддерживающий иврит

    # Создание таблицы
    table = ax.table(
        cellText=rows,
        loc='center',
        cellLoc='center',  # Центрирование текста
        colColours=['#f0f0f0'] * max_cols  # Цвет для всех столбцов
    )
    
    # Настроим внешний вид таблицы
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.2)

    # Корректировка ширины столбцов для лучшего отображения текста
    for (i, j), cell in table.get_celld().items():
        cell.set_text_props(ha='right')  # Выравнивание текста по правому краю
        cell.set_fontsize(12)
        if j == -1:  # Установка ширины для заголовков столбцов
            cell.set_width(0.1)
        else:
            cell.set_width(1.0 / max_cols)  # Динамическое выравнивание ширины ячеек

    # Показываем таблицу
    plt.show()
