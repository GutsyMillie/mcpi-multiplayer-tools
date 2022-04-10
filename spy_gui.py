#!/usr/bin/env python3

# spy_gui.py
# Basically spy.py but with a GUI
# Copyright (C) 2022 Gutsy Millie

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

from tkinter import *
from mcpi.minecraft import Minecraft
from sys import exit

try:
    mc = Minecraft.create()
    entityIds = mc.getPlayerEntityIds()
except:
    print("[ERROR] Minecraft client isn't running")
    exit()

root = Tk()
root.title("MCPi Spy")
root.geometry("200x280")
frame = Frame(root)
frame.pack()
title = Label(root, text="MCPi Spy", font=("Arial", 15))
title.pack()
listbox = Listbox(root)
listbox.pack()

def update():
    listbox.delete(0, listbox.size())
    entityIds = mc.getPlayerEntityIds()
    global z
    for z in range(0, len(entityIds)):
        listbox.insert(z, entityIds[z])

def teleport():
    selected = listbox.curselection()
    try:
        mc.camera.setNormal(entityIds[selected[0]])
    except:
        print("[ERROR] Can't find player")

update()
selected = None

update_btn = Button(root, text="Update", command=update)
update_btn.pack()
spy_btn = Button(root, text="Spy", command=teleport)
spy_btn.pack()

root.mainloop()
