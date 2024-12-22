# logchecker-cli
a simple Python script to check RIP log scores using the Redacted API.

## installation
install the required dependencies with:
```sh
pip install -r requirements.txt
```
alternatively, you can use your system's native package manager.

you can also move this script to a directory that's in your `$PATH` for easier access.

## usage
first, set the environment variable `$RED_API_KEY` to your API key:
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
alternatively, you can run it on every log file in a directory by passing the `--all` option:
```sh
./logchecker-cli --all
```
the `--all` option will **also** look for files in subdirectories, so be cautious and make sure to run it while **in** the directory you want to scan.

the script will print the log's score and issues, if there are any.
