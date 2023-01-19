# Copyright (C) 2020 Michael Farber Brodsky
import os
import sys

print("This software comes with no warranty, if it breaks your computer, it's your fault.")
print("However, you can just read the source code, it's really simple.")
# Make sure this is Ubuntu
try:
    with open("/etc/os-release", "r") as release_file:
        if not ('ID=ubuntu\n' in release_file.readlines()) and not ('ID=debian\n' in release_file.readlines()):
            sys.exit("This is not Ubuntu.")
except:
    sys.exit("This is not Ubuntu.")

# Install LyX and texlive
os.system("sudo apt install texlive texlive-lang-other texlive-font-utils lyx")
# Install culmus-latex the right way, since the deb is not good.
os.system("cd culmus-latex-0.7-r1 && sudo make CULMUSDIR=/usr/share/fonts/X11/Type1/ TEXMFDIR=/usr/share/texmf/ && sudo make install CULMUSDIR=/usr/share/fonts/X11/Type1/ TEXMFDIR=/usr/share/texmf/")
# Copy lyx-options to ~/.lyx
os.system("rm -r ~/.lyx && cp -r lyx-options ~/.lyx")

