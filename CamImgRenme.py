from tkinter import *
import tkinter as tk
from tkinter.filedialog import askdirectory,askopenfilename
import os
from tkinter import messagebox
import shutil

def sub_test_selectPath():
    #使用askdirectory()方法返回文件夹的路径
    image_folder = askdirectory() 
    #当打开文件路径选择框后点击"取消" 输入框会清空路径，所以使用get()方法再获取一次路径
    if image_folder == "":
        sub_testpath.get() 
    # 实际在代码中执行的路径为“\“ 所以替换一下
    else:
        image_folder = image_folder.replace("/", "\\") 
        sub_testpath.set(image_folder)

def ad_check_selectPath():
    #使用askdirectory()方法返回文件夹的路径
    image_folder = askdirectory() 
    #当打开文件路径选择框后点击"取消" 输入框会清空路径，所以使用get()方法再获取一次路径
    if image_folder == "":
        ad_checkpath.get() 
    # 实际在代码中执行的路径为“\“ 所以替换一下
    else:
        image_folder = image_folder.replace("/", "\\") 
        ad_checkpath.set(image_folder)

def sunglass_trans_selectPath():
    #使用askdirectory()方法返回文件夹的路径
    image_folder = askdirectory() 
    #当打开文件路径选择框后点击"取消" 输入框会清空路径，所以使用get()方法再获取一次路径
    if image_folder == "":
        sunglass_transpath.get() 
    # 实际在代码中执行的路径为“\“ 所以替换一下
    else:
        image_folder = image_folder.replace("/", "\\") 
        sunglass_transpath.set(image_folder)

def sub_rename():
    # 存储重命名规则的字符串列表
    image_folder = sub_testpath.get()
    projectnameget = projectname.get()
    # eyebrowsdisget = eyebrowsdis.get()
    image_size_widthget = image_size_width.get()
    image_size_heightget = image_size_height.get()
    rename_list = ["Image1", "Image2", "Image3","Image4"]
    # image_size_width=input("请输入图片Width:")
    # image_size_height=input("请输入图片Height:")
    for foldername in os.listdir(image_folder):
        folder_path = os.path.join(image_folder, foldername)
        if os.path.isdir(folder_path):
            # 统计当前子文件夹中的图片数量
            image_count = len([name for name in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, name)) and name.endswith(('.bmp','.png','.jpg'))])
            # 检查图片数量是否符合固定值
            if image_count != 4:
                # messagebox.showerror(f"文件夹 {foldername} 中的图片数量不为 {4}，当前数量为 {image_count}")
                print(f"文件夹 {foldername} 中的图片数量不为{4}，当前数量为 {image_count}")
                # 遍历指定目录下的所有文件夹
            else:
                for root, dirs, files in os.walk(image_folder):
                    for i,file in enumerate(files):
                        if file.lower().endswith(('.bmp','.png','.jpg')):
                            # 获取当前文件夹名称
                            folder_name = os.path.basename(root)
                            old_file_path = os.path.join(root, file)     
                            # 带眉心距信息
                            # new_file_name = folder_name+"_" + rename_list[i % len(rename_list)] + "_"+ image_size_width + "_" + image_size_height + "_" + eyebrowsdisget + "cm" + "_"+ projectnameget +"_" + '{:03d}'.format(i) + os.path.splitext(file)[1]
                            # 不带眉心距信息
                            new_file_name = folder_name + "_" + rename_list[i % len(rename_list)] + "_"+ image_size_widthget + "_" + image_size_heightget + "_" + projectnameget + "_"+ '{:03d}'.format(i) + os.path.splitext(file)[1]
                            new_file_path = os.path.join(root, new_file_name)
                            os.rename(old_file_path, new_file_path)
                            print('Convert %s to %s ...'%(old_file_path, new_file_path))
