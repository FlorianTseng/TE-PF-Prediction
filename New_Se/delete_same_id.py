import pandas as pd

def remove_duplicates(input_file, output_file):
    # 读取CSV文件
    df = pd.read_csv(input_file)

    # 检查是否存在相同的多个条目，并仅保留一个条目
    df_unique = df.drop_duplicates(subset='mpid')

    # 将结果另存为一个新的CSV文件
    df_unique.to_csv(output_file, index=False)
    print(f"File saved as {output_file}")

if __name__ == "__main__":
    input_file = 'New_Te&Se.csv'
    output_file = 'New_Te&Se_unique.csv'
    remove_duplicates(input_file, output_file)
