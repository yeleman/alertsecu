from rapidsms.messages.incoming import IncomingMessage

old = IncomingMessage.respond

def respond(self, *args, **kwargs):
    
    try:
        kwargs.pop('project_name')
    except:
        pass
        
    return old(self, *args, **kwargs)
    
IncomingMessage.respond = respond
