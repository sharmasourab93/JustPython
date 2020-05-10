class A:
    
    def execute(self):
        print("Main Execution method")
        
        
def class_method(base):
    class B(base):
        def pre_execute(self):
            print("Pre Execute")
            
        def post_execute(self):
            print("post execute")

    return B()


if __name__ == '__main__':
    obj_pass = class_method(A)
    obj_pass.pre_execute()
    obj_pass.execute()
    obj_pass.post_execute()
