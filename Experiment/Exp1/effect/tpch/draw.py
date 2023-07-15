"""
draw the figure: the mean and standard deviation of all queries
"""
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import subprocess
import os

marker = ['o', 's', '^', '*']
num_k = 5
def get_all_dirs():
    def get_dirs(target):
        pre_dir = os.getcwd()
        os.chdir(target)
        sub_res = [target + '/' + i for i in os.listdir() if os.path.isdir(i)]
        os.chdir(pre_dir)
        return sub_res

    all_target = ['.']
    res = []
    for i in all_target:
        res += get_dirs(i)

    return res

def read_data(file_name):
    with open(file_name, encoding='utf-8') as fin:
        content = [line.strip() for line in fin]
        content = [line for line in content if len(line) == 0 or line[0] == '*']
    
    while len(content) > 0 and content[0] == '':
        content = content[1:]
    
    index = [i for i,line in enumerate(content) if line == '']
    index.append(len(content)+10)

    pre = 0
    res = []
    for now in index:
        temp = tuple(content[pre:now])
        res.append(temp)
        pre = now + 1

    return res

def clear_data(data):
    def get_num(single_data):
        line = single_data[0]
        line = line.split(':')[-1]
        line = line.strip()
        return int(line)

    def get_time(single_data):
        sub_res = 0.0
        line = single_data[1].split(':')[-1]
        sub_res += float(line.strip())
        return sub_res

    res = [(get_num(i), get_time(i)) for i in data]
    return res

def process_data_mean(data1, data2, data3, data4):
    processed_data1 = []
    processed_data2 = []
    processed_data3 = []
    processed_data4 = []

    for i in range(num_k):
        sum = 0
        for key,value in data1.items():
            sum += value[i][1]
            k = value[i][0]
        # print(sum)
        processed_data1.append((k, sum/len(data1)))
    
    for i in range(num_k):
        sum = 0
        for key,value in data2.items():
            sum += value[i][1]
            k = value[i][0]
        # print(sum)
        processed_data2.append((k, sum/len(data2)))

    for i in range(num_k):
        sum = 0
        for key,value in data3.items():
            sum += value[i][1]
            k = value[i][0]
        # print(sum)
        processed_data3.append((k, sum/len(data3)))

    for i in range(num_k):
        sum = 0
        for key,value in data4.items():
            sum += value[i][1]
            k = value[i][0]
        # print(sum)
        processed_data4.append((k, sum/len(data4)))

    return processed_data1, processed_data2, processed_data3, processed_data4

def draw(data1, data2, data3, data4):
    num = [i[0] for i in data1]
    time1 = [i[1] for i in data1]
    time2 = [i[1] for i in data2]
    time3 = [i[1] for i in data3]
    time4 = [i[1] for i in data4]
    plt.plot(num, time1, marker=marker[0], color='#EB4169', label='B-TIPS-H/B', lw=2, markersize=10)
    plt.plot(num, time2, marker=marker[1], color='#00838d', label='Cost', lw=2, markersize=10)
    plt.plot(num, time3, marker=marker[2], color='#f28442', label='Random', lw=2, markersize=10)
    plt.plot(num, time4, marker=marker[3], color='#87CEFA', label='Embedding', lw=2, markersize=10)

    ax = plt.gca()
    ax.xaxis.set_major_locator(MultipleLocator(10))
    ax.yaxis.set_major_locator(MultipleLocator(0.1))

    plt.legend(fontsize=12, bbox_to_anchor=(0.95,0.9))
    plt.xticks(fontsize=22)
    plt.yticks(fontsize=22)
    plt.xlabel('number of alternative plans', fontsize=22, fontweight='bold')
    plt.ylabel('plan informativeness', fontsize=22, fontweight='bold')
    plt.tight_layout()

    plt.savefig('effect.pdf', dpi=300)

def main():
    dirs = get_all_dirs()
    data_tips_list = {}
    data_cost_list = {}
    data_random_list = {}
    data_embedding_list = {}
    # print(clear_data(read_data(dirs[0]+'/tips.txt')))
    for i in dirs:
        data_tips_list[i] = (clear_data(read_data(i+'/tips.txt')))
        data_cost_list[i] = (clear_data(read_data(i+'/cost.txt')))
        data_random_list[i] = (clear_data(read_data(i+'/random.txt')))
        data_embedding_list[i] = (clear_data(read_data(i+'/embedding.txt')))

    # print("tips", data_tips_list)
    # print("cost", data_cost_list)
    # print("random", data_random_list)
    # print("embedding", data_embedding_list)
    
    # print(process_data_mean(data_tips_list, data_cost_list, data_random_list, data_embedding_list))
    processed_mean_data1, processed_mean_data2, processed_mean_data3, processed_mean_data4 = process_data_mean(data_tips_list, data_cost_list, data_random_list, data_embedding_list)
    # print(processed_mean_data1, processed_mean_data2, processed_mean_data3, processed_mean_data4)

    draw(processed_mean_data1, processed_mean_data2, processed_mean_data3, processed_mean_data4)

if __name__ == '__main__':
    main()
    