"""Verify data/presentation parity and optionally invoke the canonical renderer.

The exported reader is retained unchanged. No alternate dashboard UI is built.
"""
from pathlib import Path
import argparse
import base64
import gzip
import json
import re
import subprocess

ROOT=Path(__file__).resolve().parent


def embedded_payload(path):
    text=path.read_text(encoding='utf-8')
    match=re.search(r'<template id="data-analytics-portable-artifact-payload-source"[^>]*>(.*?)</template>',text,re.S)
    if not match:
        raise ValueError('Canonical presentation payload is missing')
    return json.loads(gzip.decompress(base64.b64decode(match.group(1))))


def verify(artifact_path=ROOT/'artifact.json',html_path=ROOT/'index.html'):
    source=json.loads(artifact_path.read_text(encoding='utf-8'))
    payload=embedded_payload(html_path)
    for key in ('manifest','snapshot','sources'):
        if source[key]!=payload[key]:
            raise ValueError(f'Stale HTML {key}: regenerate with the canonical renderer before publishing')
    return True


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--renderer',type=Path,help='Path to deliver_portable_artifact.mjs in the canonical authoring environment')
    args=parser.parse_args()
    if args.renderer:
        subprocess.run(['node',str(args.renderer),'--input',str(ROOT/'artifact.json'),
            '--output',str(ROOT/'index.html')],check=True)
    verify()
    print('Presentation manifest, dataset snapshot and source definitions match the generated artifact.')


if __name__=='__main__':main()
