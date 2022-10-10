
def add_to_counter():
    global count
    count += 1

def substract_from_counter():
    global count
    count -= 1

def update_config(count):
    global config 
    config['variables']['count'] = str(count)
    with open('config.ini', 'w') as configfile:
        config.write(configfile)