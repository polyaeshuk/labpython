from Bio import SeqIO
from Bio.SeqUtils import GC

def calculate_gc_content(record):
    """Вычисляет GC-состав последовательности."""
    return GC(record.seq)

def sort_by_gc_content(filename):
    """
    Читает записи GenBank из файла, сортирует их по GC-составу и выводит.

    Args:
      filename: Имя входного файла GenBank (str).
    """
    try:
        records = list(SeqIO.parse(filename, "genbank"))

        # Добавляем GC-состав к каждой записи как атрибут
        for record in records:
            record.gc_content = calculate_gc_content(record)

        sorted_records = sorted(records, key=lambda record: record.gc_content)

        for record in sorted_records:
            print(f"{record.id}: {record.description}, GC = {record.gc_content}")

    except FileNotFoundError:
        print(f"Ошибка: Файл {filename} не найден.")
    except Exception as e:
        print(f"Ошибка при обработке файла {filename}: {e}")


if __name__ == "__main__":
    filename = "combined_genbank.gb"  # Замените на имя вашего файла

    print("Сортировка по GC-составу:")
    sort_by_gc_content(filename)
