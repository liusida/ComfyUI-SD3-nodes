from .nodes.sd3_load_checkpoint import *
from .nodes.sd3_load_clips import *

NODE_CLASS_MAPPINGS = {
    "SD3LoadCheckpoint": SD3LoadCheckpoint,
    "SD3LoadCLIPs": SD3LoadCLIPs,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SD3LoadCheckpoint": "SD3 Load Checkpoint",
    "SD3LoadCLIPs": "SD3 Load CLIPs",
}
