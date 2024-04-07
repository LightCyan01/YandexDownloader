
# Yandex Disk Downloader Tool

This is a fork of [@SecFathy](https://github.com/SecFathy/YandexDown)'s Yandex Disk Downloader Tool. It is a simple Python script that allows users to download files from Yandex Disk easily. With this tool, users can download both small and large files from Yandex Disk with ease. The tool takes in a Yandex Disk file link and a download location, and then downloads the specified file to the designated location.





## Installation

Installation Requirement 

```bash
  pip install requests
```
    
## Usage/Examples

### Downloading a Single File

1. Run the following command in your terminal:

```
python3 YandexCLI.py -l <yandex_link> -d <download_location>
```

2. Replace ```<yandex_link>``` with the link to the file you want to download from Yandex Disk, and ```<download_location>``` with the directory where you want to save the downloaded file.


3. Press Enter and wait for the download to complete.

### Downloading a Folder

1. Run the following command in your terminal:

```bash
python3 YandexCLI.py -l <yandex_disk_link> -d <download_location> -f <folder_path>
```

2. Replace ```<yandex_link>``` with the link to the file you want to download from Yandex Disk, including ```<download_location>``` with the directory where you want to save the downloaded file and ```-f <folder_path>``` with the path of folder that you want to download ex: ```"/<folder_name>"```.

3. Press Enter and wait for the download to complete.
