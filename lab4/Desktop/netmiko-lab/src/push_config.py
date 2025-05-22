import yaml
from jinja2 import Environment, FileSystemLoader
from netmiko import ConnectHandler

# Load YAML
with open("network_topology.yaml") as file:
    topology = yaml.safe_load(file)

# Setup Jinja2
env = Environment(loader=FileSystemLoader("."))
template = env.get_template("router_config.j2")

# Device login template (assumed same for all)
device_template = {
    "device_type": "cisco_ios",
    "username": "student",
    "password": "Meilab123",
    "port": 22,
}

# Push config to each device
for router, data in topology["routers"].items():
    print(f"Configuring {router}...")
    config = template.render(router=router, loopback=data["loopback"], interfaces=data["interfaces"])

    device = device_template.copy()
    device["ip"] = data["interfaces"][list(data["interfaces"].keys())[0]].split("/")[0]

    net_connect = ConnectHandler(**device)
    output = net_connect.send_config_set(config.splitlines())
    print(output)
    net_connect.disconnect()

