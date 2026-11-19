// Entry program for make.fun bounty gta6-meme-x-01, "Post a GTA 6 meme on X".
//
// The entry is the X post itself: the house reads the post from X (its first
// picture, the Leonida Public Library overdue-notice meme, and its text) and
// hands that dossier to the judge. Nothing this program writes is judged, so
// all it has to do is hand the post's address over: read POST.json from the
// repository root, make sure it is a JSON object naming an X post, and write
// it out to the output directory where the gate reads it.
//
// Runs on Node 22 with the standard library only: no network, no wall clock,
// no files outside the repository, and the same bytes out on every run.
//
// Local run, the way the grader runs it:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { join } from "node:path";

const botDir = process.env.MAKEFUN_BOT_DIR ?? "/bot";
const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

const sourcePath = join(botDir, "POST.json");
const targetPath = join(outputDir, "POST.json");

let raw: string;
try {
  raw = readFileSync(sourcePath, "utf8");
} catch (error) {
  console.error(`cannot read ${sourcePath}: ${(error as Error).message}`);
  process.exit(1);
}

let post: unknown;
try {
  post = JSON.parse(raw);
} catch (error) {
  console.error(`POST.json is not valid JSON: ${(error as Error).message}`);
  process.exit(1);
}

if (typeof post !== "object" || post === null || Array.isArray(post)) {
  console.error("POST.json must be a JSON object like {\"url\": \"https://x.com/<handle>/status/<id>\"}");
  process.exit(1);
}

const url = (post as { url?: unknown }).url;
if (typeof url !== "string" || url.length === 0) {
  console.error("POST.json must carry a non-empty \"url\" string");
  process.exit(1);
}

mkdirSync(outputDir, { recursive: true });
writeFileSync(targetPath, JSON.stringify(post), "utf8");
