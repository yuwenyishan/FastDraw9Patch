# coding:utf-8
from Tkinter import *  # 导入 Tkinter 库
import tkFileDialog as FileDialog
import tkMessageBox as MessageBox
import draw9Patch

__author__ = 'Jack_long'


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.Input_text = StringVar()
        self.CheckVar1 = IntVar()
        self.Title = Label(self, text='Fast9Patch', width=50, height=3)
        self.input = Entry(self, textvariable=self.Input_text, width=50, bd=3)
        self.chose_folder = Button(self, text='选择文件夹', command=self.callback, width=10, height=1, bd=3)
        self.chose_file = Button(self, text='选择文件', command=self.callback2, width=10, height=1, bd=3)
        self.checkBox = Checkbutton(self, text='包含子文件夹', variable=self.CheckVar1, onvalue=1, offvalue=0, height=2)
        self.startBtn = Button(self, text='开始制作', command=self.start_made, width=10, height=1, bd=3)
        self.MFrame = Frame(self)
        self.messageList = Listbox(self.MFrame, width=55, bd=3, height=12)
        self.pack()
        self.create_view()

    def create_view(self):
        self.Title.grid(row=0, column=0, columnspan=5, padx=5, pady=5)
        self.input.grid(row=1, column=0, columnspan=5, padx=5, pady=5)

        self.checkBox.grid(sticky=W + N, row=2, column=0, padx=5, pady=5)

        self.chose_file.grid(sticky=W + N, row=2, column=1, padx=5, pady=5)

        self.chose_folder.grid(sticky=W + N, row=2, column=2, padx=5, pady=5)

        self.startBtn.grid(sticky=W + N, row=2, column=3, padx=5, pady=5)

        self.MFrame.grid(row=3, column=0, columnspan=5, padx=5, pady=5)
        self.messageList.pack()

    def start_made(self):
        self.messageList.delete(0, END)
        # print self.Input_text.get(), self.CheckVar1.get()
        if self.Input_text.get():
            # self.add_log(self.Input_text.get())
            draw9Patch.draw_patch(app, self.Input_text.get(), self.CheckVar1.get() == 1)
        else:
            MessageBox.showerror('error', '请选择文件夹')

    def callback(self):
        # 调用filedialog模块的askdirectory()函数去打开文件夹
        file_path = FileDialog.askdirectory()
        self.input.delete(0, END)  # 清空entry里面的内容
        if file_path:
            self.Input_text.set(file_path)  # 将选择好的路径加入到entry里面

    def callback2(self):
        # 调用filedialog模块的askopenfile()函数去打开文件
        file_path = FileDialog.askopenfilename()
        self.input.delete(0, END)  # 清空entry里面的内容
        if file_path:
            self.Input_text.set(file_path)  # 将选择好的路径加入到entry里面

    def add_log(self, log):
        self.messageList.insert(0, log)


def show_error(error):
    MessageBox.showinfo(title='处理失败', message=error)


def show_log(x_app, log):
    x_app.add_log(log.encode('utf-8'))


if __name__ == '__main__':
    try:
        root = Tk(className='fast9Patch')  # 创建窗口对象的标题
        root.geometry("400x400")  # 创建窗口对象大小
        app = Application(master=root)
        app.mainloop()
    except BaseException, e:
        show_error(e.message)
