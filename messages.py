def fix_message(msg):
    
    msg = msg.replace('xoxo', '')
    
    if msg == '':
        return None

    msg = msg[0].upper() + msg[1:]
    
    if len(msg) > 50:
        msg = msg[:50]

    return msg
