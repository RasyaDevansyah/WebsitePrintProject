# WebsitePrintProject
 
## A website that automatically prints your documents
I was bored so I decided to make a website that automatically prints your documents.
I made this using visual studio code and the extenstions that helped me both port forward and run the php file.
You can hook this up to a laptop and to your printer without any database sevises or anything like that.

The design of this website is from Ravi Web you should check it out
https://youtu.be/SDJKsE_bv04?si=i7YecFsF-gFVF13L

## You will need
* Visual Studio code
* SumatraPDF
* Microsoft Word
* Python and PHP
## Instructions
1. Clone/Download the repository
  
2. Install python
   * Python should be on the microsoft store. Install it there. I used version 3.11 but other versions should be fine.
3. Install sumatraPDF
   * Install sumatraPDF here https://www.sumatrapdfreader.org/download-free-pdf-viewer.
4. Install php
   * Install The thread safe version zip file https://windows.php.net/download#php-8.3.
5. Unzip the php file
   * After you download the file, rename the file to make it readable then unzip the file and move it to Local disk C.
6. Edit the Environment Variables
   * Copy the folder path you just moved and then search environment variables in your search bar.
   * Click on Environment Variables, on system variables click on path, click new, than paste the folder path.
7. Install visual studio code.
   * You can install visual studio code here https://code.visualstudio.com/download.
8. Open visual studio and install the extension PHP server.
9. Find the file location of sumatraPDF.exe and copy the file location.
10. Go back to visual studio code open the cloned repository.
11. Open the file "Print.py" and paste the path to the variable sumatra_EXE_path (be sure to double up the back slash).
12. Open "upload.php", Right click and choose "PHP Server: Serve Project".
13. Then go to ports and forward the port 3000.


   
 
   
