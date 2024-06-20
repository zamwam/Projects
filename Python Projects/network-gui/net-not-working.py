import socket
import tkinter as tk
from tkinter import messagebox

def scan_ports(ip, start_port, end_port, protocol):
    open_ports = []
    for port in range(start_port, end_port+1):
        if protocol == 'TCP':
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        elif protocol == 'UDP':
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip,port))
        if result == 0:
            try:
                service = socket.getservbyport(port, protocol.lower())
            except Exception as e:
                service = 'Unknown'
            open_ports.append((port, service))
        sock.close()
    return open_ports

def perform_scan():
    ip = ip_entry.get()
    start_port = int(start_port_entry.get())
    end_port = int(end_port_entry.get())
    protocol = protocol_var.get()
    open_ports = scan_ports(ip, start_port, end_port, protocol)
    messagebox.showinfo("Scan Results", f"Open ports and services: {open_ports}")

root = tk.Tk()

tk.Label(root, text="IP Address:").pack()
ip_entry = tk.Entry(root)
ip_entry.pack()

tk.Label(root, text="Start Port:").pack()
start_port_entry = tk.Entry(root)
start_port_entry.pack()

tk.Label(root, text="End Port:").pack()
end_port_entry = tk.Entry(root)
end_port_entry.pack()

protocol_var = tk.StringVar(root)
protocol_var.set('TCP')  # set the default option
protocol_option = tk.OptionMenu(root, protocol_var, 'TCP', 'UDP')
protocol_option.pack()

tk.Button(root, text="Scan Ports", command=perform_scan).pack()

root.mainloop()