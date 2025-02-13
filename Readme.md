# **📥 YouTube Video Downloader for Tajziakaar**  

## **📌 Project Overview**  
This project automates the downloading of YouTube videos from a list of links provided in a text file. It utilizes the **pytube** and **youtube-dl** libraries to fetch and save videos in `.mp4` format. Additionally, it supports **login authentication** for private or restricted videos.  

This module is integrated as a separate **Django service**, allowing users to upload a text file containing YouTube links. The service then reads the file and downloads each video, saving them in the desired output folder.  

## **🚀 API Endpoint**  
The following API endpoint is available for downloading videos:  

```
 "http://127.0.0.0:<your-port>/api/download-videos/"
```

## 🔹 How to Use  
1. **Send a POST request** using **Postman** or **cURL** to the API endpoint.  
2. **Provide a text file** containing YouTube links.  
3. The response will include:  
   - 📂 The **path to the downloaded videos** on the file system.  
   - 📌 The **status of each link** (success or error).  

## 🛠 Environment Setup  
To run this service, use one of the following environments:  
- **`ocr_tf1`**  
- **`ocr-3.6`**  

⚠️ **Django Version Requirement:**  
Ensure **Django 4.2.2 or lower** is installed. Using a **higher version may cause compatibility issues**.  
