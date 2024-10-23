import time
from time import sleep
from threading import Thread

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i}\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

start_time = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end_time = time.time()
res_time = end_time - start_time
print("Время выполнения функций:", res_time)

start_time_2 = time.time()
trd_1 = Thread(target=write_words, args=(10, 'example5.txt'))
trd_2 = Thread(target=write_words, args=(30, 'example6.txt'))
trd_3 = Thread(target=write_words, args=(200, 'example7.txt'))
trd_4 = Thread(target=write_words, args=(100, 'example8.txt'))

trd_1.start()
trd_2.start()
trd_3.start()
trd_4.start()

trd_1.join()
trd_2.join()
trd_3.join()
trd_4.join()

end_time2 = time.time()
res_time2 = end_time2 - start_time_2
print(f'Время выполнения функций:', res_time2)