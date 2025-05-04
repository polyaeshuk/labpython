from Bio import Entrez
from Bio import SeqIO

# Укажите свой email, чтобы NCBI знал, кто вы (важно!)
Entrez.email = "polyaeshuk@gmail.com"

def download_genbank_records(species, num_records=5):
  """
  Скачивает записи GenBank для заданного вида.

  Args:
    species: Название вида (str).
    num_records: Количество записей для скачивания (int).

  Returns:
    Список объектов SeqRecord (Biopython).
  """
  try:
    handle = Entrez.esearch(db="nucleotide", term=f"{species} complete cds", retmax=num_records)
    record = Entrez.read(handle)
    handle.close()

    ids = record["IdList"]
    if not ids:
      print(f"Предупреждение: Не найдено записей для {species} с запросом 'complete cds'.")
      return []

    handle = Entrez.efetch(db="nucleotide", id=ids, rettype="gb", retmode="text")
    records = list(SeqIO.parse(handle, "genbank"))
    handle.close()

    print(f"Успешно скачано {len(records)} записей для {species}.")
    return records

  except Exception as e:
    print(f"Ошибка при скачивании записей для {species}: {e}")
    return []


def main():
  """
  Скачивает записи для двух видов, объединяет их и сохраняет в файл.
  """
  species1 = "Brassica oleracea"
  species2 = "Solanum lycopersicum"

  # Скачиваем записи для каждого вида
  records_species1 = download_genbank_records(species1)
  records_species2 = download_genbank_records(species2)

  # Объединяем записи
  all_records = records_species1 + records_species2

  # Проверяем, есть ли хотя бы 10 CDS
  cds_count = 0
  for record in all_records:
      for feature in record.features:
          if feature.type == "CDS":
              cds_count += 1

  if cds_count < 10:
      print(f"Предупреждение:  Общее количество CDS меньше 10 ({cds_count}).  Попробуйте увеличить число скачиваемых записей для каждого вида или выбрать другие записи.")
      
  # Сохраняем в файл
  output_filename = "combined_genbank.gb"
  try:
      SeqIO.write(all_records, output_filename, "genbank")
      print(f"Успешно сохранено {len(all_records)} записей в файл {output_filename}.")
  except Exception as e:
      print(f"Ошибка при сохранении в файл: {e}")

if __name__ == "__main__":
  main()