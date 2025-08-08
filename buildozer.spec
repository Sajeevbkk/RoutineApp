[app]
title = Habit Tracker
package.name = habittracker
package.domain = org.bro.habittracker

source.dir = .
source.main = main.py
source.include_exts = py,kv,txt,json

version = 0.1

requirements = python3,kivy

orientation = portrait
fullscreen = 1

android.permissions = INTERNET

android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 24
android.archs = arm64-v8a,armeabi-v7a

[buildozer]
# (int) Log level (0 = error, 1 = warning, 2 = info, 3 = debug, 4 = trace)
log_level = 2

# (bool) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
