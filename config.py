#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


import os

class Config(object):

    # Get a bot token from botfather
    BOT_TOKEN = os.environ.get("1813097267:AAFHYgxTfG2IHIj4OQTmXzI6_G_A12yXfKE", "")


    # Get from my.telegram.org (or @UseTGXBot)
    APP_ID = int(os.environ.get("5564160", ""))
    API_HASH = os.environ.get("2b5560d15e0f9083939429add4d5b817", "")


    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("1601731267", "").split())
    
