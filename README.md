
# 📦 Python Packaging & Publishing Guide

This repository is a **template** for creating and publishing Python packages to **PyPI** or **TestPyPI**.  
It includes a demo package (`hellodemo`) and a CLI (`hello-demo`).

---

## **1. Get Started — Clone This Repository**

```bash
git clone https://github.com/<your-username>/hello-demo.git
cd hello-super-package
```

---

## **2. Project Structure**

```
hello-super-package/
├─ src/hellodemo/__init__.py
├─ src/hellodemo/core.py
├─ tests/test_core.py
├─ README.md
├─ LICENSE
└─ pyproject.toml
```

---

## **3. Update `pyproject.toml`**

### **Minimal required fields**
Modify **`pyproject.toml`**:

```toml
[project]
name = "hello-super-package"       # Unique name on PyPI
version = "0.1.0"                  # Start from 0.1.0, bump for each release
description = "A tiny demo package that says hello."
readme = "README.md"
requires-python = ">=3.8"
license = { file = "LICENSE" }
authors = [{ name = "Your Name", email = "you@example.com" }]

# Add dependencies here if needed:
dependencies = [
    "pandas>=2.2",     # Example dependency
    "requests>=2.31"   # Optional
]

[project.urls]
Homepage = "https://github.com/<your-username>/hello-super-package"
Issues = "https://github.com/<your-username>/hello-super-package/issues"

[project.scripts]
hello-demo = "hellodemo.core:main"  # CLI entry point

[tool.hatch.build.targets.wheel]
packages = ["src/hellodemo"]

[tool.hatch.build.targets.sdist]
exclude = ["venv/**", ".venv/**", "dist/**", "build/**", "*.egg-info/**", "__pycache__/**"]
```

---

## **4. Handling Dependencies**

- Declare **all runtime dependencies** in `pyproject.toml` → `dependencies`.
- Use a `requirements.txt` **only for local development**:
    ```txt
    pandas>=2.2
    pytest
    ```
    Install dev deps:
    ```bash
    pip install -r requirements.txt
    ```
- **Do not create `setup.py`**. It’s deprecated with modern `pyproject.toml` + `hatchling`.

---

## **5. Create and Activate a Virtual Environment**
**Note**: you should create an environment outside the project directory

```bash
cd ..
python -m venv .packaging-venv
source .packaging-venv/bin/activate   # Windows: .\.packaging-venv\Scripts\activate
cd hello-super-package
```

---

## **6. Install Packaging Tools**

```bash
python -m pip install --upgrade pip
pip install build twine hatchling keyring
python -m keyring --disable
unset TWINE_USERNAME TWINE_PASSWORD 2>/dev/null || set TWINE_USERNAME= & set TWINE_PASSWORD=
```

---

## **7. Local Development & Testing**

```bash
pip install -e .
python -c "import hellodemo as h; print(h.say_hello('World'))"
hello-demo --name You
```

Run tests:
```bash
pip install pytest
pytest -q
```

---

## **8. Build the Package**

1. Bump the version in `pyproject.toml`.
2. Clean old artifacts:
   ```bash
   rm -rf dist build *.egg-info
   ```
3. Build:
   ```bash
   python -m build
   ```

Check artifacts:
```bash
ls dist
# hello_super_package-0.1.0-py3-none-any.whl
# hello_super_package-0.1.0.tar.gz
```

---

## **9. Upload to TestPyPI (Optional, Recommended)**

1. Register: [https://test.pypi.org/account/register/](https://test.pypi.org/account/register/)
2. Create token: [https://test.pypi.org/manage/account/token/](https://test.pypi.org/manage/account/token/)
3. Upload:
```bash
twine upload \
    --non-interactive \
    --repository-url https://test.pypi.org/legacy/ \
    -u __token__ \
    -p 'pypi-YOUR-TESTPYPI-TOKEN' \
    dist/*
```
4. Install from TestPyPI:
```bash
pip install \
    -index-url https://test.pypi.org/simple/ \
    --extra-index-url https://pypi.org/simple \
    hello-super-package==0.1.0
```

---

## **10. Publish to PyPI**

1. Register: [https://pypi.org/account/register/](https://pypi.org/account/register/)
2. Create token: [https://pypi.org/manage/account/token/](https://pypi.org/manage/account/token/)
3. Upload:
```bash
twine upload \
    --non-interactive \
    --repository-url https://upload.pypi.org/legacy/ \
    -u __token__ \
    -p 'pypi-YOUR-PYPI-TOKEN' \
    dist/*
```
4. Install from PyPI:
```bash
pip install hello-super-package
hello-demo --name Everyone
```

---

## **11. PyPI vs TestPyPI**

| Feature             | PyPI (Production)       | TestPyPI (Sandbox)  |
|---------------------|-------------------------|----------------------|
| URL                | https://pypi.org        | https://test.pypi.org |
| Token source       | PyPI                    | TestPyPI            |
| Package visibility | Public                  | Testing only        |
| Best use case      | Final releases          | Safe testing        |

---

## **12. Troubleshooting**

- **403 Forbidden:** Wrong token or URL.
- **Same version upload fails:** Bump `version` in `pyproject.toml`.
- **Dependencies fail on TestPyPI:** Use `--extra-index-url https://pypi.org/simple`.
- **Cannot import package:** Ensure code lives in `src/hellodemo/` and matches `[tool.hatch.build.targets.wheel]`.

---

## **13. Resources**

- [PyPI](https://pypi.org/)
- [TestPyPI](https://test.pypi.org/)
- [Python Packaging Guide](https://packaging.python.org/en/latest/)
- [Twine Docs](https://twine.readthedocs.io/)
- [PEP 621 Spec](https://peps.python.org/pep-0621/)
