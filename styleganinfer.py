# Copyright (c) 2019, NVIDIA CORPORATION. All rights reserved.
#
# This work is licensed under the Creative Commons Attribution-NonCommercial
# 4.0 International License. To view a copy of this license, visit
# http://creativecommons.org/licenses/by-nc/4.0/ or send a letter to
# Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

"""Minimal script for generating an image using pre-trained StyleGAN generator."""

import os
import pickle
import numpy as np
import PIL.Image
import dnnlib
import dnnlib.tflib as tflib
import config

def main():
    # Initialize TensorFlow.
    tflib.init_tf()
    
    f = './results/00029-sgan-custom-2gpu/network-snapshot-008040.pkl' #network loading 
    with open(f, 'rb') as pickle_file:
        _G, _D, Gs = pickle.load(pickle_file)
        # _G = Instantaneous snapshot of the generator. Mainly useful for resuming a previous training run.
        # _D = Instantaneous snapshot of the discriminator. Mainly useful for resuming a previous training run.
        # Gs = Long-term average of the generator. Yields higher-quality results than the instantaneous snapshot.

    # Print network details.
    #Gs.print_layers()
    os.makedirs(config.result_dir, exist_ok=True)
    # Pick latent vector.
    # for i in range(100):
    #print(Gs.input_shape)
    #print(Gs.shape)

    NUM=50 #number of images (100 ->00M)
    rnd = np.random.RandomState(10)
    latents = rnd.randn(NUM, Gs.input_shape[1])

    # Generate image.
    fmt = dict(func=tflib.convert_images_to_uint8, nchw_to_nhwc=True)
    images = Gs.run(latents, None, truncation_psi=0.7, randomize_noise=True, output_transform=fmt)
    #print(images[0].shape)

# Save image.

    i = 0
    for image in images:
        png_filename = os.path.join(config.result_dir, f'example{i}.png')
        PIL.Image.fromarray(image, 'RGB').save(png_filename)
        i += 1
    # png_filename = os.path.join(config.result_dir, 'example8040_s.png' )
    # PIL.Image.fromarray(images[0], 'RGB').save(png_filename)

if __name__ == "__main__":
    main()
