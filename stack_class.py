class Stack:
    def __init__(self):
        self.items = [] 

    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
     
    def peek(self):
        return self.items[-1]
     
    def size(self):
        return len(self.items)


class FileStack: 
    def __init__(self,fileName):
        self.fileName = fileName

    def push(self, item):
        with open(self.fileName, "a") as f: 
            f.write(item + "\n")
        
    def pop(self):
        with open(self.fileName, "r+") as f:
            # Readlines will return list with all lines
            lines = f.readlines()
            
            # If File is non empty
            if lines:
                item = lines.pop()
                f.seek(0)
                f.truncate(0)
                f.write_lines(lines)
                return item
            else: return None
     
    def peek(self):
        with open(self.fileName, "r") as f:
            # Readlines will return list with all lines
            lines = f.readlines()
            try:
                item = lines[-1]
                return item
            except IndexError:
                return None 
                 
 