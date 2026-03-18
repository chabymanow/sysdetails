import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFrame
from PySide6.QtWidgets import QGraphicsDropShadowEffect, QPlainTextEdit, QGroupBox
from PySide6.QtGui import QColor
from ui.ui_mainwindow import Ui_MainWindow
import subprocess
from PySide6.QtGui import QFont
import json
import functions as func
from PySide6.QtCore import QTimer
import os
import grp
import pwd
import psutil
import time
import socket
import requests


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        font = QFont("Monospace", 10)
        font.setStyleHint(QFont.TypeWriter)
        self.ui.discUsageInfo.setFont(font)
        self.ui.sensorInfo.setFont(font)
        self.ui.sysInfo.setFont(font)
        self.ui.userInfo.setFont(font)
        self.ui.CPU_info.setFont(font)
        self.ui.kernelInfo.setFont(font)
        self.ui.kernelModuleInfo.setFont(font)
        self.ui.RAMInfo.setFont(font)
        self.ui.UptimeInfo.setFont(font)
        self.ui.networkInfo.setFont(font)
        self.ui.runningAppInfo.setFont(font)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setOffset(5, 5)
        shadow.setColor(QColor(0, 0, 0, 160))

        self.ui.actionSystem_Info.triggered.connect(self.openSystemInfo)
        self.ui.actionBasic_Info.triggered.connect(self.openBasicInfo)
        self.ui.actionCPU_info.triggered.connect(self.openCPUInfo)
        self.ui.kernelRefresh.clicked.connect(self.getKernelModules)
        self.ui.actionDark.triggered.connect(func.set_dark_theme)
        self.ui.actionLight.triggered.connect(func.set_light_theme)
        self.ui.actionRunning_Apps.triggered.connect(self.openRunningApps)

        self.setupSensorTimer()
        self.getCPUinfo()
        self.getDiscUsage()
        self.getSensorInfo()
        self.getBasicInfo()
        self.userInfo()
        self.getNetworkDetails()
        self.show_page(0)

    def setupSensorTimer(self):
        self.sensorTimer = QTimer(self)
        self.sensorTimer.timeout.connect(self.getSensorInfo)
        self.sensorTimer.start(3000)  # 30000 ms = 30 seconds
    
    def setupRAMTimer(self):
        self.sensorTimer = QTimer(self)
        self.sensorTimer.timeout.connect(self.getRAMInfo)
        self.sensorTimer.timeout.connect(self.getUptimeDetails)
        self.sensorTimer.start(1000)  # 30000 ms = 30 seconds
        
    def show_page(self, index):
        self.ui.stackedWidget.setCurrentIndex(index)

    def openBasicInfo(self):
        self.setupSensorTimer()
        
        self.getDiscUsage()
        self.getSensorInfo()
        self.getBasicInfo()
        self.userInfo()
        self.getNetworkDetails()
        self.show_page(0)

    def openCPUInfo(self):
        self.setupRAMTimer()
        self.getCPUinfo()
        self.getRAMInfo()
        self.getUptimeDetails()
        self.show_page(1)

    def openSystemInfo(self):
        self.getKernelInfo()
        self.getKernelModules()
        self.show_page(2)

    def openRunningApps(self):
        self.getRunningApps()
        self.show_page(3)

    def getNetworkDetails(self):
        extIP = requests.get("https://api.ipify.org").text
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        interfaces = os.listdir("/sys/class/net")
        result = subprocess.run(
            ["ip", "route"],
            capture_output=True,
            text=True
        )

        self.ui.networkInfo.clear()
        self.ui.networkInfo.appendPlainText(f"{'Hostname':<15}: {hostname}")
        self.ui.networkInfo.appendPlainText(f"{'Local IP':<15}: {ip}")
        self.ui.networkInfo.appendPlainText(f"{'External IP':<15}: {extIP}")
        for iface in interfaces:
            if iface == "lo":
                continue
            mac_path = f"/sys/class/net/{iface}/address"
            try:
                with open(mac_path) as f:
                    mac = f.read().strip()
                self.ui.networkInfo.appendPlainText(f"{iface:<15}  MAC: {mac}")
            except FileNotFoundError:
                pass
        for line in result.stdout.splitlines():
            if line.startswith("default"):
                self.ui.networkInfo.appendPlainText(f"{'Default gateway':<15}: {line}")

    def getRunningApps(self):
        self.ui.runningAppInfo.clear()
        for p in psutil.process_iter():
            p.cpu_percent(None)
        time.sleep(1)
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent', 'username', 'status']):
            try:
                processes.append(proc.info)
            except:
                pass

        # sort by CPU
        processes = sorted(processes, key=lambda x: x['cpu_percent'], reverse=True)
        self.ui.runningAppInfo.appendPlainText(f"{'PID':<15}{'NAME':<40}{'USER':<20}{'CPU %':<10}{'RAM %':<10}{'STATUS':<12}")
        self.ui.runningAppInfo.appendPlainText("-" * 105)
        for p in processes[:50]:
            print(p)
            self.ui.runningAppInfo.appendPlainText(f"{str(p['pid']):<10} {p['name']:<40} {p['username']:<20} {"{:.1%}".format(p['cpu_percent'] / 100):<10} {"{:.1%}".format(p['memory_percent'] / 100):<10}{p['status']:<12}")

        # for proc in psutil.process_iter(['pid', 'name', 'username']):
        #     try:
        #         self.ui.runningAppInfo.appendPlainText(f"{proc.info['pid']:>10} | {proc.info['name']:<60} | {proc.info['username']}")
        #     except (psutil.NoSuchProcess, psutil.AccessDenied):
        #         pass

    def getRAMInfo(self):
        mem = psutil.virtual_memory()
        self.ui.RAMInfo.clear()
        self.ui.RAMInfo.appendPlainText(f"RAM")
        self.ui.RAMInfo.appendPlainText(f"{'Total memory':<20}: {mem.total / (1024**3):.2f} GB")
        self.ui.RAMInfo.appendPlainText(f"{'Available memory':<20}: {mem.available / (1024**3):.2f} GB")
        self.ui.RAMInfo.appendPlainText(f"{'Used memory ':<20}: {mem.used / (1024**3):.2f} GB")
        self.ui.RAMInfo.appendPlainText(f"{'RAM Usage':<20}: {mem.percent:.2f} %")
        self.ui.RAMInfo.appendPlainText(f" ")
        self.ui.RAMInfo.appendPlainText(f"{'Active Memory':<20}: {mem.active / (1024**3):.2f} GB")
        self.ui.RAMInfo.appendPlainText(f"{'Inactive Memory':<20}: {mem.inactive / (1024**3):.2f} GB")
        self.ui.RAMInfo.appendPlainText(f" ")
        self.ui.RAMInfo.appendPlainText(f"{'Buffers':<20}: {mem.buffers / (1024**3):.2f} GB")
        self.ui.RAMInfo.appendPlainText(f"{'Cached':<20}: {mem.cached / (1024**3):.2f} GB")
        self.ui.RAMInfo.appendPlainText(f" ")
        self.ui.RAMInfo.appendPlainText(f"{'Shared':<20}: {mem.shared / (1024**3):.2f} GB")
        self.ui.RAMInfo.appendPlainText(f"{'Slab':<20}: {mem.slab / (1024**3):.2f} GB")

    def getUptimeDetails(self):
        boot_time = psutil.boot_time()
        uptime_seconds = int(time.time() - boot_time)
        days = boot_time // 86400
        hours = (boot_time % 86400) // 3600
        minutes = (boot_time % 3600) // 60
        load1, load5, load15 = os.getloadavg()
        boot_time_str = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(boot_time))

        with open("/proc/uptime") as f:
            cpu_idle = float(f.read().split()[1])

        self.ui.UptimeInfo.clear()
        self.ui.UptimeInfo.appendPlainText(f"{'Boot time (seconds)':<20}: {boot_time}")
        self.ui.UptimeInfo.appendPlainText(f"{'Boot Date':<20}: {boot_time_str}")
        self.ui.UptimeInfo.appendPlainText(f"{'Uptime seconds':<20}: {uptime_seconds}")
        self.ui.UptimeInfo.appendPlainText(f"{'CPU idle time':<20}: {cpu_idle:.0f} seconds")
        self.ui.UptimeInfo.appendPlainText(
            f"{'Load average':<20}: {load1:.2f} {load5:.2f} {load15:.2f}"
        )       

    def getKernelModules(self):
        self.ui.kernelModuleInfo.clear()
        header = f"{'Module':<25}{'Size':<10}{'Used':<6}{'Dependencies':<70}{'State'}"
        self.ui.kernelModuleInfo.appendPlainText(header)
        self.ui.kernelModuleInfo.appendPlainText("-" * 125)

        with open("/proc/modules") as f:
            for line in f:
                parts = line.split()

                name = parts[0]
                size = parts[1]
                used = parts[2]
                deps = parts[3]
                state = parts[4]
                size = int(parts[1]) // 1024
                size = f"{size} KB"

                # truncate long dependency list
                if len(deps) > 65:
                    deps = deps[:65] + "..."

                self.ui.kernelModuleInfo.appendPlainText(
                    f"{name:<25}{size:>10}  {used:<10}{deps:<70}{state}"
                )


    def getKernelInfo(self):
        kernelInfo = os.uname()
        with open("/proc/cmdline") as f:
            bootImage = f.read()
        self.ui.kernelInfo.clear()
        self.ui.kernelInfo.appendPlainText(f"{'Op System Name':<18}: {kernelInfo.sysname}")
        self.ui.kernelInfo.appendPlainText(f"{'Hostname':<18}: {kernelInfo.nodename}")
        self.ui.kernelInfo.appendPlainText(f"{'Kernel versin':<18}: {kernelInfo.release}")
        self.ui.kernelInfo.appendPlainText(f"{'Kernel build info':<18}: {kernelInfo.version}")
        self.ui.kernelInfo.appendPlainText(f"{'CPU architecture':<18}: {kernelInfo.machine}")
        self.ui.kernelInfo.appendPlainText(f"{'BOOT Image':<18}: {bootImage}")

    def getCPUinfo(self):
        cpu_data = {}

        with open("/proc/cpuinfo", "r") as f:
            for line in f:
                if ":" in line:
                    key, value = line.split(":", 1)
                    key = key.strip()
                    value = value.strip()

                    # only keep first occurrence of each field
                    if key not in cpu_data:
                        cpu_data[key] = value

        self.ui.CPU_info.clear()

        wanted_keys = [
            "model name",
            "vendor_id",
            "cpu family",
            "model",
            "stepping",
            "cpu MHz",
            "cache size",
            "siblings",
            "cpu cores",
        ]

        for key in wanted_keys:
            if key in cpu_data:
                self.ui.CPU_info.appendPlainText(f"{key:<15} : {cpu_data[key]}")

        logical_count = os.cpu_count()
        self.ui.CPU_info.appendPlainText(f"{'logical CPUs':<15} : {logical_count}")

    def getDiscUsage(self):
        result = subprocess.run(["df", "-hP"], capture_output=True, text=True)
        lines = result.stdout.splitlines()

        rows = [line.split() for line in lines[1:]]

        self.ui.discUsageInfo.clear()

        self.ui.discUsageInfo.appendPlainText(
            f"{'Filesystem':<15}{'Size':<8}{'Used':<8}{'Avail':<8}{'Use%':<8}{'Mount'}"
        )
        self.ui.discUsageInfo.appendPlainText("-" * 60)

        for r in rows:
            self.ui.discUsageInfo.appendPlainText(
                f"{r[0]:<15}{r[1]:<8}{r[2]:<8}{r[3]:<8}{r[4]:<8}{r[5]}"
            )


    def userInfo(self):
        username = pwd.getpwuid(os.getuid()).pw_name
        uid = os.getuid()
        gid = os.getgid()

        groups = os.getgroups()

        self.ui.userInfo.clear()

        self.ui.userInfo.appendPlainText(f"Username: {username}")
        self.ui.userInfo.appendPlainText(f"UID: {uid}")
        self.ui.userInfo.appendPlainText(f"GID: {gid}")
        self.ui.userInfo.appendPlainText("")
        self.ui.userInfo.appendPlainText("Groups:")

        for g in groups:
            group = grp.getgrgid(g)
            self.ui.userInfo.appendPlainText(
                f"{group.gr_name:<10} GID={group.gr_gid:<5} Members={','.join(group.gr_mem)}"
            )

    def getSensorInfo(self):
        self.ui.sensorInfo.clear()
        data = func.extract_sensors()
        temperatures = func.extract_temperatures(data)
        for t in temperatures:
            self.ui.sensorInfo.appendPlainText(f"{t['adapter']:<15} {t['chip']:<25} {t['label']:<10} = {t['value']}°C")

    def getBasicInfo(self):
        info = {}

        with open("/etc/os-release") as f:
            for line in f:
                if "=" in line:
                    key, value = line.strip().split("=", 1)
                    info[key] = value.strip('"')
        longest_key = max(len(k) for k in info)

        for key, value in info.items():
            self.ui.sysInfo.appendPlainText(
                f"{key:<{longest_key}} : {value}"
            )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("")
    func.load_stylesheet(app, "main")
    func.load_stylesheet(app, "dark")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())