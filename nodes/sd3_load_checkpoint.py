import folder_paths
import comfy.sd
from nodes import CheckpointLoaderSimple

class SD3LoadCheckpoint (CheckpointLoaderSimple):
    @classmethod
    def INPUT_TYPES(s):
        return {"required": { "ckpt_name": (folder_paths.get_filename_list("checkpoints"), ),
                             }}
    RETURN_TYPES = ("MODEL", "VAE")
    FUNCTION = "load_checkpoint"

    CATEGORY = "sd3"

    def load_checkpoint(self, ckpt_name):
        ckpt_path = folder_paths.get_full_path("checkpoints", ckpt_name)
        out = comfy.sd.load_checkpoint_guess_config(ckpt_path, output_vae=True, output_clip=False, embedding_directory=folder_paths.get_folder_paths("embeddings"))
        return out[:2]
