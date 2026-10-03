import shutil
from pathlib import Path

# Куда складывать — папка для сортировки
TARGET_DIR = Path.home() / "22222"  

# Категории и расширения
CATEGORIES = {
    "Изображения": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Документы": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx"],
    "Видео": [".mp4", ".avi", ".mkv", ".mov"],
    "Музыка": [".mp3", ".wav", ".flac"],
    "Архивы": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Программы": [".exe", ".msi", ".dmg"],
}


def get_category(extension):
    for category, extensions in CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "Другое"


def organize(directory):
    directory = Path(directory)
    if not directory.exists():
        print(f"Папка не найдена: {directory}")
        return

    moved = 0
    for file in directory.iterdir():
        if file.is_dir():
            continue
        category = get_category(file.suffix)
        target_folder = directory / category
        target_folder.mkdir(exist_ok=True)
        shutil.move(str(file), str(target_folder / file.name))
        moved += 1
        print(f"  {file.name} -> {category}/")

    print(f"\nГотово! Перемещено файлов: {moved}")


def main():
    print(f"Сортирую папку: {TARGET_DIR}")
    organize(TARGET_DIR)


if __name__ == "__main__":
    main()
