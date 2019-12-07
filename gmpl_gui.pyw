import sys
from tk_html_widgets import HTMLLabel
from tkinter import *
from tkinter.filedialog import askopenfilename, askdirectory
from gmpl import *

if sys.platform == 'win32':
    MINECRAFT_FOLDER = '%APPDATA%\\.minecraft'
elif sys.platform == 'darwin':
    MINECRAFT_FOLDER = '~/Library/Application Support/minecraft'
else:
    MINECRAFT_FOLDER = '~/.minecraft'
MINECRAFT_FOLDER = os.path.expanduser(os.path.expandvars(MINECRAFT_FOLDER))

def main():
    root = Tk()
    root.title('Great Mod-Pack Launcher')

    #region Pack Load Area
    pack_load_frame = Frame(root)
    pack_path_var = StringVar()
    pack_path = ''
    pack = None
    def set_pack_path():
        nonlocal pack_path, pack
        pack_path = pack_path_var.get()
        pack = GmplFile(pack_path)
        info_render.set_html(pack.pretty_html())
    def use_pack_dialog():
        path = askopenfilename()
        pack_path_var.set(path)
    pack_load_box = Entry(pack_load_frame, textvariable=pack_path_var)
    pack_load_dialog_button = Button(pack_load_frame, text='...', command=use_pack_dialog)
    pack_load_button = Button(pack_load_frame, text='Load Pack', command=set_pack_path)
    pack_load_box.pack(side=LEFT, expand=YES, fill=X)
    pack_load_dialog_button.pack(side=LEFT)
    pack_load_button.pack(side=RIGHT, fill=X)
    pack_load_frame.pack(side=TOP, fill=X)
    #endregion

    info_render = HTMLLabel(root)
    info_render.pack(expand=YES, fill=BOTH)

    #region Inject Area
    inject_frame = Frame(root)
    inject_path_var = StringVar(None, MINECRAFT_FOLDER)
    inject_path = MINECRAFT_FOLDER
    def set_inject_path():
        nonlocal inject_path
        inject_path = inject_path_var.get()
        pack.inject(inject_path)
    def use_inject_dialog():
        path = askdirectory()
        inject_path_var.set(path)
    inject_box = Entry(inject_frame, textvariable=inject_path_var)
    inject_dialog_button = Button(inject_frame, text='...', command=use_inject_dialog)
    inject_button = Button(inject_frame, text='Inject', command=set_inject_path)
    inject_box.pack(side=LEFT, expand=YES, fill=X)
    inject_dialog_button.pack(side=LEFT)
    inject_button.pack(side=RIGHT, fill=X)
    inject_frame.pack(side=BOTTOM, fill=X)
    #endregion

    root.mainloop()

if __name__ == '__main__': main()