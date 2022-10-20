You will be able to run this script successfully using my step-by-step tutorial below.

* OC : Ubuntu (64-bit) on VirtualBox  (in my case)
* Python version: 3.10._ (in any case)

**Step one: preparing your workspace** 
The most convenient way to prepare the workspace is to create a virtual environment. If you never use virtual environment on your machine you can easily do it using this manual: <https://gist.github.com/frfahim/73c0fad6350332cef7a653bcd762f08d0332cef7a653bcd762f08d>
I did it with the commands below:
> sudo apt install -y python3-pip
> sudo apt install -y python3-venv
> mkdir myapp && cd myapp
> python3 -m venv env
> source env/bin/activate

Сongratulations, you have activated your virtual environment!

**Step two: clone my repository (to get the program file)** 

For this step you just need the link of this repository (in the command example it is -  https://github.com/rep/rep, but it is wrong, please, change it) and use this command:

> git clone https://github.com/rep/rep

Сongratulations, you have pain.py!

**Step three: installing the modules** 
On this step you can try run the program file with command :

> python3 pain.py

Probably, you will get an error telling you which modules you need to install in order to proceed. 

In my case I had to install the modules below


- google 
> pip install --upgrade google-api-python-client
- Kivy
> pip install Kivy
- bio
> pip install bio
- aiohttp
> pip install aiohttp
- pandas
> pip install pandas
- scipy
> pip install scipy
- scanpy
> pip install scanpy
- opencv-python
> pip install opencv-python
- bs4
> pip install bs4
- html5lib
> pip install html5lib
- lxml
>  Pip install lxml

In my case installation of this modules was enough for successful running of program python.py

If everything fine, you will see GUI window with writing "Ура, все работает!"

Congratulations!

P.S.
Please take a look at the requirements.txt file to check the list of all the required third-party python libraries to run this script. Don't be afraid if you have any other problems running it, I'm sure google has answers to any questions (or almost any):)
