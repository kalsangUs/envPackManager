import subprocess
import os
from pathlib import Path


class EnvironmentReader:
    def __init__(self):
        pass

    def read_conda_environments(self):
        environments = []
        result = subprocess.run(
            ['conda', 'env', 'list'],
            capture_output=True, text=True
        ).stdout
        return result.splitlines()[3:-1]

    def find_virtualenvs(self, root_paths):
        """
        Scan given root directories for virtual environments and return as strings.

        Args:
            root_paths (list of str or Path): Directories to scan.

        Returns:
            list of str: Each string is "{envname} {envpath}".
        """
        env_list = []

        for root in root_paths:
            root = Path(root)
            if not root.exists():
                continue

            for dirpath, dirnames, filenames in os.walk(root):
                dirpath = Path(dirpath)

                # Check for virtualenv signature
                bin_path = dirpath / "bin" / "python"       # Mac/Linux
                scripts_path = dirpath / "Scripts" / "python.exe"  # Windows

                if bin_path.exists() or scripts_path.exists():
                    env_name = dirpath.name
                    env_list.append(f"{env_name} {str(dirpath)}")

                    # Skip deeper scanning inside this env
                    dirnames.clear()

        return env_list
