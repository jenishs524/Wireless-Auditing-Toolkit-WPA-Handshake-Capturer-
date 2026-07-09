📁 Wireless Auditing Toolkit (WPA Handshake Capturer)

Description
Captures WPA handshakes using a monitor‑mode wireless interface and cracks them with a wordlist using aircrack‑ng.

Key Features

    Sets interface to monitor mode with airmon-ng.

    Sniffs for EAPOL frames (4‑way handshake).

    Saves handshake to handshake.cap.

    Cracks with aircrack‑ng using a wordlist.

    Dashboard shows handshake status.

Technologies

    Scapy, aircrack‑ng, Flask.

Prerequisites

    Wireless card that supports monitor mode.

    aircrack‑ng installed.

    Python 3, Scapy, Flask.

Installation
bash

sudo apt install aircrack-ng
pip install scapy flask jinja2

Usage

    Find your wireless interface: ip a.

    Start capture:
    bash

sudo python wpa_capture.py wlan0

In another terminal, start dashboard:
bash

python dashboard.py

After capturing, crack:
bash

aircrack-ng handshake.cap -w /usr/share/wordlists/rockyou.txt

Sample Output
text

[*] Handshake saved to handshake.cap
KEY FOUND! [ password ]

Notes

    Kill interfering processes: sudo airmon-ng check kill.

    Use a custom wordlist if rockyou.txt is not available.

