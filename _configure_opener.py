#!/usr/bin/env python3
"""Pre-wire Wireshark as an 'Opener' in Angry IP Scanner config.

Writes openers.xml to the Angry IP Scanner config dir so that right-click →
Open → Wireshark launches with a live capture filter on the selected IP.

Target path: %APPDATA%\Angry IP Scanner\openers.xml
"""
import os, sys, xml.etree.ElementTree as ET

EXE = r"D:\Wireshark\Wireshark.exe"
FILTER = "host ${fetcher.ip}"

def opener_path():
    # Angry IP Scanner on Windows stores config in AppData\Roaming
    base = os.environ.get("APPDATA")
    if not base:
        base = os.path.join(os.environ.get("USERPROFILE", ""), "AppData", "Roaming")
    return os.path.join(base, "Angry IP Scanner", "openers.xml")

def main():
    p = opener_path()
    os.makedirs(os.path.dirname(p), exist_ok=True)

    root = ET.Element("openers")
    op = ET.SubElement(root, "opener")
    ET.SubElement(op, "label").text = "Wireshark"
    ET.SubElement(op, "command").text = f'{EXE} -f "{FILTER}"'
    ET.SubElement(op, "in_terminal").text = "false"

    tree = ET.ElementTree(root)
    tree.write(p, encoding="utf-8", xml_declaration=True)
    print(f"  wrote: {p}")
    print(f"  command: {EXE} -f \"{FILTER}\"")

if __name__ == "__main__":
    main()
