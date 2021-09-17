#!/usr/bin/env python3
from gi import require_version
require_version('Gtk', '3.0')
require_version('Nautilus', '3.0')

from gi.repository import Nautilus, GObject
import os, subprocess

PROCESSNAME = 'alacritty'

class AlacrittyExtension(Nautilus.MenuProvider, GObject.GObject):
    def __init__(self):
        pass

    def launch_alacritty(self, menu, files):
        path = files[0].get_location().get_path()
        args = '--working-directory'

        if os.path.isdir(path) and os.path.exists(path):
            subprocess.Popen([PROCESSNAME, args, path], shell=False)

    def get_file_items(self, window, files):
        item = Nautilus.MenuItem(
            name="AlacrittyOpen",
            label="Ouvrir dans Alacritty",
            tip="Open the current directory on alacritty"
        )
        item.connect('activate', self.launch_alacritty, files)
        return [item]

    def get_background_items(self, window, file_):
        item = Nautilus.MenuItem(
            name="AlacrittyOpen",
            label="Ouvrir dans Alacritty",
            tip="Open the current directory on alacritty"
        )
        item.connect('activate', self.launch_alacritty, [file_])
        return [item]
