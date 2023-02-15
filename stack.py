
def Spush(stack, item):
    stack.append(item)
    return stack

def Spop(stack):
    if(len(stack) == 0): return None 
    else: return stack.pop(-1)
    
def findLen(stack):
    if(len(stack) == 0): return None 
    else: return len(stack)
    
def viewTop(stack):
    if (len(stack) == 0 ): return None
    else: return stack[-1]

def main():
    stack = []
    while(True):
        selection = int(input ("""Stack Operations:
            1. Push
            2. Pop
            3. Find length of Stack
            4. View top of the Stack
            5. Exit
            
            Select your option: """))
        
        if (selection == 1):
            item = input("Enter the item to be added: ")
            Spush(stack, item)
            print(f"new Stack: {stack}")
        
        elif (selection == 2): print(Spop(stack))      
        elif (selection == 3): print(findLen(stack))
        elif (selection == 4): print(viewTop(stack))
        else: 
            print ("Exitting")
            return
            
    
if __name__ == "__main__":
    main()

def test_push():
    stack = []
    expectedResult = [2]
    actualResult = Spush(2)
    assert (expectedResult == actualResult)

def test_pop():
    stack = [1,2,3]
    expectedResult = 3
    actualResult = Spop(stack)
    assert (expectedResult == actualResult)
    
