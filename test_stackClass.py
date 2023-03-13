from  stack_class import Stack, FileStack

def test_open_fileStack():
    activeStack = FileStack("stack_test_file.txt")
    peekValue = "Thanks for coming in"
    assert peekValue == activeStack.peek()
    
def test_open_emptyFile():
    activeStack = FileStack("empty_file.txt")
    assert None == activeStack.peek()
    
def test_push_fileStack():
    activeStack = FileStack("push_stack.txt")
    item = "Hello World !"
    activeStack.push(item)
    assert str(item) == activeStack.peek()

def test_pop_empty_fileStack():
    activeStack = FileStack("empty_file.txt")
    item = None
    activeStack.pop()
    assert item == activeStack.peek()
    
def test_pop_fileStack():
    activeStack = FileStack("pop_test.txt")
    item = "pop test"
    activeStack.pop()
    assert str(item) == activeStack.peek()