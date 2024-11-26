import os
from setuptools import setup, find_packages
import subprocess
import sys
from distutils.cmd import Command
with open('requirements.txt') as f:
    required = f.read().splitlines()
__version__ = "0.0.1"


class GetSubmodules(Command):
    def run(self):
        subprocess.check_call(['git', 'submodule', 'update', "--init", "--recursive"])
        build.run(self)


setup(
        name="met3r", 
        version=__version__,
        author="Mohammad Asim, Christopher Wewer, Thomas Wimmer, Bernt Schiele, Jan Eric Lenssen",
        author_email="masim@mpi-inf.mpg.de, cwewer@mpi-inf.mpg.de, twimmer@mpi-inf.mpg.de, schiele@mpi-inf.mpg.de, jlenssen@mpi-inf.mpg.de",
        description="Official Code for 'MET3R: Measuring Multi-View Consistency in Generated Images'",
        long_description=open('README.md').read(),
        long_description_content_type='text/markdown',
        url='https://github.com/mohammadasim98/met3r',
        packages=[
                "met3r",
                "dust3r",
                "dust3r/croco",
                "dust3r/croco/models",
                "dust3r/croco/models/curope",
                "dust3r/croco/utils",
                "dust3r/dust3r",
                "dust3r/dust3r/cloud_opt",
                "dust3r/dust3r/heads",
                "dust3r/dust3r/utils",
        ],
        install_requires=[
                "torch",
                "torchvision",
                "iopath",
                "roma",
                "matplotlib",
                "tqdm",
                "opencv-python",
                "scipy",
                "einops",
                "numpy",
                "jaxtyping",
                "pytorch-lightning",
                "torchmetrics",
                "pyglet<2",
                "timm==0.4.12",
                "huggingface-hub[torch]>=0.22",
                "featup@git+https://github.com/mhamilton723/FeatUp",
                "pytorch3d@git+https://github.com/facebookresearch/pytorch3d.git",
        ],

        classifiers=[
                'Programming Language :: Python :: 3',
                'License :: OSI Approved :: MIT License',
                'Operating System :: OS Independent',
        ],
        python_requires='>=3.6',
        cmdclass={"submodule": GetSubmodules}
        
)