import os,random,mouse
I=10
while I>1:
    os.system(f"mkdir {random.randint(1, 1000000)}")
    mouse.move(random.randint(-683, 683), random.randint(-384, 384), False)
    mouse.double_click()
    os.system("start")
    os.system("calc")
    I-=1