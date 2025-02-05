import os
import csv
import math
import tempfile
import shutil

def calculate_new_value(original_value):
    new_value = math.log10(((10 ** original_value - 7) * 10 ** -7) * 10 ** -2)
    return new_value

def process_csv_file(file_path):
    temp_file_path = tempfile.mktemp()  # 创建临时文件

    with open(file_path, 'r', newline='') as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    fieldnames = reader.fieldnames

    updated_rows = []
    for row in rows:
        updated_row = row.copy()  # 复制原始行的数据
        if 'True Value' in row and 'Predicted Value' in row:
            original_value = float(row['True Value'])
            new_value = calculate_new_value(original_value)
            updated_row['True Value'] = str(new_value)

            original_value = float(row['Predicted Value'])
            new_value = calculate_new_value(original_value)
            updated_row['Predicted Value'] = str(new_value)

        updated_rows.append(updated_row)

    with open(temp_file_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(updated_rows)

    shutil.move(temp_file_path, file_path)  # 替换原始文件

def process_csv_files_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            file_path = os.path.join(directory, filename)
            process_csv_file(file_path)

current_directory = os.getcwd()
process_csv_files_in_directory(current_directory)