[app]
title = Habit Tracker
package.name = habittracker
package.domain = org.bro.habittracker

source.dir = .
source.include_exts = py,kv,txt,json
source.exclude_exts = spec

source.main = main.py
version = 0.1

requirements = python3,kivy

orientation = portrait
fullscreen = 1

android.permissions = INTERNET

# Target Android API (stable version)
android.api = 34
android.minapi = 21
android.ndk = 25b
android.sdk = 24

# Force a compatible build tools version
android.build_tools_version = 34.0.0
android.available_build_tools = 34.0.0

# Accept licenses automatically
android.accept_sdk_license = true

# Architectures to build for
android.archs = arm64-v8a,armeabi-v7a

# Optional: Use this if your app has a custom icon
# icon.filename = %(source.dir)s/icon.png

# Uncomment to reduce app size (optional)
# android.downscale = 1

# Optional: Strip logs in release build
# log_level = 2

# Uncomment if you want to include assets like fonts, images, etc.
# android.add_assets = assets/

# Don't include tests in build
include_tests = false

# Include compiled Python bytecode (pyo/pyc)
include_pyo = false

# Set to 1 to enable verbose output
# log_level = 2

# Android specific environment variables (optional)
# android.extra_env =

# Signature stuff if needed later
# android.keystore = mykeystore.keystore
# android.keyalias = myalias
# android.keyalias_pass = password
# android.keystore_pass = password

# Application entry point
entrypoint = main.py

# Copy libraries in apk
android.copy_libs = 1

# (Optional) Build debug version
# build_mode = debug

# (Optional) Remove pycache files
# ignore_setup_py = true
