## IP Data Lookup with ipinfo API
![](ip-address.png)
> This simple script allows you to look up information about an IP address using the ipinfo.io API.<br>
![](https://camo.githubusercontent.com/0be573625a35ec48113c49cde118ecbe70d987fff3dcd02709b76278b06e095f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e253230332d3337373641423f7374796c653d666f722d7468652d6261646765266c6f676f3d707974686f6e266c6f676f436f6c6f723d7768697465)
![](https://camo.githubusercontent.com/004134ebde4d6264961ef9a74fa84d7faa71d9c9b7110b5c53a57dac1194cf8c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f526571756573742d3538343942453f7374796c653d666f722d7468652d6261646765266c6f676f3d707974686f6e266c6f676f436f6c6f723d7768697465)
> 
## How it works:

1. When you run the script, you need to provide an IP address.


2. The script will make a request to the **ipinfo API** to get detailed information about the IP.


3. The returned information will be saved in a JSON file. The file name will be the IP address followed by `_info.json`. For example, for IP `123456789`, the generated file will be ``123456789_info.json``
