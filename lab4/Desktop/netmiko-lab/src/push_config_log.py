import yaml
import logging
from jinja2 import Environment, FileSystemLoader
from netmiko import ConnectHandler

# Logging Setup
logging.basicConfig(filename="network_config.log", level=logging.INFO,
                    format="%(asctime)s:%(levelname)s:%(message)s")

# Load YAML
with open("network_topology.yaml") as file:
    topology = yaml.safe_load(file)

# Setup Jinja2
env = Environment(loader=FileSystemLoader("."))
template = env.get_template("router_config.j2")

device_template = {
    "device_type": "cisco_ios",
    "username": "student",
    "password": "Meilab123",
    "port": 22,
}

for router, data in topology["routers"].items():
    try:
        logging.info(f"Connecting to {router}")
        config = template.render(router=router, loopback=data["loopback"], interfaces=data["interfaces"])

        device = device_template.copy()
        device["ip"] = data["interfaces"][list(data["interfaces"].keys())[0]].split("/")[0]

        net_connect = ConnectHandler(**device)
        output = net_connect.send_config_set(config.splitlines())
        logging.info(f"{router} configuration complete")
        net_connect.disconnect()

    except Exception as e:
        logging.error(f"Failed to configure {router}: {e}")

