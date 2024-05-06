import datetime as dt
import csv
from pathlib import Path

# По тестам нужна переменная BASE_DIR,
# не придумал ничего умнее кроме вызова "родителя" у "родителя"
# Дальше в коде где используется BASE_DIR
# закомментирован вариант без BASE_DIR, не знаю чем он плох
PROJECT_DIR = Path(__file__).parent
BASE_DIR = PROJECT_DIR.parent

DT_FORMAT = '%Y-%m-%d_%H:%M:%S'


class PepParsePipeline:

    STATUSES_COUNT = {}

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        status = item['status']
        self.STATUSES_COUNT[status] = self.STATUSES_COUNT.get(status, 0) + 1
        return item

    def create_file(self):
        results_dir = '..' / BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)
        now = dt.datetime.now()
        now_formatted = now.strftime(DT_FORMAT)
        file_path = results_dir / f'status_summary_{now_formatted}.csv'

        # Вариант без BASE_DIR
        # now = dt.datetime.now()
        # now_formatted = now.strftime(DT_FORMAT)
        # file_path = f'results/status_summary_{now_formatted}.csv'
        return file_path

    def all_statuses_count(self):
        total = 0
        for status in self.STATUSES_COUNT.keys():
            total += self.STATUSES_COUNT[status]
        return total

    def writing_in_file(self, file_path, total):
        results = [('Статус', 'Количество')]
        results.extend(
            [(st, qt) for st, qt in self.STATUSES_COUNT.items()]
        )
        results.append(('Total', total))

        with open(file_path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerows(results)

    def close_spider(self, spider):
        file_path = self.create_file()
        total = self.all_statuses_count()
        self.writing_in_file(file_path, total)
