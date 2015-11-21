#!/usr/local/bin/python
#coding: utf-8

import csv
import sys


def import_csv(filename):
    data = [v for v in csv.reader(open(filename, 'rb')) if len(v) != 0]
    return data

def write_csv(write_arr, filename):
    f = open(filename, 'ab')
    csvWriter = csv.writer(f)
    for line in write_arr:
        csvWriter.writerow(line)
    f.close()

def import_all_txt(filname):
    f = open(filname)
    all_txt = f.read()
    f.close
    return all_txt

def write_all_txt(write_txt, filname):
    f = open(filname, 'w')
    f.write(write_txt)
    f.close()

def import_txt(filename):
    f = open(filename)
    lines = f.readlines() # 1行ごとに全部読み込んでる
    f.close()
    return lines

def write_txt(write_arr, filename):
    f = open(filename, 'w')
    for line in write_arr:
        f.write(line)
    f.close()

def displace(original, original_table):
    newlines = []
    for line in original:
        for i in original_table:
            line = line.replace(i[0], i[3])
        newlines.append(line)
    return newlines

if __name__ == "__main__":
    argv = sys.argv
#    print argv
    
    input_file = argv[1]
    left_num = argv[2]
    left_num = int(left_num)
    left_arr = []
    top_num = argv[3]
    top_num = int(top_num)
    top_arr = []
    data_num = int(argv[4])

    data = import_csv(input_file)

    for row in data:
        left_arr.append(row[left_num])
        top_arr.append(row[top_num])
    
    del top_arr[0]
    top_arr_u = sorted(list(set(top_arr)))
    del left_arr[0]
    left_arr_u = sorted(list(set(left_arr)))


    sys.stdout.write(",")
    counter = 0
    for i in top_arr_u:
        sys.stdout.write(i)
        counter += 1
        if counter != len(top_arr_u):
            sys.stdout.write(',')
    sys.stdout.write("\n")

    for i in left_arr_u:
        sys.stdout.write(i)
        sys.stdout.write(',')
        counter = 0
        for j in top_arr_u:
            counter += 1
            coun = 0
            for row in data:
                coun += 1
                if row[top_num] == j and row[left_num] == i:
                    sys.stdout.write(row[data_num])
                    if counter != len(top_arr_u):
                        sys.stdout.write(',')
                        break
                else:
                    if len(data) == coun:
                        sys.stdout.write(',')

        sys.stdout.write("\n")
                    





    


    

    













