import random
import tkinter as tk

# 暖心话语列表 - 激励大学生和高三学生 
messages = [
    "加油，你可以的",
    "坚持就是胜利",
    "努力终有回报",
    "今天也要加油",
    "你是最棒的",
    "相信自己",
    "未来可期",
    "继续努力",
    "你能行",
    "保持专注",
    "全力以赴",
    "坚持到底",
    "突破自我",
    "永不放弃",
    "梦想成真",
    "越战越勇",
    "超越自己",
    "脚踏实地",
    "积极向上",
    "青春无悔",
    "学业有成",
    "心无旁骛",
    "厚积薄发",
    "勇往直前",
    "信心十足",
    "斗志昂扬",
    "不负韶华",
    "天道酬勤",
    "学无止境",
    "精益求精",
    "力争上游",
    "奋发图强",
    "持之以恒",
    "壮志凌云",
    "马到成功",
    "前程似锦",
    "金榜题名",
    "旗开得胜",
    "鹏程万里",
    "功成名就"
]

# 背景色列表 - 增加更多颜色 
bg_colors = [
    "#FFC0CB", "#ADD8E6", "#FFB6C1", "#B8E6E6",
    "#FFD700", "#98FB98", "#FFA07A", "#E6E6FA",
    "#FF69B4", "#87CEFA", "#FFE4E1", "#90EE90",
    "#FFE4B5", "#D8BFD8", "#FFA500", "#87CEEB"
]

# 存储所有弹窗的列表 
popups = []
# 全局变量存储根窗口 
global_root = None


def create_popup(root, index):
    # 随机选择内容和样式 
    msg = random.choice(messages)
    bg = random.choice(bg_colors)
    font_size = random.randint(12, 14)  # 调整字体大小以适应缩小的弹窗 

    # 创建弹窗 
    popup = tk.Toplevel(root)
    popup.title(f"暖心话语 - {index}")  # 添加序号便于识别 
    popup.configure(bg=bg)

    # 增大弹窗尺寸20%（191x76 -> 229x91） 
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    popup_width = 229  # 增大20%后的宽度 
    popup_height = 91  # 增大20%后的高度
    # 确保弹窗范围覆盖整个屏幕 
    x = random.randint(0, screen_width - popup_width)
    y = random.randint(0, screen_height - popup_height)
    popup.geometry(f"{popup_width}x{popup_height}+{x}+{y}")  # 弹窗大小，位置 

    # 确保弹窗在最前面 
    popup.lift()
    popup.attributes('-topmost', True)

    # 提高视觉效果 - 添加边框效果 
    popup.resizable(False, False)  # 禁止调整窗口大小，保持美观 

    # 标签显示文字 - 使用更清晰的字体设置 
    label = tk.Label(popup, text=msg, bg=bg, font=("微软雅黑", font_size, "bold"), wraplength=200, justify="center")
    label.pack(padx=12, pady=12)

    # 将弹窗添加到列表中 
    popups.append(popup)


def create_popups(root, count, max_count):
    if count < max_count:
        print(f"创建第{count + 1}个弹窗")
        create_popup(root, count + 1)
        # 实现弹出速度从慢到快的效果 
        # 初始延迟500ms，每次减少30ms，最小延迟100ms 
        delay = max(100, 500 - (count * 30))
        print(f"下一个弹窗延迟: {delay}ms")
        # 使用after方法延迟创建下一个弹窗，避免阻塞事件循环 
        root.after(delay, create_popups, root, count + 1, max_count)
    else:
        print("所有弹窗创建完成，准备一起关闭...")
        # 所有弹窗创建完成后，5秒后一起关闭 
        root.after(5000, close_all_popups)


def close_all_popups():
    """关闭所有弹窗并结束程序"""
    print("开始关闭所有弹窗...")
    for popup in popups:
        try:
            popup.destroy()
        except:
            pass
    print("所有弹窗已关闭！")
    # 结束程序进程 
    if global_root:
        global_root.quit()
        global_root.destroy()


def main():
    global global_root
    print("程序开始运行，正在创建弹窗...")
    global_root = tk.Tk()
    global_root.withdraw()  # 隐藏主窗口 

    # 设置弹窗数量 
    max_popups = 400
    create_popups(global_root, 0, max_popups)

    global_root.mainloop()


if __name__ == "__main__":
    main()
