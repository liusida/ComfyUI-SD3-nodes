import folder_paths
import comfy.sd
from nodes import CheckpointLoaderSimple

class SD3LoadCheckpoint (CheckpointLoaderSimple):
    @classmethod
    def INPUT_TYPES(s):
        return {"required": { "ckpt_name": (folder_paths.get_filename_list("checkpoints"), ),
                             "shift": ("FLOAT", {"default": 3.0, "min": 0.0, "max": 100.0, "step":0.01}),
                             }}
    RETURN_TYPES = ("MODEL", "VAE")
    FUNCTION = "main"

    CATEGORY = "sd3"

    def main(self, ckpt_name, shift):
        ckpt_path = folder_paths.get_full_path("checkpoints", ckpt_name)
        model, _, vae, _ = comfy.sd.load_checkpoint_guess_config(ckpt_path, output_vae=True, output_clip=False, embedding_directory=folder_paths.get_folder_paths("embeddings"))
        m = model.clone()

        sampling_base = comfy.model_sampling.ModelSamplingDiscreteFlow
        sampling_type = comfy.model_sampling.CONST

        class ModelSamplingAdvanced(sampling_base, sampling_type):
            pass

        model_sampling = ModelSamplingAdvanced(model.model.model_config)
        model_sampling.set_parameters(shift=shift)
        m.add_object_patch("model_sampling", model_sampling)

        return (m, vae)
