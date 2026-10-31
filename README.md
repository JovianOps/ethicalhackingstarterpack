# ReconSuite Portable

Portable network toolkit bundle — launches **Wireshark** + **Angry IP Scanner** side-by-side.

## Paths
- **Wireshark** — `D:\Wireshark\Wireshark.exe`
- **Angry IP Scanner** — `D:\Angry IP Scanner\ipscan.exe`

## Usage
1. Double-click `start.bat` to launch both tools.
2. Run `_configure_opener.py` once to pre-wire Wireshark as a right-click Opener in Angry IP Scanner:
   - Right-click any scanned host → **Open → Wireshark**
   - Wireshark opens with capture filter: `host <ip>`

## Opener Config
- Label: `Wireshark`
- Command: `D:\Wireshark\Wireshark.exe -f "host ${fetcher.ip}"`
- Run in terminal: unchecked

## Files
| File | Purpose |
|---|---|
| `start.bat` | Launches both tools |
| `_configure_opener.py` | Writes `openers.xml` to `%APPDATA%\Angry IP Scanner\` |
| `.gitignore` | Excludes `*.exe`, `build/`, `dist/` |