def ad_check_rename():
    # 存储重命名规则的字符串列表
    image_folder = ad_checkpath.get()
    projectnameget = projectname.get()
    # eyebrowsdisget = eyebrowsdis.get()
    image_size_widthget = image_size_width.get()
    image_size_heightget = image_size_height.get()
    eyebrowsdis5thget = eyebrowsdis5th.get()
    # print(eyebrowsdis5thget,type(eyebrowsdis5thget))
    # quit()
    eyebrowsdis50thget = eyebrowsdis50th.get()
    eyebrowsdis95thget = eyebrowsdis95th.get()
    height_list = ["5th", "50th", "95th"]
    # print(height_list,type(height_list))
    eyebrowsdis_list = [eyebrowsdis5thget,eyebrowsdis50thget,eyebrowsdis95thget]
    # print(len(eyebrowsdis_list),type(eyebrowsdis_list))
    # quit()
    for root, dirs, files in os.walk(image_folder):
        for i,file in enumerate(files):
            if file.lower().endswith(('.bmp','.png','.jpg')):
                # 获取当前文件夹名称
                folder_name = os.path.basename(root)
                old_file_path = os.path.join(root, file)     
                # 带眉心距信息
                new_file_name = folder_name + "_" + height_list[i % len(height_list)] + "_" + eyebrowsdis_list[i % len(eyebrowsdis_list)] + "cm" + "_" + image_size_widthget + "_" + image_size_heightget + "_" + projectnameget + "_" + '{:03d}'.format(i) + os.path.splitext(file)[1]
                new_file_path = os.path.join(root, new_file_name)
                os.rename(old_file_path, new_file_path)
                print('Convert %s to %s ...'%(old_file_path, new_file_path))

def sunglass_trans_rename():
    # 存储重命名规则的字符串列表
    image_folder = sunglass_transpath.get()
    projectnameget = projectname.get()
    # eyebrowsdisget = eyebrowsdis.get()
    image_size_widthget = image_size_width.get()
    image_size_heightget = image_size_height.get()
    keyword1 = 'daytime'
    keyword2 = 'night'
    sunglass_trans_list = ["30%", "40%", "50%","60%","70%","80%","90%"]
    sunglass_trans_list_new = [num for num in sunglass_trans_list for _ in range(3)]
    # print(sunglass_trans_list_new)
    sight_list = ["目视前方","左后视镜","右后视镜"]
    for folder_name in os.listdir(image_folder):
        folder_path = os.path.join(image_folder, folder_name)
        print(folder_name)
        # 确保当前路径是文件夹而不是文件，并且文件夹名称包含指定关键词
        if os.path.isdir(folder_path) and keyword1 in folder_name:
            for i, file in enumerate(os.listdir(folder_path)):
                if file.lower().endswith(('.bmp','.png','.jpg')):
                    old_file_path = os.path.join(folder_path, file)
                    new_file_name = folder_name + "_" + '关窗' + '_' + sunglass_trans_list[i % len(sunglass_trans_list)] + "_" + '目视前方' + "_" + image_size_widthget + "_" + image_size_heightget + "_" + projectnameget + "_" + '{:03d}'.format(i) + os.path.splitext(file)[1]
                    new_file_path = os.path.join(folder_path, new_file_name)
                    shutil.move(old_file_path, new_file_path)
                    print('Convert %s to %s ...'%(old_file_path, new_file_path))
        # else:
        #     print('keyword1 invalid!')
        if os.path.isdir(folder_path) and keyword2 in folder_name:
            for i, file in enumerate(os.listdir(folder_path)):
                if file.lower().endswith(('.bmp','.png','.jpg')):
                    old_file_path = os.path.join(folder_path, file)
                    new_file_name = folder_name + "_" + '关窗' + '_' + sunglass_trans_list_new[i % len(sunglass_trans_list_new)] + "_" + sight_list[i % len(sight_list)] + "_" + image_size_widthget + "_" + image_size_heightget + "_" + projectnameget + "_" + '{:03d}'.format(i) + os.path.splitext(file)[1]
                    new_file_path = os.path.join(folder_path, new_file_name)
                    shutil.move(old_file_path, new_file_path)
                    print('Convert %s to %s ...'%(old_file_path, new_file_path))
        # else:
        #     print('keyword2 invalid!')
root = tk.Tk()
root.title("CamImgRename_Tool")
root.geometry("650x500")


projectname = StringVar()
# eyebrowsdis = StringVar()
image_size_width = StringVar()
image_size_height = StringVar()
eyebrowsdis5th = StringVar()
eyebrowsdis50th = StringVar()
eyebrowsdis95th = StringVar()

