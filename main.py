import threading

def count(n):
    while n > 0:
        n -= 1

if __name__ == '__main__':
    count(100)
    count(100)
    t1 = threading.Thread(target=count, args=(100,))
    t1.start()
    t2 = threading.Thread(target=count, args=(100,))
    t2.start()
    t1.join()
    t2.join()
