import datetime
import multiprocessing

def read_info(name):
    all_data = []
    with open (name,'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)

all_files = ['file 1.txt', 'file 2.txt', 'file 3.txt','file 4.txt']

start = datetime.datetime.now()
for filename in all_files:
    read_info(filename)
finish = datetime.datetime.now()
print(finish - start,'Линейный')

if __name__ =='__main__':
    start_1 = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info,all_files)
    finish_1 = datetime.datetime.now()
    print(finish_1 - start_1,'Многопроцессный')