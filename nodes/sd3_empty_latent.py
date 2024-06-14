import torch
import comfy.model_management

class SD3EmptyLatent:
    def __init__(self):
        self.device = comfy.model_management.intermediate_device()

    @classmethod
    def INPUT_TYPES(s):
        resolution = []
        # Generate resolutions following this guideline: "Resolution should be around 1 megapixel and width/height must be multiple of 64"
        for width in range(512, 1921, 64):
            height = int(1024 * 1024 / width / 64) * 64
            resolution.append(f"{width}x{height}")

        return {"required": {"resolution": (resolution, {"default": "1024x1024"}),
                             "batch_size": ("INT", {"default": 1, "min": 1, "max": 16})}}
    RETURN_TYPES = ("LATENT",)
    FUNCTION = "main"

    CATEGORY = "latent/sd3"

    def main(self, resolution, batch_size=1):
        width, height = map(int, resolution.split('x'))
        latent = torch.zeros([batch_size, 16, height // 8, width // 8], device=self.device)
        return ({"samples":latent}, )
