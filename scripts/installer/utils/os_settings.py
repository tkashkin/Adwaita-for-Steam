#!/usr/bin/env python3

import subprocess
import sys
import os

match sys.platform:
    case "linux":
        def linux_get_current_desktop() -> str:
            return os.getenv("XDG_CURRENT_DESKTOP", "unknown").lower()

        def linux_get_setting_portal(path: str, key: str) -> str | None:
            try:
                import dbus
                bus = dbus.SessionBus()
                desktop = bus.get_object("org.freedesktop.portal.Desktop", "/org/freedesktop/portal/desktop")
                settings = dbus.Interface(desktop, "org.freedesktop.portal.Settings")
                return str(settings.ReadOne(path, key))
            except:
                return None
        
        def linux_get_setting_gsettings(path: str, key: str) -> str | None:
            try:
                return subprocess.run(
                    args = ["gsettings", "get", path, key],
                    check = True,
                    capture_output = True,
                    text = True
                ).stdout.strip().strip("'")
            except:
                return None
        
        def linux_get_setting(path: str, key: str) -> str | None:
            return linux_get_setting_portal(path, key) or linux_get_setting_gsettings(path, key)
    
    case "win32" | "cygwin":
        import winreg

        def win32_get_reg_value(key: int, subkey: str, name: str) -> str | None:
            try:
                import winreg
                return winreg.QueryValueEx(winreg.OpenKey(key, subkey), name)[0]
            except:
                return None
    
    case "darwin":
        def darwin_get_setting(key: str, domain: str = "-g") -> str | None:
            try:
                return subprocess.run(
                    args = ["defaults", "read", domain, key],
                    check = True,
                    capture_output = True,
                    text = True
                ).stdout.strip()
            except:
                return None