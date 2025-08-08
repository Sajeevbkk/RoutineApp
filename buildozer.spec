[app]
# (str) Title of your application
title = Habit Tracker

# (str) Package name
package.name = habittracker

# (str) Package domain (used for signing)
package.domain = org.bro.habittracker

# (str) Source code where main.py is located
source.include_exts = py,kv,txt,json

# (str) Application versioning (major.minor.patch)
version = 0.1

# (str) Application requirements
requirements = python3,kivy

# (str) Supported orientation (one of: landscape, portrait, all)
orientation = portrait

# (bool) Fullscreen mode
fullscreen = 1

# (list) Permissions
android.permissions = INTERNET

# (int) Android API level to compile against
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (int) Android SDK version to use
android.sdk = 24

# (str) Architectures supported by the app (comma-separated)
android.archs = arm64-v8a,armeabi-v7a

# (str) Entry point of the app
source.main = main.py

# (str) Presplash screen
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
# icon.filename = %(source.dir)s/data/icon.png


[buildozer]
# (int) Log level (0 = error, 1 = warning, 2 = info, 3 = debug, 4 = trace)
log_level = 2

# (bool) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1