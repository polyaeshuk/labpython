from Bio import SeqIO
from Bio.Seq import Seq

def translate_cds(filename):
  """
  Читает записи GenBank из файла и выводит транслированные белковые последовательности.

  Args:
    filename: Имя входного файла GenBank (str).
  """
  try:
    records = list(SeqIO.parse(filename, "genbank"))

    for record in records:
      for feature in record.features:
        if feature.type == "CDS":
          try:
            # Извлекаем координаты кодирующей области
            start = feature.location.start
            end = feature.location.end
            strand = feature.location.strand

            # Извлекаем последовательность кодирующей области
            cds_seq = feature.extract(record.seq)

            # Транслируем последовательность
            translation = cds_seq.translate(to_stop=True)

            print(f"{record.id}: {record.description}")
            print(f"Coding sequence location = [{start}:{end}]({'Positive' if strand == 1 else 'Negative'})") #Явно указываем полярность цепи
            print(f"Translation =\n{translation}\n")

          except Exception as e:
            print(f"Ошибка при трансляции CDS в {record.id}: {e}")

  except FileNotFoundError:
    print(f"Ошибка: Файл {filename} не найден.")
  except Exception as e:
    print(f"Ошибка при обработке файла {filename}: {e}")


if __name__ == "__main__":
  filename = "combined_genbank.gb"  # Замените на имя вашего файла

  print("\nТрансляция CDS:")
  translate_cds(filename)