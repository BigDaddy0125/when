import psutil

# 获取所有网络接口
net_ifs = psutil.net_if_addrs()
# print(net_ifs)#查询所有网络接口
# 过滤出IPv4地址
for interface, addrs in net_ifs.items():
    for addr in addrs:
        if str(addr.family) == 'AF_INET':
            print(f"{interface}: {addr.address}")

# 监控特定网络接口（例如'eth0'）的发送和接收字节
nic = psutil.net_io_counters(pernic=True)['WLAN']#将eth0修改为WLAN
# print(f"Bytes Sent: {nic.bytes_sent}, Bytes Received: {nic.bytes_recv}")
# 实时监控网络流量（简单示例）
import time

last_sent = nic.bytes_sent
last_recv = nic.bytes_recv
print("当前WLAN流量统计")
while True:
    nic = psutil.net_io_counters(pernic=True)['WLAN']#将eth0修改为WLAN
    print(f"发送: {round((nic.bytes_sent - last_sent)/1024,3)} kBytes,\t发送累计：{round(nic.bytes_sent/1024/1024,3)} MBytes\n接收: {round((nic.bytes_recv - last_recv)/1024,3)} kBytes,\t接收累计：{round(nic.bytes_recv/1024/1024,3)} MBytes")
    last_sent = nic.bytes_sent
    last_recv = nic.bytes_recv
    time.sleep(1)  # 每秒刷新一次
