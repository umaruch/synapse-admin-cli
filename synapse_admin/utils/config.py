from genericpath import isfile
import json
import dataclasses
from pathlib import Path

from synapse_admin.utils import dirs
from synapse_admin.types.config import Config, LogedUser


def save(server_url, user_id, access_token):
    config = Config(server_url, LogedUser(user_id, access_token))
    with open(dirs.get_homedir()+"/.synapse-admin.config.json", "w") as conf_file:
        if dataclasses.is_dataclass(config):
            json.dump(dataclasses.asdict(config), conf_file)


def load():
    if not Path(dirs.get_homedir()+"/.synapse-admin.config.json").isfile():
        print("Config file not found. Please init synapse-admin by command: synapse-admin init")
        exit(1)
    
    with open(dirs.get_homedir()+"/.synapse-admin.config.json", "r") as conf_file:
        config_dict = json.load(conf_file)
        config = Config(server_url=config_dict.get("server_url"))
        if config_dict.get("loged_as"):
            config.loged_as = LogedUser(**config_dict["loged_as"])
            
        return config
