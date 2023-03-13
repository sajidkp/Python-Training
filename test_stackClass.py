from  stack_class import Stack, FileStack
path = "./tests/"
def test_open_fileStack():
    activeStack = FileStack(path + "stack_test_file.txt")
    peekValue = "Thanks for coming in"
    assert peekValue == activeStack.peek()
    
def test_open_emptyFile():
    activeStack = FileStack(path + "empty_file.txt")
    assert None == activeStack.peek()
    
def test_push_fileStack():
    activeStack = FileStack(path + "push_stack.txt")
    item = "Hello World !"
    activeStack.push(item)
    assert str(item) == activeStack.peek()

def test_pop_empty_fileStack():
    activeStack = FileStack(path + "empty_file.txt")
    item = None
    activeStack.pop()
    assert item == activeStack.peek()
    
def test_pop_fileStack():
    activeStack = FileStack(path + "pop_test.txt")
    item = "pop test"
    activeStack.pop()
    assert str(item) == activeStack.peek()