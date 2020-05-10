class MyExeception(Exception):
    pass


class MyClass:
    
    def cleanup(self, message=None):
        print("Cleaning Up")
        try:
            raise NotImplementedError("Method not implemented")
        except NotImplementedError as n:
            print(str(n))
        
    def run(self):
        try:
            if not True:
                print("Not Working")
                raise Exception("Run is too short")
            
            raise Exception("Run Is too Long")
        
        except Exception as e:
            e = str(e)
            print(e)
            self.cleanup(e)
        
        print("Method completed.")
        

if __name__ == '__main__':
    x = MyClass()
    x.run()