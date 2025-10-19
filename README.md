# QR File Transfer Project
## Video Demo: 
#### https://www.youtube.com/watch?v=_zXLBtAMqsY
## Description:

This is my small project about a web application built with **Flask**.
It allows users to transfer the files from two different devices. If you use a phone, you can scan the QR code to access the website faster.

First, we need to access this URL: https://qr-tranfer-project.onrender.com/ (it has a typo, so you need to type "tranfer" on the URL instead of "transfer"!). 

In order to transfer the files, we need to create a room that is a place to store every file. For other devices to join that room, we just need to enter the URL or scan the QR code on the phone to access the website.

At first, I just built the website locally and didn't have the creating room feature. However, when I wanted to deploy it on Render, I realized that we could see others' files if I just stored every uploaded files in one folder. Therefore, I created that feature to create a different room for a different person.

After that, we just need to press or click on "Upload file" and then "Upload". If you refresh the website, you will see the file appear in the "Uploaded Files" section. Then, if you want to download, you just need to click or press on that file.

Notice: the room will be automatically deleted in 10 minutes in order to save the memory!!!

### How it works:
#### 1. Create a room
When you enter the website, you can create a new room. A unique room ID and corresponding QR code will be generated. This ensures that each users can have a private space to store their files.

#### 2. Join a room
On other devices, you can join the same room by entering the URL or scanning the QR code.

#### 3. Upload and Download files
Once connected to the same room, users can upload and download files just by clicking or taping in the filename.

#### 4. Automatic Deletion
To save the memory and enhance security. Every file will be deleted in 10 minutes. Therefore, make sure that you get the job done within 10 minutes.

### Technologies Used:
- Python
- Flask
- HTML, CSS, JS (Jinja templates)
- Render (for deployment)

### Challenges Faced:
During development, I encountered several challenges. One of the biggest issues was how to manage files from different users without mixing them up. At first, I saved all uploaded files in a single folder, which caused confusion and security problems. To solve that, I added the room system where each room has its own folder. Another challenge was testing the website on my phone using the local network. I learned how to find my local IP address and use it in Flask so my phone could connect to the app. Finally, deploying on Render also required some adjustments, such as handling static files correctly and making sure uploaded files were stored temporarily.

#### If you want you can run it locally by clone the repository: https://github.com/AnhTaiLe06/QR-Tranfer_Project. (you need to change the local_ip in the code into your network ip to run locally)
