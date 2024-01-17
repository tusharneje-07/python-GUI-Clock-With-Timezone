import ttkbootstrap as ttk
import FontSetting as Font 
import pytz
import datetime
fs = Font.SetFontFamily('Poppins')

def update_time():
    timeZone = selected.get()
    headingVar.set(timeZone)
    nowTime = (datetime.datetime.now(pytz.timezone(f'{timeZone}')).strftime('%H:%M:%S %p'))
    timeUpdate.set(str(nowTime))
    root.after(100, update_time)

# main root 
root = ttk.Window(themename='darkly')
root.geometry('700x350')
root.resizable(False, False)
root.title('World Clock')


# heading label 
headingVar = ttk.StringVar()
headLb = ttk.Label(root,textvariable=headingVar,font=fs.setFont_size_style(15,'bold'),foreground='#ff9b94')
headLb.pack(anchor='center',pady=20)


# update time
timeUpdate = ttk.StringVar()
mainTimeLabel = ttk.Label(root, textvariable=timeUpdate,font=fs.setFont_size_style(60,'bold'))
mainTimeLabel.pack(anchor='center')

# time zones
items = ['Asia/Kolkata','Asia/Dubai','Asia/Singapore','Europe/London','US/Alaska','Europe/Moscow','America/Chicago','GMT+0']
selected = ttk.StringVar(value=items[0])
cmbBox = ttk.Combobox(root,textvariable=selected)
cmbBox['values'] = items
cmbBox.pack(anchor='center')



update_time()

root.mainloop()