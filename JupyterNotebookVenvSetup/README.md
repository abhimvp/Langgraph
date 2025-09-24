# Jupyter Notebook

- What is it? -> It's a web application that runs in the browser in which you can create and share documents that contains live python code, equations, visualizations as well as text.
- There are two types of environments that you can create for your workspace: virtual and conda. These environments allow you to install packages without affecting other environments, isolating your workspace's package installations - [refer](https://code.visualstudio.com/docs/python/environments)
- Virtual environments: A virtual environment is a built-in way to create an environment. A virtual environment creates a folder that contains a copy (or symlink) to a specific interpreter. When you install packages into a virtual environment it will end up in this new folder, and thus isolated from other packages used by other workspaces.
- pip - The Python package manager that installs and updates packages. It's installed with Python 3.9+ by default (unless you are on a Debian-based OS; install python3-pip in that case).
- venv - Allows you to manage separate package installations for different projects and is installed with Python 3 by default (unless you are on a Debian-based OS; install python3-venv in that case)
- To create local environments in VS Code using virtual environments or Anaconda, you can follow these steps: open the Command Palette (Ctrl+Shift+P), search for the Python: Create Environment command, and select it.
- If you are creating an environment using Venv, the command presents a list of interpreters that can be used as a base for the new virtual environment.
- Create a virtual environment in the terminal
  If you choose to create a virtual environment manually, use the following command (where ".venv" is the name of the environment folder): - `python -m venv .venv`.
- To work with Python in Jupyter Notebooks, you must activate an Anaconda environment in VS Code, or another Python environment in which you've installed the Jupyter package.
- i will [use](https://docs.astral.sh/uv/) `uv` - An extremely fast Python package and project manager, written in Rust.A single tool to replace pip, pip-tools, pipx, poetry, pyenv, twine, virtualenv, and more.⚡️ 10-100x faster than pip.
- Let's Create a virtual environment:

```bash
abhis@Tinku MINGW64 ~/Desktop/Langgraph/Langgraph/JupyterNotebookVenvSetup (main)
$ uv venv jupyterEnv
Using CPython 3.12.7
Creating virtual environment at: jupyterEnv
Activate with: source jupyterEnv/Scripts/activate
abhis@Tinku MINGW64 ~/Desktop/Langgraph/Langgraph/JupyterNotebookVenvSetup (main)
$ source jupyterEnv/Scripts/activate
(jupyterEnv) #here we can see the virtual environment is activated.
abhis@Tinku MINGW64 ~/Desktop/Langgraph/Langgraph/JupyterNotebookVenvSetup (main)
$
# To work with jupyter Notebooks in VsCode - we should install jupyter package in this environment.
(jupyterEnv)
abhis@Tinku MINGW64 ~/Desktop/Langgraph/Langgraph/JupyterNotebookVenvSetup (main)
$ uv pip install jupyter
Using Python 3.12.7 environment at: jupyterEnv
Resolved 99 packages in 1.73s
Prepared 36 packages in 3.44s
Installed 99 packages in 5.52s
...
..
.

```

- You can create a Jupyter Notebook by running the Create: New Jupyter Notebook command from the Command Palette (Ctrl+Shift+P) or by `creating a new .ipynb file` in your workspace.
- Next, select a kernel using the kernel picker in the top right - it will show our `jupyterEnv/Scripts/python.exe` - select that. You're good to go now.

```text
It's helpful to understand the difference between these two uv commands:

uv add <package>: This command is for project dependency management. It looks for a pyproject.toml file and adds the package as a dependency to the [project.dependencies] section. This is useful when you want to share your project and allow others to easily install the exact same dependencies. If you wanted to use this, you would first run uv init to create the pyproject.toml file.

uv pip install <package>: This command is for installing packages directly into the current environment. It behaves almost identically to the standard pip install. It doesn't require a pyproject.toml file and is perfect for quick setups or when you're just working within a virtual environment without a formal project structure.

```

- Also if we want to add new packages/dependencies we need to work with in jupyter notebook - we do:

```bash
!uv pip install pydantic # will install package's into Jupyter's environment
```

- you can install additional packages via `!uv pip install <package_name>`.
