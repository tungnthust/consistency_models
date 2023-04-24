from setuptools import setup

setup(
    name="consistency-models",
    py_modules=["cm", "evaluations"],
    install_requires=[
        "blobfile",
        "torch",
        "tqdm",
        "numpy",
        "scipy",
        "pandas",
        "Cython",
        "piq",
        "joblib",
        "albumentations",
        "lmdb",
        "clip @ git+https://github.com/openai/CLIP.git",
        "mpi4py",
        "flash-attn",
        "pillow",
    ],
)
