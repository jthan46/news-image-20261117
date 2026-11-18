// Entrypoint for the 17 November 2026 news-image entry.
// It loads the artwork that sits next to this script, sanity-checks the
// payload, and then publishes those exact bytes under the name the
// grader expects inside whichever destination folder is configured.

import * as fs from "node:fs";
import * as path from "node:path";
import { fileURLToPath } from "node:url";

const MAX_ALLOWED_BYTES = 1048576;
const PNG_MAGIC = [0x89, 0x50, 0x4e, 0x47];
const JPEG_MAGIC = [0xff, 0xd8, 0xff];

function startsWithBytes(buffer, prefix) {
  if (buffer.length < prefix.length) {
    return false;
  }
  for (let index = 0; index < prefix.length; index += 1) {
    if (buffer[index] !== prefix[index]) {
      return false;
    }
  }
  return true;
}

function looksLikeSupportedImage(buffer) {
  return startsWithBytes(buffer, PNG_MAGIC) || startsWithBytes(buffer, JPEG_MAGIC);
}

const scriptFolder = path.dirname(fileURLToPath(import.meta.url));
const artworkPath = path.resolve(scriptFolder, "entry.png");

if (!fs.existsSync(artworkPath)) {
  throw new Error(`Cannot publish anything: no file found at ${artworkPath}`);
}

const artworkBytes = fs.readFileSync(artworkPath);

if (artworkBytes.length > MAX_ALLOWED_BYTES) {
  throw new Error(
    `Artwork is ${artworkBytes.length} bytes, which exceeds the ${MAX_ALLOWED_BYTES} byte limit`,
  );
}

if (!looksLikeSupportedImage(artworkBytes)) {
  throw new Error("Artwork header is neither PNG nor JPEG, so it will not be published");
}

const configuredDir = process.env.MAKEFUN_OUTPUT_DIR;
const destinationFolder = configuredDir ? path.resolve(configuredDir) : path.resolve("/output");
fs.mkdirSync(destinationFolder, { recursive: true });

const destinationPath = path.resolve(destinationFolder, "entry.png");
fs.writeFileSync(destinationPath, artworkBytes);

console.log(`Published ${artworkBytes.length} bytes to ${destinationPath}`);
