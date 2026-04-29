# Vindows93 ISO Creation Script
import os
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
print("Getting Ubuntu Server 22.04...")
print("You need curl.")
os.system("curl -L -o ubuntu-server.iso https://releases.ubuntu.com/22.04/ubuntu-22.04.5-server-amd64.iso")
print("Installed ISO!")
print("Creating Cubic working directory...")
os.makedirs("v93",511,True)
print("Creating commands for you to run in Cubic...")
print("Run these commands one by one.")
print("""sudo apt-get update
sudo apt update
sudo apt install xinit xorg
sudo apt install lightdm i3
sudo apt install firefox
echo 'exec --no-startup-id firefox --kiosk https://v3.windows93.net' >> /etc/skel/.config/i3-plz-add-after-boot
""")
print("After you've done that, start the Cubic ISO creation process and Vindows93 should be good to go.")
print("After login, copy .config/i3-plz-add-after-boot's contents to the end of your .config/i3.")