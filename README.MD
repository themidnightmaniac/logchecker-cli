# logchecker-cli
a simple python script to check rip log score using the redacted API.

## installation
install the required dependencies with:
```sh
pip install -r requirements.txt
```
or you can use your native package manager.

you can also move this script to somewhere in your ```$PATH``` for ease of access.

## usage
first, set the environment variable `$RED_API_KEY` as you api key:
```sh
export RED_API_KEY='your_api_key'
```
on windows 
```sh
set RED_API_KEY="your_api_key"
```
then just run the script passing your log file as an argument:
```sh
./logchecker-cli [FILE]
```
instead, you can also run it on every file on a dir, by passing the --all option.
```sh
./logchecker-cli --all
```
the ```--all``` option will <i>also</i> look for files in subdirs, but be careful to run only in the directory you want.

the script will print the log's score and issues, if there are any.
