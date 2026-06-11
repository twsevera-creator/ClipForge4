"""
ClipForge — TikTok Auto-Clipper
Deployed on Railway
"""

import os, json, uuid, threading, time, subprocess, re
from pathlib import Path
from flask import Flask, render_template, request, jsonify, Response, send_file

app = Flask(__name__)

BASE     = Path(__file__).parent
JOBS_DIR = BASE / "jobs"
JOBS_DIR.mkdir(exist_ok=True)

jobs = {}
