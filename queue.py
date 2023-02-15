
def enqueue(queue, item):
    queue.append(item)

def dequeue(queue):
    if(len(queue) == 0): return None 
    else: return queue.pop(0)
    
def findLen(queue):
    if(len(queue) == 0): return None 
    else: return len(queue)
    
def viewFront(queue):
    if (len(queue) == 0 ): return None
    else: return queue[0]

def main():
    queue = []
    while(True):
        selection = int(input ("""Queue Operations:
            1. EnQueue
            2. DeQueue
            3. Find length of Queue
            4. View front of the Queue
            5. Exit
            
            Select your option: """))
        
        if (selection == 1):
            item = input("Enter the item to be added: ")
            enqueue(queue, item)
            print(f"new Queue: {queue}")
        
        elif (selection == 2): print(dequeue(queue))      
        elif (selection == 3): print(findLen(queue))
        elif (selection == 4): print(viewFront(queue))
        else: 
            print (" Exitting")
            return
            
    
if __name__ == "__main__":
    main()

