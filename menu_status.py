# -*- coding: utf-8 -*-
import subprocess
import sys

from Foundation import *
from AppKit import *
from PyObjCTools import AppHelper

__VERSION__ = "0.3"

class KwmStatusMenuAppDelegate(NSObject):
    mode = "init"
    mode_to_status = {"bsp": "B", "monocle": "M", "float": "F", "error": "E"}
    mode_list = ["Bsp", "Monocle", "Float"]
    def applicationDidFinishLaunching_(self, sender):
        self.statusItem = NSStatusBar.systemStatusBar().statusItemWithLength_(NSVariableStatusItemLength)
        self.to_display()
        self.statusItem.setHighlightMode_(FALSE)
        self.statusItem.setEnabled_(TRUE)

        # Notificatinos events
        events = ["NSWorkspaceActiveSpaceDidChangeNotification", "NSWorkspaceDidLaunchApplicationNotification", "NSWorkspaceDidTerminateApplicationNotification", "NSWorkspaceDidHideApplicationNotification", "NSWorkspaceDidUnhideApplicationNotification", "NSWorkspaceDidActivateApplicationNotification", "NSAccessibilityWindowCreatedNotification", "NSAccessibilityFocusedWindowChangedNotification", "NSWorkspaceDidDeactivateApplicationNotification"]
        nc = NSWorkspace.sharedWorkspace().notificationCenter()
        for event in events:
            nc.addObserver_selector_name_object_(self, self.observerEvent_, event, None)

        # menu
        self.menu = NSMenu.alloc().init()

        # Action
        for mode in self.mode_list:
            menuitem = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_(mode, 'clickEvent:', '')
            self.menu.addItem_(menuitem)

        # Separator and Quit action
        self.menu.addItem_(NSMenuItem.separatorItem())
        menuitem = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_('Quit', 'terminate:', '')
        self.menu.addItem_(menuitem)

        self.statusItem.setMenu_(self.menu)

        # Timer de refresh
        # self.timer = NSTimer.alloc().initWithFireDate_interval_target_selector_userInfo_repeats_(NSDate.date(), 2.0, self, 'refresh:', None, True)
        # NSRunLoop.currentRunLoop().addTimer_forMode_(self.timer, NSDefaultRunLoopMode)
        # self.timer.fire()

        self.get_mode()

    def clickEvent_(self, notification):
        mode = notification.title()
        if mode in self.mode_list:
            command = "kwmc space -t {0}".format(mode.lower())
            subprocess.Popen(command.split(" "), stdout=subprocess.PIPE, env={'PATH': '/usr/local/bin'}).communicate()
        self.get_mode()

    def observerEvent_(self, notifications):
        self.get_mode()

    def refresh_(self, notifications):
        self.get_mode()

    def get_mode(self):
        try:
            command = "kwmc query space active mode".split(" ")
            self.mode = subprocess.Popen(command, stdout=subprocess.PIPE, env={'PATH': '/usr/local/bin'}).communicate()[0].rstrip().translate(None, "[]")
        except:
            self.mode = "error"

        self.to_display()

    def to_display(self):
        # bsp | monocle | float | other
        self.statusItem.setToolTip_(self.mode)
        if self.mode in self.mode_to_status:
            self.statusItem.setTitle_(self.mode_to_status[self.mode])
        else:
            self.statusItem.setTitle_(self.mode)

def hide_dock_icon():
    NSApplicationActivationPolicyRegular = 0
    NSApplicationActivationPolicyAccessory = 1
    NSApplicationActivationPolicyProhibited = 2
    NSApp.setActivationPolicy_(NSApplicationActivationPolicyProhibited)

app = NSApplication.sharedApplication()
delegate = KwmStatusMenuAppDelegate.alloc().init()
app.setDelegate_(delegate)
hide_dock_icon()
AppHelper.runEventLoop()
