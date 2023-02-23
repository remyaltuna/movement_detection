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
1. Create a folder and title it “Work”
2. Within the folder make another folder titled “Python script”
3. Put the python code `main_improved.py` within the python script folder
4. Within python script make a folder called “Segmented Videos”
5. Download the sj_#### folders about 6 at a time into the segmented videos folder
6. Open `main_improved.py` in python and run the code provided
7. Let the program run
8. Once completed, it will upload all the data for the movement coding into a txt file called “results” within the python script folder
9. Open the results txt file and put the results into the movement coding google sheet for each sj ID
10. Empty the Work folder and download new sj_#### folder 
11. Repeat the process (the data will still be saved in the result txt file it will not erase every time you rerun the code)
