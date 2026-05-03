import argparse
import shutil
from pathlib import Path


def copy_and_sort_files(src_dir: Path, dst_dir: Path):
    try:
        for item in src_dir.iterdir():
            if item.is_dir():
                copy_and_sort_files(item, dst_dir)
            elif item.is_file():
                try:
                    ext = item.suffix[1:].lower() if item.suffix else "no_extension"

                    target_dir = dst_dir / ext
                    target_dir.mkdir(parents=True, exist_ok=True)

                    target_file = target_dir / item.name

                    shutil.copy2(item, target_file)

                except Exception as e:
                    print(f"Помилка при копіюванні файлу {item}: {e}")

    except Exception as e:
        print(f"Помилка доступу до директорії {src_dir}: {e}")


def main():
    parser = argparse.ArgumentParser(description="Сортування файлів")
    parser.add_argument("source", nargs="?", help="Шлях до вихідної директорії")
    parser.add_argument("destination", nargs="?", default="dist", help="Шлях призначення")

    args = parser.parse_args()

    source = args.source
    if not source:
        source = input("Введіть шлях до вихідної папки: ").strip()
    
    destination = args.destination

    src_path = Path(source)
    dst_path = Path(destination)

    if not src_path.exists() or not src_path.is_dir():
        print(f"Помилка: Вихідна директорія '{src_path}' не існує або не є текою.")
        return

    try:
        dst_path.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        print(f"Не вдалося створити директорію призначення: {e}")
        return

    copy_and_sort_files(src_path, dst_path)
    print(f"Копіювання завершено! Результати у папці: {dst_path.absolute()}")


if __name__ == "__main__":
    main()