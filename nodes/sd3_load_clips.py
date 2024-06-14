import folder_paths
from comfy_extras.nodes_sd3 import TripleCLIPLoader

class SD3LoadCLIPs(TripleCLIPLoader):
    @classmethod
    def INPUT_TYPES(s):
        return {"required": { "clip_g": (folder_paths.get_filename_list("clip"), ), "clip_l": (folder_paths.get_filename_list("clip"), ), "t5xxl": (folder_paths.get_filename_list("clip"), )}}

    FUNCTION = "main"

    def main(self, clip_g, clip_l, t5xxl):
        return self.load_clip(clip_g, clip_l, t5xxl)
