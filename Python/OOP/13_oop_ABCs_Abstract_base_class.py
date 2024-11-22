
from abc import ABCMeta, abstractmethod



class Programming(metaclass= ABCMeta):
    @abstractmethod
    def has_oop(self):

        pass

    @abstractmethod
    def has_name(self):

        pass


class Python(Programming):
    
    def has_oop(self):

        return "Yes"



class Pascal(Programming):
    
    def has_oop(self):

        return "No"
    def has_name(self):
        return "Pascal"

one = Pascal()

print(one.has_oop())