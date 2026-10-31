# ReconSuite — Ethical Hacking Starter Pack

Portable network toolkit bundle — launches **Wireshark** + **Angry IP Scanner** side-by-side.
All tools bundled in `external/`, no install required.

## Layout
```
ReconSuite/
├── start.bat              # Double-click to launch both tools
├── _configure_opener.py   # Pre-wire Wireshark as Opener in Angry IP Scanner
├── external/
│   ├── Wireshark/         # Portable Wireshark
│   └── AngryIPScanner/    # Portable Angry IP Scanner
└── .gitignore
```

## Files
| File | Purpose |
|---|---|
| `start.bat` | Launches both tools |
| `_configure_opener.py` | Writes `openers.xml` to `%APPDATA%\Angry IP Scanner\` |
| `.gitignore` | Excludes `*.exe`, `build/`, `dist/` |
