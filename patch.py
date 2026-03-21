# Vindows93's Windows93 Patcher
import os, requests, tarfile
#import json
import os
#import asyncio
#import aiohttp
from urllib.parse import urlparse

print("Now starting Vindows93 creation...")
#print("Not grabbing Windows93 via its HAR...")
#HAR_FILE = "v0.windows93.net.har"
#OUT = "mirror"
#CONNECTIONS = 512  # insane speed
#timeout = aiohttp.ClientTimeout(total=10)

# Load HAR
#with open(HAR_FILE, "r", encoding="utf-8") as f:
#    har = json.load(f)

#urls = {entry["request"]["url"] for entry in har["log"]["entries"] if "windows93" in entry["request"]["url"]}
#print(f"Found {len(urls)} URLs")

#async def fetch(session, url):
#    try:
#        async with session.get(url,timeout=timeout) as resp:
#            if resp.status != 200:
#                return f"SKIP {url} ({resp.status})"
#
#            data = await resp.read()
#
#            path = urlparse(url).path
#            if path.endswith("/"):
#                path += "index.html"
#
#            local_path = os.path.join(OUT, path.lstrip("/"))
#            os.makedirs(os.path.dirname(local_path), exist_ok=True)
#
#            with open(local_path, "wb") as f:
#                f.write(data)
#
#            return f"OK   {url}"
#    except Exception as e:
#        return f"ERR  {url} ({e})"
#
#async def main():
#    connector = aiohttp.TCPConnector(limit=CONNECTIONS)
#    timeout = aiohttp.ClientTimeout(total=None)

#    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
#        tasks = [fetch(session, url) for url in urls]
#        for future in asyncio.as_completed(tasks):
#            print(await future)

#asyncio.run(main())

print("Patching Windows93... (Not, because patching doesn't work)")
with open("patchStuff") as f:
    username = f.read().split(";")
    doHost = username[1]
    username = username[0]
with open("patchMe.html","w") as f:
    #f.write(
    string = """<!DOCTYPE html>
<html>
<head>
  <style>
    html, body {
      margin: 0;
      padding: 0;
      overflow: hidden;
      background: black;
    }
    iframe {
      width: 100vw;
      height: 100vh;
      border: none;
    }
  </style>
</head>
<body>

<iframe id="v93" src="https://v3.windows93.net"></iframe>

<script>
const frame = document.getElementById("v93");

frame.onload = () => {
    const win = frame.contentWindow;

    // Inject your patch code directly into Windows93
    win.eval(`
        import { fs } from "/42/api/fs.js";

        fs.write("/c/users/windows93/Connect to The Real World.js", \`
            import { fs } from "/42/api/fs.js";

            let rootHandle = null;

            async function pickFolder() {
              rootHandle = await window.showDirectoryPicker();
              await readAll(rootHandle);
            }

            async function readAll(handle) {
              for await (const entry of handle.values()) {

                if (entry.kind === "file") {
                  const file = await entry.getFile();
                  const text = await file.text();
                  await fs.write("/place/" + file.name, text);
                }

                if (entry.kind === "directory") {
                  await readAll(entry);
                }
              }
            }

            function newCon() {
              fs.mount("/place", "indexeddb");
              pickFolder();
            }

            newCon();
        \`);

        fs.write("/c/users/windows93/Refresh connection with The Real World.js", \`
            import { fs } from "/42/api/fs.js";

            let rootHandle = null;

            async function pickFolder() {
              rootHandle = await window.showDirectoryPicker();
              await readAll(rootHandle);
            }

            async function readAll(handle) {
              for await (const entry of handle.values()) {

                if (entry.kind === "file") {
                  const file = await entry.getFile();
                  const text = await file.text();
                  await fs.write("/place/" + file.name, text);
                }

                if (entry.kind === "directory") {
                  await readAll(entry);
                }
              }
            }

            function refresh() {
              if (rootHandle) {
                readAll(rootHandle);
              }
            }

            refresh();
        \`);

        fs.move("/c/users/windows93/", "/c/users/"""+username+""");
    `);

    console.log("Vindows93 patches injected");
};
</script>

</body>
</html>
"""
    #f.write(string)
print("Getting Tiny Core Linux...")
tcl = requests.get("http://tinycorelinux.net/17.x/x86/release/TinyCore-current.iso")
if tcl.ok:
    print("TCL is ok")
    with open("tiny.iso","wb") as f:
        f.write(tcl.content)
else:
    print("Abort abort, TCL is a goner")
    exit(1)
print("Modifying rootfs to have Windows93...")
input("Press Enter when you have mounted the ISO.")
drv = input("Which drive is it? (Ex. /dev/usb0/ or D:\\) Please format properly so disk does not hate me ")
print("Unzipping rootfs...")
with tarfile.open(f"{os.path.realpath(drv)}/boot/core.gz", 'r:gz') as tar_ref:
    tar_ref.extractall(f"{os.path.realpath(drv)}/boot/CORE") # Specify the output directory
