import folder_paths
import comfy.sd

class SD3CombineClips:
    @classmethod
    def INPUT_TYPES(s):
        return {"optional": { "clip_g": ("CLIP", ), "clip_l": ("CLIP", ), "t5xxl": ("CLIP", )
                             }}
    RETURN_TYPES = ("CLIP",)
    FUNCTION = "combine_clips"

    CATEGORY = "sd3"

    def combine_clips(self, clip_g, clip_l, t5xxl):
        clip_data = [clip_g, clip_l, t5xxl]
        return (clip_data,)