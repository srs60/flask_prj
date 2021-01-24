# Creation and Running Flask Demo Projects

### 1. Download `virtual box` from [Oracle virtualbox](https://www.virtualbox.org/wiki/Downloads)

- Windows: VirtualBox-6.1.4-136177-Win.exe or new
- Ubuntu:  sudo apt-get install virtualbox
    
If you want to install the latest VirtualBox version from the Oracle repositories, check [this](https://linuxize.com/post/how-to-install-virtualbox-on-ubuntu-18-04/) tutorial.

### 2. Download `vagrant` and Install file from [Vagrant](https://www.vagrantup.com/downloads.html)
- Windows: 64-bit vagrant_2.2.7_x86_64.msi or new
- Ubuntu: [Vagrant Download page](https://www.vagrantup.com/downloads.html) to see if a newer version is available

#### Start by updating the package list with:
- sudo apt update

#### Download the Vagrant package using the following curl command:
- curl -O https://releases.hashicorp.com/vagrant/2.2.6/vagrant_2.2.6_x86_64.deb

##### Once the .deb file is downloaded, install it by typing:
- sudo apt install ./vagrant_2.2.6_x86_64.deb

##### Verify Vagrant installation
To verify that the installation was successful, run the following command which prints the Vagrant version:
- vagrant --version

### 3. Create folder for projects
- mkdir API_Projects
- cd API_Projects

### 4. Install both files

---

### 5. To prepare for Flask projects you must run some commands

    mkdir myprj_src
    cd myprj_src
    //virtualenv -p python3 demoname_prj   // if you want to use virtualenv
    //source demoname_prj/bin/activate     // activate / deactivate
    // copy all files from zip folder to myprj_src folder

If you want to change to another project, you must change infront of synchro folder definitions in Vagrantfile

### 6. Folders on PC::myprj_src and folder in virtual box::myprj/src are totally synchronized. 

    You can edit files in PC::demoname_src and to use them in virtual box.

### 7. Run first vagrant command from command window

    vagrant init ubuntu/xenial64

### 8. After creation of virtual disk, vagrant create file Vagrantfile

	copy Vagrant_base file (both files are text) to Vagrantfile

### 9. Now run full inastallation of sftware packages on virtual box

	vagrant up

### 10. Go to virtual disk

    vagrant ssh

Now you are in virtual disk under Ubuntu OS and must use linux commands.

### 11. Create first flask application write a file:

    app.py

### 12. To run a flask server with app:

    python app.py

After that go to the browser and write:
    
    localhost:6050
        or
    localhost:6500/hello/John
            
To exit server use ctrl-C

### 13. After this application you can try other applications:

    python prjname.py

### 14. To exit virtual box use:

    exit
	
After that to stop virtual box use:
	
    vagrant halt
	
To run virtual box again or after some changes into Vagrantfile or apps:

    vagrant up
        or
    vagrant reload

### 15. The End
