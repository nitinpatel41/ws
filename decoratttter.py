def dec1(func):
    def nowexec():
        print("Executing now")
        func()
        print("Executed")
    return nowexec
@dec1
def abc():
    print("Nitin")
abc()