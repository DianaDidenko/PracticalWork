# bugfix.py
def buggy_function():
    # Fixed code
    try:
        result = 1 / 1  # Виправлення помилки
    except ZeroDivisionError:
        result = None
    return result
