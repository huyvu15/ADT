# xây dựng hệ thống mô phỏng trật tự lễ tân ở quầy tiếp đón tại ngân hàng
import install_queue_linkedlist as Que
import random
import numpy as np
import random
# lớp khách hàng
class Customer:
    def __init__(self, id, corivalTime):
        self.id = id # mã khách hàng
        self.corivalTime = corivalTime # thời gian khách hàng chờ

# lớp thu ngân, nhân viên là người trực tiếp làm việc với khách hàng
class Counter:
    def __init__(self, id, nCustomer, cur_Cus, stop_Time):
        self.id = id # mã nhân viên
        self.nCustomer = nCustomer # tổng số khách hàng phục vụ
        self.cur_Cus = cur_Cus # số khách hàng hiện tại
        self.stop_Time = stop_Time # thời gian khách hàng xong việc với quầy hiện tại
        self.isfree = 1 # quầy có trống hay không?
    
    # đón khách hàng
    def start_Serve(self,id_Cus, startTime): # đưa khách hàng vào quầy vào bắt đầu phục vụ
        self.cur_Cus = id_Cus # gắn mã, số thứ tự cho khách hàng
        self.stopTime = startTime + 5 # mặc định cho thời gian phục vụ 1 khách hàng là 5 phút(quy ước)
        # cần 1 hàm để sinh ra cái thời gian đấy
            
    # dừng phục vụ
    def stop_Serve(self,time): # ví dụ 3h phục vụ thì 3h05 xong 
        if self.cur_Cus != None and self.stop_Time == time:
            self.nCustomer += 1 # ghi công bằng cách tăng số kh lên 1
            self.cur_Cus = None # gắn KH hiện tại bằng None người khách đó đi ra thì quầy đang trống
            self.stop_Time -= 1

# lớp cơ chế hoạt động
# chỉ sử lý bài toán tĩnh số quầy không đổi và lúc nào cx mở
class Simulation(): # máy kiểm tra xem quầy có đang làm việc không
    def __init__(self, nCouters, Counters, sTime, customers, p):
        self.nCouters = nCouters # số lượng quầy 
        self.Counters = Counters # danh sách các quầy
        self.sTime = sTime # thời gian mô phỏng
        # sau này khi gắn sTime = 100 nghĩa là xét trong 100 đơn vị thời gian
        # đối tượng được phục vụ
        # khách nào đến trước phục vụ trước nên dùng queue
        self.customers = customers # 1 hàng đợi khách hàng (cài đặt bằng queue)
        self.p = p # Xác suất thời gian trung bình có 1 khách hàng đến 
        
        
    # Các method
    # khởi tạo
    def simulation(self, n, s): # n - nCounters, s - sTime
        self.nCouters = n
        self.Counters = [] 
        
        # tạo ra n quầy
        for i in range(n-1):
            self.Counters[i] = Counter(i)
        self.sTime = s
        self.customer = Que.Queue()
     
    def isFree(self):
         pass   
     
    def isEmpty(self):
        pass
    
        
    def handle_Arrival(self, i): # xử lý khách hàng đến
        t = random.randint(1, 10) # return {0, 1, ... p-1} quy định 0 là có khách  còn lại là ko
        if t == 0 :
            new_cus = Customer(Customer.size, i) # i là thời điểm khách hàng xuất hiện
            Customer.enqueue(new_cus)
        pass
    
    def handle_Serve(self, i): # xử lý phúc vụ
        for each_couter in self.Counters: # mỗi quầy hay mỗi thu ngân
            if self.Counters.isFree() and not Customer.isEmpty(): # isFree và isEmpty chưa setting
                # quầy đang trống và có khách chờ
                Counter.start_Serve(Customer.id.dequeue(), i) # i là sTime
                pass 
        pass
    
    
    
    def handle_Stop_Serve(self, i): # Kiểm tra kết thúc phục vụ ở quầy
        for each_counter in self.Counters:
            if Counter.curCus != None and self.sTime == i:
                Counter.stop_Serve()
        pass    





    