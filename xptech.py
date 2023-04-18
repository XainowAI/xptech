import platform
import subprocess

def get_os():
    return platform.system() + ' ' + platform.release()

def get_kernel():
    return subprocess.check_output(['uname', '-sr']).decode().strip()

def get_uptime():
    return subprocess.check_output(['uptime', '-p']).decode().strip()

def get_packages():
    return subprocess.check_output(['dpkg-query', '-f', '${binary:Package}\n', '-W']).decode().strip().count('\n')

def get_shell():
    return subprocess.check_output(['echo', '$SHELL']).decode().strip()

def get_terminal():
    return subprocess.check_output(['echo', '$TERM']).decode().strip()

def get_cpu():
    return subprocess.check_output(['lscpu']).decode().strip()

def get_gpu():
    return subprocess.check_output(['lspci', '-nnk']).decode().strip()

def get_memory():
    return subprocess.check_output(['free', '-h']).decode().split('\n')[1].split()[2:]

def neofetch():
    os_info = get_os()
    kernel_info = get_kernel()
    uptime_info = get_uptime()
    package_info = get_packages()
    shell_info = get_shell()
    terminal_info = get_terminal()
    cpu_info = get_cpu()
    gpu_info = get_gpu()
    memory_info = get_memory()

    print(f'''
        \u001b[1m{os_info}\u001b[0m {' '*(25-len(os_info))} {'-'*20}
        Kernel: {kernel_info}
        Uptime: {uptime_info}
        Packages: {package_info}
        Shell: {shell_info}
        Terminal: {terminal_info}
        CPU: {cpu_info}
        GPU: {gpu_info}
        Memory: {memory_info[0]} / {memory_info[1]}
    ''')

neofetch()
