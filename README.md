
# BlackKaliLoader

This tool aims to create an ethical **backdoor** using ngrok proxy for your raspberry.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Support](#support)
- [Contributing](#contributing)

## Requirements
- A stable internet connection
- Ngrok Token --> [Ngrok Website](https://ngrok.com/)
- Telegram Bot Token (BotFather) --> [Bot](https://telegram.me/botfather)
- ChatID Token --> [Guide](https://www.alphr.com/find-chat-id-telegram/)

## Installation & Usage

Clone or download this repository on your raspberry, preferred in a directory.

Then you'll need a ngrok token, just register on their [Website](https://ngrok.com/) and save it.
You need also a  telegram bot token and chatId. To get the bot token just create a bot on telegram with [Botfather](https://telegram.me/botfather) and save your token. To get your chatID follow this guide --> [Guide](https://www.alphr.com/find-chat-id-telegram/)

It's all set!
Now give the right permissions to the script and launch it:

```sh
mkdir blackkaliloader
chmod 775 blackkaliloader
./blackkaliloader -t '<YOURTOKEN>'
```
If you want to activate debug mode just leave **set -x** command on top of the script (Row 19).


## Support
If you encounter a bug using this script, please [open an issue](https://github.com/gdjohn4s/blackKaliLoader/issues/new) specifying some information like:
- SO
- Kernel
- Arch
- Python Version
- Little bug description



## Contributing

Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and [open a pull request](https://github.com/fraction/readme-boilerplate/compare/).


