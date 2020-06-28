'''
    @Auther: CuzMiles
    @Date: 2020/6/28
'''
from pynput.keyboard import Key, Listener as KeyboardListener
from pynput.mouse import Controller, Button

#def on_press(key):
# 启动判断
flag = None
# 键值记录
mkey = None
# 获取鼠标控制器
mouse = Controller()

# 按键释放监听
def onkey_release(key):
    global flag, mkey
    if key == Key.f8 or key == Key.f9:
        # 初始化
        if mkey is not key:
            mkey = key
            flag = False
            # 释放鼠标按键
            mouse.release(Button.left)
            mouse.release(Button.right)
        flag = (flag == False)
        # 获取模拟状态
        btn = None
        if key == Key.f8:
            btn = Button.left
        elif key == Key.f9:
            btn = Button.right
        # 判断状态
        if flag:
            mouse.press(btn)
        else:
            mouse.release(btn)
        # print(flag,btn)
    elif key == Key.f10:
        mouse.release(Button.left)
        mouse.release(Button.right)
        exit()

# 主函数
if __name__ == '__main__':
    print("*********************")
    print("* FF  模拟加载成功  *")
    print("* F8  开启左键长按  *")
    print("* F9  开启右键长按  *")
    print("* F10 释放关闭程序  *")
    print("*********************")
    # 注册监听器
    with KeyboardListener(on_press=None, on_release=onkey_release) as klistener:
        klistener.join()