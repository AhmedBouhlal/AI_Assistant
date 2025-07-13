# ai_interface.py

import os
import requests
from assistant_config import OLLAMA_MODEL, OLLAMA_HOST


def call_ollama(prompt):
    """
    Calls local Ollama LLM API.
    Expects OLLAMA_HOST and OLLAMA_MODEL in assistant_config.py.
    """
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False
    }
    res = requests.post(OLLAMA_HOST, json=payload)
    res.raise_for_status()
    return res.json()["response"]