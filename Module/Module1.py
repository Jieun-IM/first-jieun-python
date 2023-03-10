def func1():
    print("Module1.py의 func1()이 호출됨.")
    
def func2():
    print("Module1.py의 func2()가 호출됨.")
    
def func3():
    print("Module1.py의 func3()이 호출됨.")
    
def publicFunc():
    print('this is public function')

def _privateFunc():
    print('this is private function')    

    
if __name__ =="__main__":
    print('\n')
    func1()
    
publicFunc()
_privateFunc()