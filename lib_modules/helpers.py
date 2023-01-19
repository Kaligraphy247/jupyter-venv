import os, time
from subprocess import Popen, PIPE


def get_venv_folder():
    """
    Get the name of virtual environment by checking if
    user is currently in an ``activated`` venv environment.
    """
    venv_folder = os.environ.get("VIRTUAL_ENV")
    if venv_folder:
        venv_folder = (
            venv_folder.rsplit("\\") if os.name == "nt" else venv_folder.rsplit("/")
        )
        # print(venv_folder[-1])  # ! debug
        return venv_folder[-1]

    else:
        # print(venv_folder, "nothing")  # ! debug
        return None


def install_required_libraries(requirement_list: list):
    """Installs, jupyter and kernel."""

    pkg_1 = "jupyter"
    if not get_venv_folder() == None:
        print("All good, proceed!") #! debug

        # * always use context managers 😉
        # ? but context manager with Popen is unpredictable on windows
        # todo run on linux
        # with Popen(["msg * 'Hi!'"], stdout=PIPE) as proc:
        #     print(proc.stdout.read())

        # we only need one package so it will be hardcoded.
        proc = Popen(f"pip install {pkg_1}", stdout=PIPE, shell=True)
        print(proc.communicate()[0].decode("utf-8").strip())
        time.sleep(5)
        print("Finished Installing packages\nSetting venv kernel")
    else:
        print("Bad!")


requirement_list = ["tabulate", "autopep8"]

install_required_libraries(requirement_list)
# get_venv_folder()
