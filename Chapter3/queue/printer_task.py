from queue_structure import Queue
import random

class Printer():
    def __init__(self, ppm):
        self.ppm = ppm #每分钟打印的页数 eg.10页/5页(high quality)
        self.current_task = None
        self.time_remaining = 0 #打印一次需要的时间

    def tick(self):
        if self.current_task != None: # printer是否在工作状态
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None


    def idle(self):
        if self.current_task != None:
            return False
        else:
            return True

    def start_next(self, new_task): #如果print idle 就会将队列中的下一个放入printer 任务中
        self.current_task = new_task
        # 打印该次文档需要的时间
        self.time_remaining = new_task.get_page()*(self.ppm/60) #每秒钟打印的页数

class Task():
    def __init__(self, time):
        self.page = 0
        self.timestamp = time #时间戳

    def get_stamp(self):
        return self.timestamp #显示时间戳（该任务开始时的时间）

    def get_page(self):
        self.page = random.randint(1,20)
        return self.page

    def wait_time(self, final_time):  #进入printer的时间 - 生产时间
        return final_time - self.timestamp

def new_print_task():  #从1s-180s中随机一秒的时间里产生一个任务（采取泊松分布到达）
    num = random.randrange(1,181)  # 平均在180s中产生一个任务
    if num == 180:
        return True
    else:
        return False

def model(simulation_time, ppm): #仿真时间(s)、打印速率
    lab_printer = Printer(ppm)
    print_queue = Queue()
    waiting_time = []
    #sum_task = 0

    for current_second in range(simulation_time):
        if new_print_task(): #如果出现了一个任务
            task = Task (current_second) #任务生产的时间
            print ('page time:', task.get_stamp())
            print('page page:', task.get_page())
            #sum_task = sum_task + 1
            #print('sum:', sum_task)
            print_queue.enqueue(task)  # queue的每个单元都有很多的属性

        if (lab_printer.idle()) and (not print_queue.is_empty()):
            front_task = print_queue.dequeue()
            print('printer time:', front_task.get_stamp())
            print('printer page:', front_task.get_page())
            waiting_time.append(front_task.wait_time(current_second)) # 将等待时间记录在list中
            lab_printer.start_next(front_task)  # printer 处理当前任务的时间

    lab_printer.tick()

    average_waiting_time =sum(waiting_time)/len(waiting_time)
    print("Average Wait %6.2f secs %3d tasks remaining."%(average_waiting_time,print_queue.size()))

for i in range(1):
    model(3600, 5)