# InstaUnpinner
SSL certificate unpinner for Android Facebook Messenger

You need **ROOT** access to perform this operations!

# Supported devices
Every rooted Android device based on x86, x86_64, arm-v7a or arm64-v8a

# Tested for
| App name | Version | Architecture |
| - | - | - |
| Facebook Messenger | 275.0.0.20.119 | arm-v7a |

# How to use?

## Messenger
Execute following commands in your terminal:

`adb shell`

`su`

`cp /data/data/com.facebook.orca/lib-superpack-xz/libcoldstart.so /sdcard/libcoldstart.so`

`exit`

`exit`

`adb pull /sdcard/libcoldstart.so`

`python patch.py libcoldstart.so`

`adb push patch_libcoldstart.so /sdcard/patch_libcoldstart.so`

`adb shell`

`su`

`cp /sdcard/patch_libcoldstart.so /data/data/com.facebook.orca/lib-superpack-xz/libcoldstart.so`

`exit`

`exit`

Restart your Messenger app
