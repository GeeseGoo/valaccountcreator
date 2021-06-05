import time

# Send each character 1 by 1, making it more human
def type(element, word):
    for x in word:
        element.send_keys(x)
        time.sleep(0.2)
