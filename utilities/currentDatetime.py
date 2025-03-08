import datetime

def take_current_time():
    return datetime.datetime.now().strftime("%H_%M_%S_%d_%m_%Y")