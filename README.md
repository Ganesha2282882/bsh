# bsh
NOTE: If an error with the shell has occurred, it will logout automatically.

My very own Linux shell called BSH (Brahma Shell).
## Installation
### Just copy the script:
```bash
# cp app.py /bin/bsh
# chmod +x /bin/bsh
```
### Change the shell (Removes your account from DMs, but still login using username.):
```bash
# chsh $YOUR_UNIX_USERNAME
```
Log out and log back in.
## Help
### Shell Built-in Commands:
```bsh
cd - change directory
echo - say something
exit - exit shell
```
On the 3 built-ins, an argument with special characters, including `!@#$%^&*()\/<space>'"-=+<>{}`, does not require single or double quotes ('/").

For example:
```bsh
echo Hello!@
```
is still valid. This is not the case for external commands, though.
