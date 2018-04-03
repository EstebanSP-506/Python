import datetime

class Call(object):
    callID = 0
    def __init__(self, caller_name, caller_phone, call_reason ):
        Call.callID+=1
        self.call_id = Call.callID
        self.caller_name = caller_name
        self.caller_phone = caller_phone
        self.call_time = datetime.datetime.now()
        self.call_reason = call_reason
    def display (self):
        print "Call ID: {}".format(self.call_id)
        print "Call name: {}".format(self.caller_name)
        print "Call reason: {}".format(self.call_reason)
        print "Call number: {}".format(self.caller_phone)
        print "Call time: {}".format(self.call_time)
        print "=========================================="
        


call1 = Call("Justin Case","555-5555-5555","testing")
call2 = Call("Justin Case 2","666-5555-5555","testeado")
call3 = Call("Justin Case 3","619-5555-5555","lol")

class CallCenter(object):
    def __init__(self):
        self.calls_list = []
        self.queue_size = 0
    # Methods
    def add(self, *calls):
        for element in calls:
            self.calls_list.append(element)                          
        self.queue_size = len(self.calls_list)  
        return self          
    def remove(self):
        del self.calls_list[0]           
        self.queue_size = len(self.calls_list)  
        return self          
    def removePhone(self,phoneNumber):
        for a in self.calls_list:
            print a.caller_phone
            if a.caller_phone == phoneNumber:
                self.calls_list.remove(a)
        self.queue_size = len(self.calls_list)
        return self       
    # Still not sure if this sorting is going to work   
    def sortQueue(self):  
        sorted(self.calls_list,key=lambda Call : Call.call_time)
        return self    
    def info(self):
        print "The current length of the queue is {}".format(self.queue_size)
        for elements in self.calls_list:
            print "Call ID: {}. The caller name is: {} and the caller phone number is {}".format(elements.call_id, elements.caller_name, elements.caller_phone)
        print "===================================="

call4 = Call("Justin Case 3","506-8555-5758","lol")
call5 = Call("Justin Case 3","333-5555-5555","lol")
call6 = Call("Justin Case 3","123-5555-5555","lol")
call1.display()
call2.display()
call3.display()
call4.display()
call5.display()
call6.display()

call_center1 = CallCenter()

call_center1.add(call6,call3,call2,call4,call5,call1).removePhone("506-8555-5758").info()

call_center1.sortQueue().info()

