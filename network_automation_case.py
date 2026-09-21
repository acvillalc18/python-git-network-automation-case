def device_status(device):
    device_issues = []

    if device["status"] != "operational":
        device_issues.append("Device is not operational")

    if device["backup_status"] == "failed":
        device_issues.append("Backup Failed")

    if device["cpu_usage"] > 30:
        device_issues.append("CPU usage is high")

    if device["uptime_days"] < 30:
        device_issues.append("Uptime is low")

    if device["memory_usage"] > 60:
        device_issues.append("Memory usage is high")

    return device_issues

network_inventory = [
    {
        "hostname": "RTR-DATA-01",
        "device_type": "router",
        "management_ip": "192.168.1.1",
        "location": "Data Center",
        "status": "operational",
        "cpu_usage": 20,
        "memory_usage": 40,
        "uptime_days": 120,
        "backup_status": "completed"
    },
    {
        "hostname": "SW-DATA-01",
        "device_type": "switch",
        "management_ip": "192.168.1.10",
        "location": "Data Center",
        "status": "operational",
        "cpu_usage": 40,
        "memory_usage": 50,
        "uptime_days": 60,
        "backup_status": "failed"
    },
    {
        "hostname": "FW-DATA-01",
        "device_type": "firewall",
        "management_ip": "192.168.1.254",
        "location": "Data Center",
        "status": "operational",
        "cpu_usage": 20,
        "memory_usage": 40,
        "uptime_days": 110,
        "backup_status": "completed"
    },
    {
        "hostname": "RTR-MAIN-01",
        "device_type": "router",
        "management_ip": "192.168.2.1",
        "location": "Main Office",
        "status": "operational",
        "cpu_usage": 30,
        "memory_usage": 50,
        "uptime_days": 80,
        "backup_status": "completed"
    },
    {
        "hostname": "SW-MAIN-01",
        "device_type": "switch",
        "management_ip": "192.168.2.10",
        "location": "Main Office",
        "status": "operational",
        "cpu_usage": 20,
        "memory_usage": 40,
        "uptime_days": 90,
        "backup_status": "completed"
    },
    {
        "hostname": "FW-MAIN-01",
        "device_type": "firewall",
        "management_ip": "192.168.2.254",
        "location": "Main Office",
        "status": "warning",
        "cpu_usage": 40,
        "memory_usage": 70,
        "uptime_days": 40,
        "backup_status": "completed"
    },
    {
        "hostname": "RTR-OPS-01",
        "device_type": "router",
        "management_ip": "192.168.3.1",
        "location": "Operations Center",
        "status": "operational",
        "cpu_usage": 40,
        "memory_usage": 50,
        "uptime_days": 20,
        "backup_status": "completed"
    },
    {
        "hostname": "SW-OPS-01",
        "device_type": "switch",
        "management_ip": "192.168.3.10",
        "location": "Operations Center",
        "status": "down",
        "cpu_usage": 20,
        "memory_usage": 30,
        "uptime_days": 10,
        "backup_status": "failed"
    }
]


print("===Operational Report===")
print(f"Number of Network Devices: {len(network_inventory)}")

print("\n---Device Overview----")                    

for device in network_inventory:
    print(f"Hostname: {device['hostname']}")
    print(f"Device Type: {device['device_type']}")
    print(f"Management IP: {device['management_ip']}")
    print(f"Location: {device['location']}")
    print(f"Status: {device['status']}")
    print(f"CPU Usage: {device['cpu_usage']}%")
    print(f"Memory Usage: {device['memory_usage']}%")
    print(f"Uptime: {device['uptime_days']} days")
    print(f"Backup Status: {device['backup_status']}")
    print("-" * 40)

print("\n---Devices with Issues---")          

for device in network_inventory:
    device_issues = device_status(device)

    if device_issues:
        print(f"Device: {device['hostname']}")

        for issue in device_issues:
            print(f"- {issue}")

print("\n---Number of Devices by Location---")            

main_office_total = 0
data_center_total = 0
operations_center_total = 0

for device in network_inventory:

    if device["location"] == "Main Office":
        main_office_total += 1

    if device["location"] == "Data Center":
        data_center_total += 1

    if device["location"] == "Operations Center":
        operations_center_total += 1          

print(f"Main Office: {main_office_total}")
print(f"Data Center: {data_center_total}")
print(f"Operations Center: {operations_center_total}")


print("\n---Number of Devices by Type---")

router_total = 0
switch_total = 0
firewall_total = 0

for device in network_inventory:

    if device["device_type"] == "router":
        router_total += 1

    if device["device_type"] == "switch":
        switch_total += 1

    if device["device_type"] == "firewall":
        firewall_total += 1

print(f"Routers: {router_total}")
print(f"Switches: {switch_total}")
print(f"Firewalls: {firewall_total}")

print("\n---Average Uptime---")

total_uptime = sum(device["uptime_days"] for device in network_inventory)
average_uptime = total_uptime / len(network_inventory)

print(f"Average uptime across all devices: {average_uptime:.1f} days")