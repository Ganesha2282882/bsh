# bsh (<a href="https://repl.it/@GaneshaSharma/BSH">run on <a href="https://repl.it">repl.it</a></a>)
NOTE: If an error with the shell has occurred, it will logout automatically.

My very own Linux shell called BSH (Brahma Shell).

## Installation
### Do the normal make:
```bash
$ make
# make install
```
There is no `./configure`. You also need `pyinstaller`.
### Change the shell (Removes your account from DMs, but still you can login using username.):
```bash
# chsh $YOUR_UNIX_USERNAME
```
Use `/usr/local/bin/bsh` as the path.
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
