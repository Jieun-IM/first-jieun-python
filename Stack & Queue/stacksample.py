from inspect import Stack


def stack_sample():
    document_actions = Stack()
    
    document_actions.push('action: enter; text_id: 1; text: My favourite document')
    
    document_actions.push('action: format; text_id: 1; alignment: center')
    
    document_actions.pop()
    
    document_actions.push('action: format; text_id: 1; style: bold')
    print(document_actions.stack)    