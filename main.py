# # decorator: funksiyaning logikasiga halaqit bermagan holda undan oldin va keyin ishlaydigan funksiya

# def f1(func):
#   def f2(*args, **kwargs):
#     print("funksiya hali ishlamadi")
#     func(*args, **kwargs)
#     print("funksiya ishlab bo'ldi")
  
#   return f2

# @f1
# def f3(a, b):
#   print(a + b)

# f3(3, 2)

# # f1 -> decorator funksiya
# # func -> uning parametri
# # f2 -> uning ichidagi funksiya
# # print("funksiya hali ishlamadi") -> funksiya ishlashidan oldin bajariladigan amal
# # func(*args, **kwargs) -> funksiyaning o'zi
# # print("funksiya ishlab bo'ldi") -> funksiya ishlashidan keyin bajariladigan amal

# # f3 -> func
# # f3 bajarilishidan oldin print("funksiya hali ishlamadi") ishlaydi va u ishlashidan keyin pprint("funksiya ishlab bo'ldi") yana ishlaydi


# # ====================================================================================
# # ====================================================================================


# # iterator va generator: ma'lumotlarni ketma-ket olish uchun mo'ljallangan mexanizmlar
# # iteratorlar 2 xil bo'ladi: iterable va sequence
# # iterable: elementlari ketma-ket olinadigan har qanday obyekt (set, dict)
# # sequence: tartiblangan va index orqali murojaat qilinadgian (list, tuple, str)

# # barcha sequencelar iterable, lekin barcha iterablelar sequence emas.

# # iterator: iterable ustidagi iteratsiyani boshqaradigan obyekt
# # iterable dan iterator yaratish uchun iter() funksiyasini ishlatamiz

# a = [1, 2, 3]
# a_iter = iter(a)

# # va undagi qiymatlarni olish uchun biz next() funksiyasini ishlatamiz

# print(next(a_iter)) # -> natija 1
# print(next(a_iter)) # -> natija 2
# print(next(a_iter)) # -> natija 3

# print(next(a_iter)) # -> natija StopIteration


# # generator: iteratorni yaratishning oson usuli
# # generatorlarni yaratishning 3 xil usuli bor: yield, OOP, anonymous

# # 1-usul (yield orqali)
# def number_generator(n):
#   for i in range(n):
#     yield i

# gen = number_generator(5)
# for num in gen:
#   print(num)

# # 2-usul (OOP orqali)
# class NumberGenerator:
#   def __init__(self, n):
#     self.n = n
#     self.current = 0

#   def __iter__(self):
#     return self

#   def __next__(self):
#     if self.current < self.n:
#       num = self.current
#       self.current += 1
#       return num
#     else:
#       raise StopIteration

# gen = NumberGenerator(5)
# for num in gen:
#   print(num)


# # 3-usul (anonymous)
# gen = (x * 2 for x in range(5))
# for num in gen:
#   print(num)



# # ====================================================================================
# # ====================================================================================


# import time, os
# from threading import Thread, current_thread
# from multiprocessing import Process, current_process


# COUNT = 200000000
# SLEEP = 10

# def io_bound(sec):

#     pid = os.getpid()
#     threadName = current_thread().name
#     processName = current_process().name

#     print(f"{pid} * {processName} * {threadName} \
#         ---> Start sleeping...")
#     time.sleep(sec)
#     print(f"{pid} * {processName} * {threadName} \
#         ---> Finished sleeping...")

# def cpu_bound(n):

#   pid = os.getpid()
#   threadName = current_thread().name
#   processName = current_process().name

#   print(f"{pid} * {processName} * {threadName} \
#     ---> Start counting...")

#   while n>0:
#     n -= 1

#   print(f"{pid} * {processName} * {threadName} \
#     ---> Finished counting...")

# if __name__=="__main__":
#   start = time.time()

#   # # 1-misol
#   # io_bound(SLEEP)
#   # io_bound(SLEEP)

#   # # output:

#   # # 16485 * MainProcess * MainThread         ---> Start sleeping...
#   # # 16485 * MainProcess * MainThread         ---> Finished sleeping...
#   # # 16485 * MainProcess * MainThread         ---> Start sleeping...
#   # # 16485 * MainProcess * MainThread         ---> Finished sleeping...
#   # # Time taken in seconds - 20.00841999053955

#   # # 2-misol
#   # t1 = Thread(target = io_bound, args =(SLEEP, ))
#   # t2 = Thread(target = io_bound, args =(SLEEP, ))
#   # t1.start()
#   # t2.start()
#   # t1.join()
#   # t2.join()

#   # # output:

#   # # 17072 * MainProcess * Thread-1 (io_bound)         ---> Start sleeping...
#   # # 17072 * MainProcess * Thread-2 (io_bound)         ---> Start sleeping...
#   # # 17072 * MainProcess * Thread-1 (io_bound)         ---> Finished sleeping...
#   # # 17072 * MainProcess * Thread-2 (io_bound)         ---> Finished sleeping...
#   # # Time taken in seconds - 10.005249977111816

#   # # 3-misol
#   # cpu_bound(COUNT)
#   # cpu_bound(COUNT)

#   # # output:

#   # # 17387 * MainProcess * MainThread     ---> Start counting...
#   # # 17387 * MainProcess * MainThread     ---> Finished counting...
#   # # 17387 * MainProcess * MainThread     ---> Start counting...
#   # # 17387 * MainProcess * MainThread     ---> Finished counting...
#   # # Time taken in seconds - 8.758356094360352

#   end = time.time()
#   print('Time taken in seconds -', end - start)


# # ====================================================================================
# # ====================================================================================

# # context manager
# from contextlib import contextmanager

# @contextmanager
# def file_manager(file_name, mode):
#   f = None
#   try:
#     if "." not in file_name:
#       raise NameError
#     print(f"File {file_name} is opening...")
#     f = open(file_name, mode) # file is opening
#     yield f # file object is being returned
#   finally:
#     if f:
#       print(f"File {file_name} is closing...")
#       f.close()

# with file_manager("main.py", "r") as file:
#   f = file.read()
#   print(f)