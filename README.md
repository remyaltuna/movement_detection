# Movement Detection
This script takes in the different clips for a subject and computes the magnitude of movement and time of movement.

Before clonin repository, you need a github account and authenticate it with an ssh key.
To generat an ssh key, from terminal:
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```
Use same email that you used to open github account.

Now we have to copy this ssh key into your github account.
1. Go to github account
2. Cick top right profile icon and then `settings` from the dropdown.
3. On the left hand side, click on `SSH and GPG keys` and the click on `New SSH Key`.
4. From terminal, type each commmand line by line:
   ```bash
   cd
   cd .ssh
   ls
   cat id_ed25519.pub
   ```
   This should print a line that look like this:
   ```bash
   ssh-ed25519 HFHDHDHFUSDGFGDFifdsuhbfiusdhfiUBSDfiusdhfudsbISUDBf+ "your@email.com"
   ```
   Copy paste this whole line into the github `SSH and GPG keys` website under `Key`. Also give this key a title like `Macbook` and leave key type as `Authentication key`. Click `Add SSH Key`
   
Navigate to where you want to store the repo
```bash
cd ~
```
Now you can clone this repository in your local machine. From terminal type:
```bash
git clone git@github.com:remyaltuna/movement_detection.git
```

## Setup
First check that you have python3 installed by running the following command:
```bash
python3 --version
```
You should get something like this:
```bash
Python 3.10.5
```
Haven't tested with any other version but it might work with lower version. If not, update it or install to version `3.10.9` from https://www.python.org/downloads/macos/

Before using this script, you must first set up a python environment. This allows us to have specific version of python
 packages that are needed for this script to run. The necessary packages are saved in `requirements.txt`. To 
create a new virtual environment, run the following commands in the terminal.

```bash
python3 -m pip install --upgrade pip
```
Navigate to the directory where you downloaded the repository
```bash
cd path/to/where/you/downloaded/repository

For example:
cd Documents/movement_detection
```
Next create virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```
You should see `(venv)` at the beginning of your terminal prompt. For example:
```bash
(venv) ~ %
```
Next, install packages from `requirements.txt`
```bash
pip install -r requirements.txt
```

If everything installs correctly, you should be good to run the script.


## Instructions
1. Inside the repository folder, create a new folder called `Segmented_Video` (MUST MATCH EXACTLY).
5. Download up to 6 subject folders (`sj_####`) into the `Segmented_Video` folder.
6. From terminal, go to repository folder. ex: `cd path/to/movement_detection`
7. Start virtual environment with `source venv/bin/activate`
8. Run script with `python3 main_improved.py`
7. Let the program run, it will take as long as the videos are. You should be able to see the video playing in a popup window.
8. Once completed, it will upload all the data for the movement coding into `results.txt` and `results.csv` within the `movement_detection` folder.
9. The movement start times for each clip get logged inside their respective folders as a txt file.
10. Once completed, delete the subject folders in `Segemented_Video` and download new sj_#### folders.
11. Repeat the process (the data will still be saved in the `result.txt` and `results.csv` files. It will not erase every time you rerun the code)
