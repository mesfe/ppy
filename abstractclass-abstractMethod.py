from abc import ABCMeta,abstractmethod

class Shape(object):



    __metaclass__ = ABCMeta


    @abstractmethod
    def area(self): print 'area'

    @abstractmethod
    def parimiter(self): print 'area'




class Rectangular(Shape):

    def __init__(self):
        super(Rectangular,self).__init__()


    def area(self):
        print 'area'


    def parimiter(self):
        print 'paramitier'


rec=Rectangular()

rec.area()