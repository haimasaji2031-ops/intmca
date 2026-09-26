# Python Installation: Frequently Asked Questions

## 1. Is Python free to download and use?

Yes. Python is open-source software and can be downloaded from [python.org](https://www.python.org/downloads/) without a purchase.

## 2. Which Python version should I install?

Choose the current stable Python 3 release offered for your operating system on the official downloads page. Check course or project instructions first if they require a particular version.

## 3. Do I need to uninstall an older Python version?

Usually not. Multiple versions can coexist, but it is important to know which interpreter a command is using. On Windows, `py -0p` lists Python installations known to the launcher. On macOS or Linux, `which -a python3` shows matching commands on PATH.

## 4. What are Python and pip?

Python is the programming language and interpreter used to run Python programs. `pip` is Python's package installer, used to install additional libraries. Running pip as `py -m pip` or `python3 -m pip` helps ensure it belongs to the selected interpreter.

## 5. What does “Add Python to PATH” mean?

PATH is a list of locations that a terminal searches when you enter a command. Adding Python to PATH lets the terminal find it by command name. If it is not enabled, Python may still be usable through the Windows `py` launcher or by repairing the installation settings.

## 6. Python is already installed on Linux. Should I reinstall it?

No, not unless you have a specific requirement. First check it with `python3 --version`. The operating system may rely on its system-managed Python, so do not remove or overwrite it.

## 7. Can I install Python without administrator rights?

Some installation methods support installing for the current user, but the available options depend on the operating system and computer policy. On a school or work device, ask the administrator if installation is restricted.

## 8. What should I do if verification fails?

Open a new terminal and try the operating-system-specific commands in [Installation.md](Installation.md). If they still fail, consult its troubleshooting table and record the exact error message.

## 9. Where should I get help?

Start with the [official Python documentation](https://docs.python.org/3/) and the installation instructions for your operating system. For a managed device, contact its administrator.