# Rider Save Editor

> **Note**
>
> This has been tested to work for Version 2.00.1.00 of [Rider](https://play.google.com/store/apps/details?id=com.ketchapp.rider)
>
> Version naming for the app is different across Google Play and Apk sites such as APK pure.

> **Warning**
>
> Requires a rooted Android device
>
> I cannot promise that it will not break the functionality of the game.

# Info

An editor of save files for the Android game [Rider](https://play.google.com/store/apps/details?id=com.ketchapp.rider) developed by [Ketchapp games](http://www.ketchappgames.com/).

# Setup

### PC side

Install python ([3.11](https://www.python.org/downloads/release/python-3110/) tested).

[Clone the repoository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) ***OR*** [Download it](https://github.com/JKook-Plus/rider_save_editor/archive/refs/heads/main.zip)

Create a virtual environment (recommended)

`py -3.11 -m venv venv`

Open the virtual environment

__Windows__
`venv\Scripts\activate.bat`

Install requirements.txt

`pip install -r requirements.txt`

### Android side

> **Warning**
>
> THIS WILL NOT WORK IF YOUR DEVICE IS NOT ROOTED
> 
> [XDA Link on how to root your device](https://www.xda-developers.com/root/)

Install Rider

- [Google play](https://play.google.com/store/apps/details?id=com.ketchapp.rider) 
- or find an APK

Run the game at least once.

Enable USB debugging or if you know what you are doing wireless debugging (you will need to edit the code to get this to work)

# Usage

Run [main.py](../main.py)

# TODO

- Make it more user friendly
- Make it more usable
- Make it into an executable
