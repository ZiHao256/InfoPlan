import os


def str_from_file(file_name):
    file = open(input_path + file_name + '.json')

    file_content = ""

    iter_f = iter(file)
    for line in iter_f:
        file_content += line
    return file_content


if __name__ == '__main__':

    input_path = os.path.abspath(os.path.dirname(os.getcwd())) + '/process_AQP_list/output/'

    print("input the first file")

    first_file_name = input()

    first_file__content = str_from_file(first_file_name)

    while 1:

        print("input the name(without .json) of file to be merged(enter 0 to stop)")
        name = input()

        if name == '0':
            break

        t = str_from_file(name)

        first_file__content = first_file__content[:-1] + ','

        t = t[1:]

        first_file__content += t

        # print(first_file__content)

    w_file_merge = open(input_path+'merge.json', 'w')
    w_file_merge.write(first_file__content)
