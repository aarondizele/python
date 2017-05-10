import time
import math
import threading
import multiprocessing as mp

share_data = []

# def calc_square():

#     global share_data
#     print("Calculate square numbers: ")
#     for i in range(1,5):
#         time.sleep(5)
#         print('square:',i*i)

# def calc_cube():
#     print("Calculate cube numbers: ")
#     for i in range(1,5):
#         time.sleep(5)
#         print('cube:',i*i*i)

# # arr = [2,3,8,9]


def calc_square(q):
    # v.value = 5.4
    # global share_data
    for n in range(2,11):
        q.put(n*n)
    #     share_data.append(n*n)
    # print('Inside process {}'.format(share_data))

def f(n):
    sum = 0
    for x in range(1000):
        sum += x*x
    return sum

if __name__=="__main__":
    # t = time.time()
    # # calc_square()
    # # calc_cube()
    # # t1 = threading.Thread(target=calc_square)
    # # t2 = threading.Thread(target=calc_cube)
    # p1 = mp.Process(target=calc_square)
    # p2 = mp.Process(target=calc_cube)

    # # t1.start()
    # # t2.start()
    # p1.start()
    # p2.start()

    # # t1.join()
    # # t2.join()
    # p1.join()
    # p2.join()

    # print("Done in: {} seconds".format(time.time()-t))
    # print("Program done execution!")
    # v = mp.Value('d',1)
    # q = mp.Queue()
    # p = mp.Process(target=calc_square, args=(q,))
    # p.start()
    # p.join()

    # # print('Outside process {}'.format(v.value))
    # while q.empty() is False:
    #     print(q.get())


    t1 = time.time()
    # array = [x for x in range(2,11)]
    p = mp.Pool()
    result = p.map(f, range(100000))
    # print(result)
    p.close()
    p.join()

    print("Pool took: {}".format(time.time()-t1))

    t2 = time.time()
    result = []
    for x in range(100000):
        result.append(f(x))
    print("Serial processing took:{}".format(time.time()-t2))