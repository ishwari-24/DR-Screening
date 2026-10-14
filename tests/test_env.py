"""Checks that the Python environment is set up correctly."""
import sys

def check(name, import_name=None):
    try:
        module = __import__(import_name or name)
        print(f"[OK]   {name:<14} {getattr(module, '__version__', 'n/a')}")
        return module
    except ImportError:
        print(f"[FAIL] {name} is not installed")
        return None

print("Python:", sys.version.split()[0])
for pkg, imp in [("numpy", None), ("pandas", None), ("opencv-python", "cv2"),
                 ("pillow", "PIL"), ("scikit-image", "skimage"),
                 ("scikit-learn", "sklearn"), ("matplotlib", None),
                 ("tqdm", None)]:
    check(pkg, imp)

torch = check("torch")
check("torchvision")
if torch is not None:
    print("CUDA available (expected False on this laptop):", torch.cuda.is_available())
