# from collections.abc import Iterable
# class Connect(Iterable):
#     def sum(self):
#         i=0
#         for x in self:
#             i+=x
#         return i
        



class SingleValue():
    def __init__(self, value):
        self.value = value
        
    def getvalue(self):
        return self.value


class ManyValues(list):
    i=0
    def __init__(self):
        super().__init__()

    
    def _sum(self):
        if self:
            for child in self:
                if "SingleValue" in str(type(child)):
                    ManyValues.i+=child.getvalue()
                elif isinstance(child, int):
                    ManyValues.i+=child
                else:
                    child._sum()
    
    @property
    def sum(self):
        self._sum()
        res = ManyValues.i
        i=0
        return res
                    
                    


 
sv   = SingleValue(11)
ov = ManyValues()
ov.append(22)
ov.append(33)

av = ManyValues()
av.append(ov)
av.append(sv)

print(av.sum)
