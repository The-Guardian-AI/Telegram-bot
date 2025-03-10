
### Update Package Lists and Install Dependencies:

```bash
sudo apt update
sudo apt install python3-pip python3-venv -y
```

This will install the necessary tools for managing Python and creating a virtual environment.

### Create a Virtual Environment:

```bash
python3 -m venv bot_env
```

This will create a virtual environment called `bot_env`.

### Activate the Virtual Environment:

```bash
source bot_env/bin/activate
```

This will activate the virtual environment. You'll see the prompt change to indicate that you're inside the virtual environment.

### Install Required Python Libraries:

```bash
pip install python-telegram-bot requests
```

This will install the required libraries (`python-telegram-bot` and `requests`) inside your virtual environment.

### Create and Edit the Bot Script:

```bash
nano telegram_bot.py
```

Paste code from the file here.

### Run the Bot Script:

```bash
python3 telegram_bot.py
```

This will start the bot and make it ready to receive commands from users.


### Deactivate the Virtual Environment (optional):

After you finish using the bot, you can deactivate the virtual environment by running:

```bash
deactivate
```
