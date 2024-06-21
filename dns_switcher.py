import os
import tkinter as tk
from tkinter import messagebox

def enable_cloudflare_dns():
    commands = [
        'netsh interface ipv4 set dns name="Wi-Fi" source="static" address="1.1.1.1"',
        'netsh interface ipv4 add dns name="Wi-Fi" address="1.0.0.1" index=2',
        'netsh interface ipv6 set dns name="Wi-Fi" source="static" address="2606:4700:4700::1111"',
        'netsh interface ipv6 add dns name="Wi-Fi" address="2606:4700:4700::1001" index=2'
    ]
    for command in commands:
        os.system(command)
    messagebox.showinfo("Success", "Cloudflare DNS enabled.")

def disable_cloudflare_dns():
    commands = [
        'netsh interface ipv4 set dns name="Wi-Fi" source="dhcp"',
        'netsh interface ipv6 set dns name="Wi-Fi" source="dhcp"'
    ]
    for command in commands:
        os.system(command)
    messagebox.showinfo("Success", "Default DNS settings restored.")

# Create the main window
root = tk.Tk()
root.title("DNS Switcher")

# Create buttons
enable_button = tk.Button(root, text="Enable Cloudflare DNS", command=enable_cloudflare_dns, width=30)
disable_button = tk.Button(root, text="Disable Cloudflare DNS", command=disable_cloudflare_dns, width=30)

# Arrange buttons in the window
enable_button.pack(pady=10)
disable_button.pack(pady=10)

# Run the application
root.mainloop()