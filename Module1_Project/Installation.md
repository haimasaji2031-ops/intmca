# Python Installation Guide

## 1. Software Requirements

### Hardware

- A desktop or laptop that meets the minimum requirements of its operating system.
- An internet connection to download the installer or operating-system packages.
- Enough free disk space for the Python installation and any programs you plan to create.

### Software and access

- Windows, macOS, or a Linux distribution that is still supported by its vendor.
- Permission to install software. On a managed school or workplace computer, an administrator may need to perform the installation.
- A terminal application: PowerShell or Windows Terminal on Windows, Terminal on macOS, or a terminal emulator on Linux.

No separate compiler or paid software is needed for a standard Python installation.

## 2. Before You Begin

1. Identify your operating system and whether it is 64-bit or ARM-based, if the download page asks.
2. Visit the [official Python downloads page](https://www.python.org/downloads/) and select the current stable Python 3 release for your operating system.
3. Avoid third-party download sites. If using Linux, prefer your distribution's official package manager.

## 3. Installation Steps

### Windows

1. On the official Python website, open the Windows downloads and choose the recommended current Python 3 download for your computer.
2. Open the downloaded installer and follow its prompts. If the installer offers an **Add Python to PATH** option, enable it if you want to run Python using the `python` command in a new terminal.
3. Choose the standard installation unless you have a specific reason to customize it. Approve the installation if Windows requests permission.
4. When setup finishes, close and reopen PowerShell or Windows Terminal so it can read updated environment settings.

### macOS

1. On the official Python website, open the macOS downloads and choose the current installer package that matches your Mac.
2. Open the downloaded `.pkg` file and follow the installation prompts.
3. Open Terminal after the installation completes. macOS includes system tools that may use Python internally; do not remove or replace those system files.

### Linux

Python 3 may already be installed. Check it first using the verification command below. If it is missing, use your distribution's documentation and package manager. For example:

**Ubuntu or Debian-based distributions:**

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

**Fedora:**

```bash
sudo dnf install python3 python3-pip
```

Package names can differ by release. Do not remove or replace the system-managed Python; operating-system tools may depend on it.

## 4. Verification Steps

Open a **new** terminal window and run the commands for your operating system.

**Windows PowerShell:**

```powershell
py --version
py -m pip --version
py -c "print('Python is working')"
```

If `py` is unavailable, try `python` in its place. A successful setup displays a Python 3 version, a pip version, and the text `Python is working`.

**macOS or Linux:**

```bash
python3 --version
python3 -m pip --version
python3 -c "print('Python is working')"
```

The commands should print a Python 3 version, a pip version, and the text `Python is working`. If the first command reports that Python cannot be found, use the troubleshooting section.

## 5. Troubleshooting

| Problem | What to try |
| --- | --- |
| `python` or `py` is not recognized on Windows | Reopen the terminal. Try `py --version`; if neither command works, rerun the official installer and check its PATH option, or use the installation manager provided on the official Python download page. |
| `python` opens the Microsoft Store instead of Python | Try `py --version`. If Python is installed but the `python` command is redirected, review Windows **Manage app execution aliases** settings or repair the Python installation. |
| `python3` is not found on macOS or Linux | Confirm installation completed, open a new terminal, and retry. On Linux, install Python 3 using your distribution's package manager. |
| `pip` is not recognized | Run pip through the interpreter: `py -m pip --version` on Windows or `python3 -m pip --version` on macOS/Linux. |
| A permission error appears | Use an account permitted to install software or ask the computer administrator. Avoid solving package permission issues by running every command as administrator or root. |
| The version shown is unexpected | Multiple Python installations may exist. Check with `py -0p` on Windows or `which -a python3` on macOS/Linux, and use the intended interpreter explicitly. |
| The installer will not open or download | Download it again from [python.org](https://www.python.org/downloads/), confirm it matches your operating system and processor, and check whether security software or organization policies block installation. |

If the issue continues, note the operating system, the exact command, and the complete error message before asking an administrator or consulting the official Python documentation.

## Conclusion

Python can be installed from the official Python website or, on Linux, from the distribution's package manager. Following the steps for the correct operating system and running the verification commands confirms that the interpreter is available. The troubleshooting table and [FAQ](FAQ.md) provide next steps for common setup questions.

## References

- [Python downloads](https://www.python.org/downloads/)
- [Python documentation](https://docs.python.org/3/)