sub_testpath = StringVar()
sub_testpath.set(os.path.abspath("."))
ad_checkpath = StringVar()
ad_checkpath.set(os.path.abspath("."))
sunglass_transpath = StringVar()
sunglass_transpath.set(os.path.abspath("."))
# 项目基本信息
basicinf =tk.LabelFrame(root, text="基本信息",padx=2, pady=2)
basicinf.grid(row=0, column=1, sticky = 'w',padx=20)
basicinflabel1 = Label(basicinf, text="项目名称:").grid(row=0, column=1)
basicinfentry1 = tk.Entry(basicinf, textvariable=projectname, width=15).grid(row=0, column=2)
basicinflabel2 = Label(basicinf, text="图片宽度(Width):").grid(row=0, column=3)
basicinfentry2 = tk.Entry(basicinf, textvariable=image_size_width, width=15).grid(row=0, column=4)
basicinflabel3 = Label(basicinf, text="图片高度(Height):").grid(row=0, column=5)
basicinfentry3 = tk.Entry(basicinf, textvariable=image_size_height, width=15).grid(row=0, column=6)

# 数模校核命名
ad_check =tk.LabelFrame(root, text="数模校核",padx=2, pady=2)
ad_check.grid(row=1, column=1,sticky = 'w',padx=20)
ad_checkeyelabel1 = Label(ad_check, text="5th眉心距(cm):").grid(row=0, column=0, sticky = 'w')
ad_checkeyeentry1 = tk.Entry(ad_check, textvariable=eyebrowsdis5th, width=10).grid(row=0, column=1, sticky = 'w')
ad_checkeyelabel2 = Label(ad_check, text="50th眉心距(cm):").grid(row=1, column=0, sticky = 'w')
ad_checkeyeentry2 = tk.Entry(ad_check, textvariable=eyebrowsdis50th, width=10).grid(row=1, column=1, sticky = 'w')
ad_checkeyelabel3 = Label(ad_check, text="95th眉心距(cm):").grid(row=2, column=0, sticky = 'w')
ad_checkeyeentry3 = tk.Entry(ad_check, textvariable=eyebrowsdis95th, width=10).grid(row=2, column=1, sticky = 'w')
ad_checklabel = Label(ad_check, text="图片路径:").grid(row=3, column=0, sticky = 'w')
ad_checkentry = tk.Entry(ad_check, textvariable=ad_checkpath, width=55).grid(row=3, column=1, sticky = 'w')
ad_checkbutton1 = Button(ad_check, text="路径选择", command=ad_check_selectPath).grid(row=3, column=2, sticky = 'w')
ad_checkbutton2 = Button(ad_check, text="Rename", command=ad_check_rename).grid(row=3, column=3, sticky = 'w')

# 主观画质命名
sub_test = tk.LabelFrame(root, text="主观画质",padx=2, pady=2)
sub_test.grid(row=2, column=1,sticky = 'w',padx=20)
# sub_testlabel2 = Label(sub_test, text="眉心距(cm):").grid(row=0, column=2)
# sub_testentry2 = tk.Entry(sub_test, textvariable=eyebrowsdis).grid(row=0, column=3)
sub_testlabel = Label(sub_test, text="图片路径:").grid(row=0, column=0)
sub_testentry = tk.Entry(sub_test, textvariable=sub_testpath, width=60).grid(row=0, column=1)
sub_testbutton1 = Button(sub_test, text="路径选择", command=sub_test_selectPath).grid(row=0, column=2)
sub_testbutton2 = Button(sub_test, text="Rename", command=sub_rename).grid(row=0, column=3)

# 墨镜透过率
sunglass_trans = tk.LabelFrame(root, text="墨镜透过率",padx=2, pady=2)
sunglass_trans.grid(row=3, column=1,sticky = 'w',padx=20)
sunglass_translabel = Label(sunglass_trans, text="图片路径:").grid(row=0, column=0)
ssunglass_transentry = tk.Entry(sunglass_trans, textvariable=sunglass_transpath, width=60).grid(row=0, column=1)
sunglass_transbutton1 = Button(sunglass_trans, text="路径选择", command=sunglass_trans_selectPath).grid(row=0, column=2)
sunglass_transbutton2 = Button(sunglass_trans, text="Rename", command=sunglass_trans_rename).grid(row=0, column=3)


root.mainloop()