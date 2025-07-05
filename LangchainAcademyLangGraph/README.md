# Introduction to LangGraph

This course is divided into six modules, starting with the basics and gradually progressing to more advanced topics.

- Set up LangGraph Studio:
  LangGraph Studio is a custom IDE for viewing and testing agents.
  Studio can be run locally and opened in your browser on Mac, Windows, and Linux.
  See documentation here on the local Studio development server and here.
  Graphs for LangGraph Studio are in the module-x/studio/ folders.
  To start the local development server, **run the following command in your terminal in the /studio directory each module:**
  `langgraph dev`
  You should see the following output:

  - 🚀 API: http://127.0.0.1:2024
  - 🎨 Studio UI: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024
  - 📚 API Docs: http://127.0.0.1:2024/docs

- Open your browser and navigate to the Studio UI: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024

To use Studio, you will need to create a .env file with the relevant API keys
Run this from the command line to create these files for module 1 to 6, as an example:

```cmd
for i in {1..6}; do
  cp module-$i/studio/.env.example module-$i/studio/.env
  echo "OPENAI_API_KEY=\"$OPENAI_API_KEY\"" > module-$i/studio/.env
done
echo "TAVILY_API_KEY=\"$TAVILY_API_KEY\"" >> module-4/studio/.env
```

## Setup

- **`Python version:`** To get the most out of this course, please ensure you're using `Python 3.11`. This version is required for best compatibility with LangGraph. If you're on an older version, upgrading will ensure everything runs smoothly.

```bash
$ python --version
Python 3.11.9
```

- **`Create an environment and install dependencies`**:

  - Will use `UV` : Refer [docs](https://docs.astral.sh/uv/guides/projects/)

```bash
abhis@Tinku MINGW64 ~/Desktop/Langgraph/Langgraph/LangchainAcademyLangGraph (main)
$ uv init
Initialized project `langchainacademylanggraph`
# example of adding libraries and uv automatically creates a virtual environment for us.
abhis@Tinku MINGW64 ~/Desktop/Langgraph/Langgraph/LangchainAcademyLangGraph (main)
$ uv add requests
Using CPython 3.12.7
Creating virtual environment at: .venv
Resolved 6 packages in 203ms
Installed 5 packages in 86ms
 + certifi==2025.6.15
 + charset-normalizer==3.4.2
 + idna==3.10
 + requests==2.32.4
 + urllib3==2.5.0
# Activate the virtual environment
abhis@Tinku MINGW64 ~/Desktop/Langgraph/Langgraph/LangchainAcademyLangGraph (main)
$ source .venv/Scripts/activate # Windows
(langchainacademylanggraph) # we can see venv activated.
abhis@Tinku MINGW64 ~/Desktop/Langgraph/Langgraph/LangchainAcademyLangGraph (main)
$
```

- Good to know commands: Creating and working on Python projects, i.e., with a pyproject.toml.

  uv init: Create a new Python project.
  uv add: Add a dependency to the project.
  uv remove: Remove a dependency from the project.
  uv sync: Sync the project's dependencies with the environment.
  uv lock: Create a lockfile for the project's dependencies.
  uv run: Run a command in the project environment.
  uv tree: View the dependency tree for the project.
  uv build: Build the project into distribution archives.
  uv publish: Publish the project to a package index.

- Since we will be working on Jupyter Notebooks - refer [docs](https://docs.astral.sh/uv/guides/integration/jupyter/)
  - Using Jupyter within a project: If you're working within a project, you can start a Jupyter server with access to the project's virtual environment via the following: `uv run --with jupyter jupyter lab` . By default, jupyter lab will start the server at [http://localhost:8888/lab](http://localhost:8888/lab). Within a notebook, you can import your project's modules as you would in any other file in the project. For example, if your project depends on requests, import requests will import requests from the project's virtual environment.
  - However, if you need to install additional packages from within the notebook, there are a few extra details to consider.
    - Creating a kernel : If you need to install packages from within the notebook, we recommend creating a dedicated kernel for your project. Kernels enable the Jupyter server to run in one environment, with individual notebooks running in their own, separate environments.
    - In the context of uv, we can create a kernel for a project while installing Jupyter itself in an isolated environment, as in uv run --with jupyter jupyter lab. Creating a kernel for the project ensures that the notebook is hooked up to the correct environment, and that any packages installed from within the notebook are installed into the project's virtual environment.
    - To create a kernel, you'll need to install ipykernel as a development dependency: `uv add --dev ipykernel`
    - Then, you can create the kernel for project with: `uv run ipython kernel install --user --env VIRTUAL_ENV $(pwd)/.venv --name=project`
    - From there, start the server with: `uv run --with jupyter jupyter lab` -> OPENS UP BROWSER WITH THIS FOLDER DIRECTORY.
    - When creating a notebook, select the project kernel from the dropdown. Then use `!uv add pydantic` to add `pydantic` to the project's dependencies, or !uv pip install pydantic to install pydantic into the project's virtual environment without persisting the change to the project pyproject.toml or uv.lock files. Either command will make import pydantic work within the notebook.
- Will create test jupyter notebook and try to add dependencies.
