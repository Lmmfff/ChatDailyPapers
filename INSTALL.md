# Installation Notes

This project targets `Python 3.9`.

If you install dependencies with `Python 3.13`, packages pinned in `requirements.txt` such as `Pillow==9.4.0` may fail to build or install.

Recommended setup with conda:

```powershell
conda env create -f environment.yml
conda activate chatdailypapers-py39
pip install -r requirements.txt
```

If the environment already exists:

```powershell
conda activate chatdailypapers-py39
pip install -r requirements.txt
```
