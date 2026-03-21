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

      // flatten everything into /place/
      await fs.write("/place/" + file.name, text);
    }

    if (entry.kind === "directory") {
      // ignore directory structure entirely
      await readAll(entry);
    }
  }
}

function newCon() {
  fs.mount("/place", "indexeddb");
  pickFolder();
}

function refresh() {
  if (rootHandle) {
    readAll(rootHandle);
  }
}

newCon()
