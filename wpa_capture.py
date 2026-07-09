#!/usr/bin/env python3
"""
Project 18 – Wireless Auditing Toolkit (WPA Handshake Capturer)
Captures WPA handshakes using a monitor-mode interface.
"""
import sys
import time
import subprocess
from scapy.all import *

def set_monitor_mode(interface):
    """Set interface to monitor mode using airmon-ng."""
    try:
        # Kill interfering processes
        subprocess.run(["sudo", "airmon-ng", "check", "kill"], check=False)
        subprocess.run(["sudo", "airmon-ng", "start", interface], check=True)
        return f"{interface}mon"
    except Exception as e:
        print(f"[!] Failed to set monitor mode: {e}")
        return None

def capture_handshake(iface):
    """Sniff for EAPOL frames (handshake)."""
    print(f"[*] Capturing on {iface}. Press Ctrl+C to stop.")
    packets = []
    def handler(pkt):
        if pkt.haslayer(EAPOL):
            packets.append(pkt)
            print(f"[+] Handshake frame captured (total: {len(packets)})")
            if len(packets) >= 4:
                wrpcap("handshake.cap", packets)
                print("[*] Handshake saved to handshake.cap")
                return True
    try:
        sniff(iface=iface, prn=handler, store=0, timeout=120)
    except KeyboardInterrupt:
        print("\n[*] Stopped by user.")
    return packets

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: sudo python wpa_capture.py <interface>")
        print("Example: sudo python wpa_capture.py wlan0")
        print("\nTo find your interfaces: ip a")
        sys.exit(1)
    iface = sys.argv[1]
    monitor_iface = set_monitor_mode(iface)
    if not monitor_iface:
        # Try using the interface directly if monitor mode fails
        print(f"[*] Trying to capture directly on {iface}...")
        monitor_iface = iface
    capture_handshake(monitor_iface)