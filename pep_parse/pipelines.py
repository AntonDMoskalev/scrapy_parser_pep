import datetime as dt

from pep_parse.constants import BASE_DIR, DATETIME_FORMAT


class PepParsePipeline:
    """
    The pipeline generates and stores an additional .csv table,
    with a count of the number of each status,
    and the total number of statuses.
    """
    total = 0
    status_list = {}

    def open_spider(self, spider):
        self.total = 0
        self.status_list = {}

    def process_item(self, item, spider):
        self.status_list[item['status']] = self.status_list.get(
            item['status'], 0) + 1
        self.total += 1
        return item

    def close_spider(self, spider):
        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)
        parser_mode = 'status_summary'
        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        file_name = f'{parser_mode}_{now_formatted}.csv'
        file_path = results_dir / file_name
        with open(file_path, mode='w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            for value in self.status_list:
                f.write(f'{value},{self.status_list[value]}\n')
            f.write(f'Total,{self.total}\n')
