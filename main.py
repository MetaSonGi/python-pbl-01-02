# main.py

import json

def read_log_file(filename):
    """
    Reads the log file, splits lines by comma,
    and converts each line into a list.

    :param filename: str - Path to the log file
    :return: list of lists
    """
    log_entries = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            # 첫 줄은 헤더
            header = file.readline().strip().split(',')
            for line in file:
                # 각 라인을 콤마로 분리
                parts = line.strip().split(',')
                if len(parts) == len(header):
                    log_entries.append(parts)
    except FileNotFoundError:
        print('Error: File not found.')
    except IOError:
        print('Error: Could not read the file.')

    return log_entries


def sort_logs_by_time(log_entries):
    """
    Sorts the log entries in reverse chronological order.

    :param log_entries: list of lists
    :return: sorted list of lists
    """
    # timestamp는 각 리스트의 첫 번째 원소
    return sorted(
        log_entries,
        key=lambda x: x[0],
        reverse=True
    )


def convert_to_dict(log_entries, header):
    """
    Converts list of lists into list of dictionaries.

    :param log_entries: list of lists
    :param header: list of str
    :return: list of dicts
    """
    dict_list = []
    for entry in log_entries:
        row_dict = {}
        for index, field in enumerate(header):
            row_dict[field] = entry[index]
        dict_list.append(row_dict)
    return dict_list


def save_json(data, filename):
    """
    Saves data as JSON to a file.

    :param data: list of dicts
    :param filename: str - Output file name
    """
    try:
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)
    except IOError:
        print('Error: Could not write to the file.')


def main():
    log_file = 'mission_computer_main.log'
    json_file = 'mission_computer_main.json'

    # 로그 읽기 → 리스트 생성
    log_entries = read_log_file(log_file)

    if not log_entries:
        print('No data found in log file.')
        return

    # 첫 행은 헤더
    header = ['timestamp', 'event', 'message']

    # 리스트 출력
    print('=== Original List ===')
    for entry in log_entries:
        print(entry)

    # 시간 역순 정렬
    sorted_entries = sort_logs_by_time(log_entries)

    print('\n=== Sorted List (Reverse Chronological) ===')
    for entry in sorted_entries:
        print(entry)

    # 리스트 → 딕셔너리 변환
    dict_entries = convert_to_dict(sorted_entries, header)

    # JSON 파일로 저장
    save_json(dict_entries, json_file)

    print(f'\nJSON file saved: {json_file}')


if __name__ == '__main__':
    main()

