import os
import csv


def replace_spaces_with_underscore(csv_file, dat_file):
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        rows = list(csv_reader)

    # 替换标签中的空格为下划线
    for i in range(len(rows[0])):
        rows[0][i] = rows[0][i].replace(' ', '_')

    with open(dat_file, 'w') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerows(rows)


def remove_empty_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # 移除空行
    lines = [line.strip() for line in lines if line.strip()]

    with open(file_path, 'w') as file:
        file.write('\n'.join(lines))


def process_dat_files(directory):
    for file_name in os.listdir(directory):
        if file_name.endswith('.dat'):
            file_path = os.path.join(directory, file_name)
            remove_empty_lines(file_path)


def convert_csv_to_dat(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            csv_file = os.path.join(directory, filename)
            dat_file = os.path.splitext(csv_file)[0] + '.dat'
            replace_spaces_with_underscore(csv_file, dat_file)
            remove_empty_lines(dat_file)

            print(f"转换完成！已将CSV文件 {csv_file} 转换为 {dat_file}。")


# 指定目录
directory_path = r'C:\Users\11097\Desktop\论文\SISSO\Single_Feature\PFn'

# 执行转换
convert_csv_to_dat(directory_path)