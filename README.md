# blob-video-downloader
#### Windows application for download videos with blob url 

## Step 1:
  **Press F12** to find the `m38u` file in `Network` > `Fetch/XHR` and **Download** the file.

## Step 2:
  Open the `m38u` file and **Extract** all `ts` files saving into a `txt` file.
  Example:
  ```
  #EXTM3U
  #EXT-X-VERSION:
  #EXT-X-TARGETDURATION:
  #EXT-X-MEDIA-SEQUENCE:

  #EXTINF:,
  0.ts
  #EXTINF:,
  1.ts
  #EXTINF:,
  2.ts
  #EXTINF:,
  3.ts
  .
  .
  .
  #EXT-X-ENDLIST
  ```
  To
  ```
  0.ts
  1.ts
  2.ts
  3.ts
  .
  .
  .
  ```
  **Note: Remember to add the completed url in front of all `ts` file name.**

## Step 3:
  **Execute** `ts_downloader.py` to download all ts segments of the original video.
  
## Step 4:
  **Double click** to run the application `merge_ts.bat` to merge all ts segments into one ts video.
  Or
  **Save** the following windows command into `bat` file.
  ```
  copy /b *.ts new.ts
  ```
  **Note: The `bat` file and all all `ts` segments must be in the same path.**
  
