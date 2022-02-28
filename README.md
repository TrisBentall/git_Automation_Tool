# Repo Automation Tool
A simple tool to automate the creation of a new github repository.

This was developed for MacOS and has not been tested on Windows or Linux
## Installation

Depedencies:

Python3 is required to run the script
The only depedency required to install is selenium
```sh
pip3 install selenium
```

Clone the repo and add this line to your .zshrc file
```sh
source %filepath/.create_command.sh%
```

In the keys.py file enter your github username, password and profile url

In the .create_command file, enter the filepath for the tools directory and the target directory for your new repo's

## Usage example

To run the tool, in the command line enter create followed by the name of the repository you want to make.

For example if I wanted to make a new repo called Hello World, I would run
```sh
create "Hello World"
```

## Release History

* 0.0.1
    * Initial release

## Meta

Tris Bentall – [@trisbentall](https://twitter.com/trisbentall)

Distributed under the MIT license. See [``LICENSE``](https://mit-license.org) for more information.

[https://github.com/TrisBentall](https://github.com/TrisBentall)