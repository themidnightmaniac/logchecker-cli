# logchecker-cli
simple python script to check rip log score using the redacted API

## installation
```sh
pip install -r requirements.txt
```
or you can use your native package manager

## usage
first, set the environment variable `$RED_API_KEY` as you api key:
```sh
export RED_API_KEY='your_api_key'
```
then just run the script passing your log file as an argument:
```sh
./logchecker-cli [FILE]
```
the script will print the log's score and issues, if there are any.