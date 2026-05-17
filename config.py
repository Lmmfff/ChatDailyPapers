# encoding: utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os

def _split_env_list(name, default=""):
    raw = os.getenv(name, default)
    return [item.strip() for item in raw.split(",") if item.strip()]


# Authentication for user filing issue.
USERNAME = os.getenv("GITHUB_USERNAME", "Lmmfff")
TOKEN = os.getenv("GITHUB_TOKEN","")

# The repository to add this issue to.
REPO_OWNER = os.getenv("REPO_OWNER", "Lmmfff")
REPO_NAME = os.getenv("REPO_NAME", "ChatDailyPapers")


# Set new submission url of subject.
NEW_SUB_URL = os.getenv("NEW_SUB_URL", "https://arxiv.org/list/cs/new")

# Keywords to search.
KEYWORD_LIST = _split_env_list("KEYWORD_LIST", "Biomedical Knowledge Graphs")

# LLM provider settings.
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "deepseek").lower()
LLM_MODEL = os.getenv("LLM_MODEL", "deepseek-chat")

LLM_API_BASE = os.getenv("LLM_API_BASE", "https://api.deepseek.com")

# Backward-compatible key list name used by the current code.
OPENAI_API_KEYS = _split_env_list("LLM_API_KEYS","")

LANGUAGE = os.getenv("LANGUAGE", "zh")  # zh | en
FILTER_TIME_SPAN_DAYS = float(os.getenv("FILTER_TIME_SPAN_DAYS", "3"))



# $env:GITHUB_TOKEN="你的本地token"
# $env:LLM_PROVIDER="deepseek"
# $env:LLM_MODEL="deepseek-chat"
# $env:LLM_API_KEYS="你的deepseek key"
# python main.py --filter_times_span 7