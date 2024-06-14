from .nodes.sd3_load_checkpoint import *
from .nodes.sd3_combine_clips import *

NODE_CLASS_MAPPINGS = {
    "SD3LoadCheckpoint": SD3LoadCheckpoint,
    "SD3CombineClips": SD3CombineClips,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SD3LoadCheckpoint": "SD3 Load Checkpoint",
    "SD3CombineClips": "SD3 Combine CLIPs (CLIP-G/-L/T5 XXL)",
}
