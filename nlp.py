from textblob import TextBlob

def process_command(command):
    blob = TextBlob(command.lower())
    # Identifying actions from the commands
    if "move" in blob.words:
        if "left" in blob.words:
            return "move_left"
        elif "right" in blob.words:
            return "move_right"
    elif "jump" in blob.words:
        return "jump"
    elif "change" in blob.words and "color" in blob.words:
        return "change color"
    else:
        return "unknown command"
    

