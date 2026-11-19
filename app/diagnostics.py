"""Network diagnostics."""
import subprocess


def check_host(host: str) -> str:
    command = "ping -c 1 " + host
    return subprocess.check_output(command, shell=True, text=True)