print("Using Misalf's script from a forum to put firefox installer in home directory...")
with open(f"{os.path.realpath(drv)}/boot/CORE/home/firefoxInstall.sh") as f:
    f.write('''#!/bin/sh
## Author: Misalf
## v 0.1
## Jun-6-2014

echo -e "\033]0;Wget...\007"

#. /etc/init.d/tc-functions
#useBusybox

trap 'echo -e "\033]0;$\007" ; line="=" ; f_line ; trap 2 ; kill -2 $$' 1 2 3 13 15

##******************************************************************************************************************
##***************************************************Functions******************************************************
## coreplayer2

## Draws a line at full screen-width  ( use xy=(line#) for row position ;   linecolor=([0]-[7]) linebold=([0]-[7]) ;  line=([char]) )
f_line() {
wide=`stty size | cut -d" " -f2`
#printf "\033[3;0H"
echo -ne "\033[0${linebold};3${linecolor}m "
printf '%*s\n' "$(( wide-2 ))" '' | tr ' ' $line
printf "\033[00m"
}

## Check Connection / URL
f_chkconn () {
echo -ne "\033[00;35m Using\033[01;30m: \033[00;32m${WGET} \033[01;30m::"
echo -e "\033[00;35m URL\033[01;30m: \033[00;36m${URL}"

line="-"
f_line

echo -ne "\033[00;36m Testing connection to server\033[01;30m... \033[00m"
${WGET} -s -T 20 "${URL}" 2>/dev/null &
rotdash $!
case $? in
	0) echo -e "\033[00;32mOK \033[00m"; cx=0;;
	1) echo -e "\033[00;31mFail\033[00;33m!\033[00m"; cx=1; f_line; exit 1;;
esac
}
##******************************************************************************************************************
##******************************************************************************************************************

f_resolve_url() {
url=$1
domain=`echo $url | sed 's-^[^/]*/*\([^/]*\)/\?.*$-\1-'`
ipaddr=`ping -c 1 $domain | sed -n 's@^.*(\([0-9]*\.[0-9]*\.[0-9]*\.[0-9]*\).*$@\1@p' | head -1`
req_url=`echo $url | sed "s-/[^/]\+-/$ipaddr-"`
wget $req_url
}

##******************************************************************************************************************

#WGET="$(which wget)"
WGET="$(which busybox) wget"

if [ -z "$1" ]; then
	echo -e "\033[00;31m No download specified\033[01;30m."
	echo -e "\033[00;33m Exiting\033[01;30m..."
	sleep 3
	exit 1
else
	if [ -z "$2" ]; then
		DIR="."
		URL="$1"
	else
		DIR="$1"
		if [ ! -d "${DIR}" ]; then
			echo -e "\033[00;31m Directory does not exist\033[01;30m:"
			echo -e "\033[01;34m ${DIR}/"
			echo -e "\033[00;33m Exiting\033[01;30m..."
			sleep 3
			exit 1
		fi
		URL="$2"
	fi
fi

linebold=1
linecolor=0
line="="
f_line

f_chkconn

echo -e "\033[00;35m Downloading to\033[01;30m:"
echo -e "\033[00;34m ${DIR}/\033[00;33m${URL##*/}"
line="-"
f_line

if [ -f ${DIR}/${URL##*/} ]; then
	echo -e "\033[00;35m Continuing download\033[01;30m..."
else
	echo -e "\033[00;35m Starting download\033[01;30m..."
fi

##******************************************************************************************************************

echo -ne "\033]0;Wget: ${URL##*/}\007"

RETRYNUM=0
while true; do
	RETRYNUM=$((RETRYNUM+1))
	###xterm -title "Wget: ${URL}" -e $(which busybox) wget -P ${DIR} -c ${URL}
	echo -ne "\033[00;32m"
	#${WGET} -P ${DIR} -c ${URL} && (echo -e "\n\033[00;33m DONE.") ; break || (echo -e "\033[00;31mERROR\033[01;30m = \033[00;33m$?\n\n\033[00;35mRetrying...\033[00m" ; sleep 2)
	${WGET} -P ${DIR} -c ${URL}
	EL=$?
	case $EL in
		0)
			echo -e "\n\033[00;33m DONE. Press any key to exit."
			line="="
			f_line
			break
			;;
		*)
			echo -e "\033[00;31m ERROR\033[01;30m = \033[00;33m${EL}"
			linebold=0
			linecolor=1
			line="-"
			f_line
			linebold=1
			linecolor=0
			echo -ne "\033[00;35m Waiting 5 seconds\033[01;30m... \033[00;33m"
			sleep 5 &
			rotdash $!
			echo -e "\033[00;35mRetrying\033[01;30m (\033[00;35m#${RETRYNUM}\033[01;30m)\033[00m"
			;;
	esac
done

read junk

echo -e "\033[00m"''')
print("Making it executable...")
os.system(f"chmod +x {os.path.realpath(drv)}/boot/CORE/home/firefoxInstall.sh")
print("Placing autoFox script and init-adding it...")
with open(f"{os.path.realpath(drv)}/boot/CORE/home/autoFox.sh") as f:
    f.write("""#!/bin/bash
firefox --kiosk https://windows93.net""")
with open(f"{os.path.realpath(drv)}/boot/CORE/init", "a") as f:
    f.truncate(18)
    f.write("""exec /home/autoFox.sh
exec /sbin/init""")
print("Making it executable...")
os.system(f"chmod +x {os.path.realpath(drv)}/boot/CORE/home/autoFox.sh")
os.system(f"chmod +x {os.path.realpath(drv)}/boot/CORE/init")
print("Rezipping core.gz...")
with tarfile.open(f"{os.path.realpath(drv)}/boot/core.gz", "w:gz") as tar:
    tar.add(f"{os.path.realpath(drv)}/boot/CORE/", arcname=os.path.basename(f"{os.path.realpath(drv)}/boot/CORE/"))
print("Vindows93 setup complete.")
