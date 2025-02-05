import csv

input_file = r'C:\Users\11097\Desktop\论文\SISSO\Single_Feature\PFn\PFn\desc_dat\desc_D001_t001.dat'
output_file = 'result.csv'

# 读取输入文件内容
with open(input_file, 'r') as file:
    lines = file.readlines()

# 解析输入文件内容
data = []
for line in lines:
    line = line.strip()
    if line.startswith('Index'):
        continue
    index, y_true, y_pred, descriptor_1 = line.split()
    data.append([index, y_true, y_pred, descriptor_1])

# 写入输出文件
with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Index', 'y_true', 'y_pred', 'descriptor_1'])  # 写入标题行
    writer.writerows(data)  # 写入数据行

print(f"转换完成，结果已保存到 {output_file} 文件中。")