#!/usr/bin/env python3

# spy.py
# A Minecraft Pi multiplayer tool to see with the eyes of other players
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

from mcpi.minecraft import Minecraft
from os import system

system("clear")
mc = Minecraft.create()

while True:
    entityIds = mc.getPlayerEntityIds()
    print("\033[1;31;40mSpy v1.0\033[0;37;40m")
    print("-" * 20)
    for x in entityIds:
        try:
            print("ID :",x)
        except:
            pass
    print("")
    answer = input("ID or \"R\" to reset : ")
    type(answer)
    if answer == "R":
        mc.camera.setNormal()
    if answer != "U" and answer != "R":
        mc.camera.setNormal(answer)
    system("clear")
