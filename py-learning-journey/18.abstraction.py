#Abstraction used abstarct class that provides must implementable blueprint for the other class using that method,other class must overrdoe all abstarct method from abstract class.abstarct can able to contain both abstrct and non-abstract methods.

from abc import ABC, abstractmethod
class main(ABC):

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass

    def optional(self):
        pass

class app(main):
        def login(self):
            print("Login Feature")

        def logout(self):
            print("Logout Feature")

obj = app()
obj.login()
obj.logout()