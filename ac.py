from abc import ABC,abstractmethod
class subject(ABC):
    @abstractmethod
    def name(self):
        pass
class bca(subject):
    def name(self):
        print("java and python")

b1=bca()
b1.name()
