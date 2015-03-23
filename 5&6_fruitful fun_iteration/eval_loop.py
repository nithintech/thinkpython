val='2+3*6'
def eval_loop():
    while True:
        if val=="done":
             break
        else:
            new=eval(val)
            return new
print eval_loop()
