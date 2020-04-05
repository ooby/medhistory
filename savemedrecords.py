# -*- coding: utf-8 -*-
"""Читает файл реестра медицинской истории и дописывает в другой файл"""

import sys

def filebuffer(fileobject):
    """Генератор буфера строк из файла"""
    try:
        prev = None
        while True:
            while prev:
                yield prev
                prev = yield prev
            prev = yield next(fileobject)
    except Exception:
        return

def process_records(infile, outfile):
    """Обработка MEDRECORD"""
    count = 0
    islist = 0
    with open(infile, 'r', encoding='utf-8', errors='ignore') as file1:
        infb = filebuffer(file1)
        for line in infb:
            if 'MEDRECORD_LIST' in line:
                if islist > 0:
                    position = line.find('MEDRECORD_LIST')
                    line = line[:(position + 15)]
                    with open(outfile, 'a', encoding='utf-8') as file2:
                        count += 1
                        file2.write(line)
                        print(count, 'строк записано в', outfile)
                        break
                else:
                    islist += 1
                    position = line.find('MEDRECORD_LIST')
                    line = line[(position - 1):]
                    with open(outfile, 'a', encoding='utf-8') as file2:
                        count += 1
                        file2.write(line)
                        continue
            else:
                if islist > 0:
                    with open(outfile, 'a', encoding='utf-8') as file2:
                        count += 1
                        file2.write(line)
                        continue
                else:
                    continue

# def process_data(infile):
#     """Обработка Data"""
#     count = 0
#     isrecord = 0
#     with open(infile, 'r', encoding='utf-8', errors='ignore') as file1:
#         infb = filebuffer(file1)
#         for line in infb:
#             if 'MEDRECORD' in line:

#             else:
#                 if isrecord > 0:
#                     with open('Data_'+infile, 'a', encoding='utf-8') as file2:
#                         count += 1
#                         file2.write(line)
#                         continue
#                 else:
#                     continue

def main():
    """Main"""
    if len(sys.argv) > 2:
        process_records(sys.argv[1], sys.argv[2])
        # process_data(sys.argv[2])
    else:
        print('Недостаточно вводных данных')

if __name__ == "__main__":
    main()