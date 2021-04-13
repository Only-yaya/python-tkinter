#-*- encoding:utf-8 -*-
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
import tkinter.filedialog
from pygame.sprite import Sprite


'''
	下拉框选择
'''
def combobox_get_(num_s):
	# global声明 修改全局变量值
	global all_data
	all_data[num_s]['Combobox'] = cmb_dict[num_s].get()
	print(num_s,cmb_dict[num_s].get())

'''
	文件选择,获取文件路径
'''
def filenames_get_(num_s):
	# 文件多选
	filenames = 改tkinter.filedialog.askopenfilenames()
	# global声明 修全局变量值
	global all_data
	all_data[num_s]['filenames'] = filenames

'''
	添加按钮-追加显示下拉框和弹出框
'''
def addBox():
	# global声明 修改全局变量值
	global cmb_dict, all_data
	global num
	num = 1+num
	# 用户选择 数据存储
	all_data[num] = {}
	all_data[num]['Combobox'] = None
	all_data[num]['filenames'] = None

	# 下拉框
	cmb_dict[num] = ttk.Combobox(root,state='readonly')
	cmb_dict[num].pack()
	cmb_dict[num]['value'] = ('上海','北京','南京','广州')
	cmb_dict[num].bind("<<ComboboxSelected>>",lambda m=num: combobox_get_(num))

	# 文件选择
	btn = Button(root,text="文件选择对话框",command=lambda m=num: filenames_get_(m))
	btn.pack()


def showEntries():
	print('当前已添加条数:',num)
	text_str = ''
	for key in all_data.keys():
		print(key, all_data[key])
		text_str += str(key) +' : '+ str(all_data[key]) + '\n'
	lb.config(text = text_str)
	

# 声明变量,数据存储 
num = 0
# 输出结果(all_data),用于调取接口传递参数数据
all_data = {}
cmb_dict = {}

root = Tk()

showButton = Button(root, text='确认提交', command=showEntries)
showButton.pack()

addboxButton = Button(root, text='添加按钮', fg="Red", command=addBox)
addboxButton.pack()

lb = Label(root,text = '')
lb.pack()

root.mainloop()
