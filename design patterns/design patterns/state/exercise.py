class CombinationLock:
    def __init__(self, combination):
        self.status = 'LOCKED'
        self.com = combination
        self.var = 0
        # todo
    def reset(self):
        self.status = 'LOCKED'
        # todo - reset lock to LOCKED state

    def enter_digit(self, digit):
        # todo
        n = len(self.com)
        if self.status == 'LOCKED':
            if self.var == n-1:
                self.status = 'OPEN'
        if digit == self.com[self.var]:
            self.var+=1
            if self.status == 'LOCKED':
                self.status = str(digit)
                print #(str(digit)+" yo")
            else:
                print# (str(digit)+" mo "+str(n))
                self.status+=str(digit)
                if self.var == n:
                    #print (str(digit)+" no")
                    self.status = 'OPEN'
                
        else:
            self.status = 'ERROR'
                

            # if entry == code:
            #     state = State.UNLOCKED


c1 = CombinationLock([1,2,3,4,5])
c1.enter_digit(1)
c1.enter_digit(2)
print(c1.status)
c1.enter_digit(3)
print(c1.status)
c1.enter_digit(4)
c1.enter_digit(3)
print(c1.status)
