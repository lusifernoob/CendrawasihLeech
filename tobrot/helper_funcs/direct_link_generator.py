# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Helper Module containing various sites direct links generators. This module is copied and modified as per need
from https://github.com/AvinashReddy3108/PaperplaneExtended . I hereby take no credit of the following code other
than the modifications. See https://github.com/AvinashReddy3108/PaperplaneExtended/commits/master/userbot/modules/direct_links.py
for original authorship. """

import logging
import json
import math
import re
import urllib.parse
from os import popen
from random import choice
from urllib.parse import urlparse

import lk21
import requests
from bs4 import BeautifulSoup
from js2py import EvalJs
# from lk21.extractors.bypasser import Bypass
from base64 import standard_b64encode

from tobrot.helper_funcs.exceptions import DirectDownloadLinkException


def direct_link_generator(text_url: str):
    """ direct links generator """
    if not text_url:
        raise DirectDownloadLinkException("`No links found!`")
    elif 'zippyshare.com' in text_url:
        return zippy_share(text_url)
    elif 'yadi.sk' in text_url:
        return yandex_disk(text_url)
    elif 'cloud.mail.ru' in text_url:
        return cm_ru(text_url)
    elif 'mediafire.com' in text_url:
        return mediafire(text_url)
    elif 'osdn.net' in text_url:
        return osdn(text_url)
    elif 'github.com' in text_url:
        return github(text_url)
    elif 'mxplayer.in' in text_url:
       return mxplayer(text_url)
    elif 'racaty.net' in text_url:
        return racaty(text_url)
    elif 'letsupload.io' in text_url:
        return letsupload(text_url)
    elif 'hxfile.co' in text_url:
        return hxfile(text_url)
    elif 'layarkacaxxi.icu' in text_url:
        return fembed720(text_url)
    elif 'naniplay.nanime.in' in text_url:
        return naniplay(text_url)
    elif 'naniplay.nanime.biz' in text_url:
        return nanibiz(text_url)
    elif 'naniplay.com' in text_url:
        return nani(text_url)
    elif 'femax20.com' in text_url:
        return fembed(text_url)
    elif 'anonfiles.com' in text_url:
        return anon(text_url)
    elif 'sbembed.com' in text_url:
        return sbembed(text_url)
    elif 'streamsb.net' in text_url:
        return streamsb(text_url)
    elif 'fembed.com' in text_url:
        return fembed(text_url)
    elif '1drv.ms' in text_url:
        return onedrive(text_url)
    else:
        raise DirectDownloadLinkException(f'No Direct link function found for {text_url}')

def letsupload(url: str) -> str:
    dl_url = ''
    try:
        text_url = re.findall(r'\bhttps?://.*letsupload\.io\S+', url)[0]
    except IndexError:
        raise DirectDownloadLinkException("`No Letsupload links found`\n")
    bypasser = lk21.Bypass()
    dl_url=bypasser.bypass_url(text_url)
    return dl_url

def hxfile(url: str) -> str:
    dl_url = ''
    try:
        text_url = re.findall(r'\bhttps?://.*hxfile\.co\S+', url)[0]
    except IndexError:
        raise DirectDownloadLinkException("`No HXFile links found`\n")
    bypasser = lk21.Bypass()
    dl_url=bypasser.bypass_url(text_url)
    return dl_url

def anon(url: str) -> str:
    dl_url = ''
    try:
        text_url = re.findall(r'\bhttps?://.*anonfiles\.com\S+', url)[0]
    except IndexError:
        raise DirectDownloadLinkException("`No anonfiles links found`\n")
    bypasser = lk21.Bypass()
    dl_url=bypasser.bypass_url(text_url)
    return dl_url

    ### Update by manssizz@CendrawasihLeech ###
### https://github.com/Manssizz/CendrawasihLeech/ ###
def fembed720(url: str) -> str:
    dl_url = ''
    try:
        text_url = re.findall(r'\bhttps?://.*layarkacaxxi\.icu\S+', url)[0]
    except IndexError:
        raise DirectDownloadLinkException("`No Fembed links found`\n")
    bypasser = lk21.Bypass()
    dl_url=bypasser.bypass_url(text_url)
    return dl_url["720p/mp4"]

def nani(url: str) -> str:
    dl_url = ''
    try:
        text_url = re.findall(r'\bhttps?://.*naniplay\.com\S+', url)[0]
    except IndexError:
        raise DirectDownloadLinkException("`No Fembed links found`\n")
    bypasser = lk21.Bypass()
    dl_url=bypasser.bypass_url(text_url)
    return dl_url

def naniplay(url: str) -> str:
    dl_url = ''
    try:
        text_url = re.findall(r'\bhttps?://.*naniplay\.in\S+', url)[0]
    except IndexError:
        raise DirectDownloadLinkException("`No Fembed links found`\n")
    bypasser = lk21.Bypass()
    dl_url=bypasser.bypass_url(text_url)
    return dl_url

def nanibiz(url: str) -> str:
    dl_url = ''
    try:
        text_url = re.findall(r'\bhttps?://.*naniplay\.biz\S+', url)[0]
    except IndexError:
        raise DirectDownloadLinkException("`No Fembed links found`\n")
    bypasser = lk21.Bypass()
    dl_url=bypasser.bypass_url(text_url)
    return dl_url

def streamsb(url: str) -> str:
    dl_url = ''
    try:
        text_url = re.findall(r'\bhttps?://.*streamsb\.net\S+', url)[0]
    except IndexError:
        raise DirectDownloadLinkException("`No streamsb links found`\n")
    bypasser = lk21.Bypass()
    dl_url=bypasser.bypass_sbembed(text_url)
    lst_link = []
    count = len(dl_url)
    for i in dl_url:
        lst_link.append(dl_url[i])
    return lst_link[count-1]    

def sbembed(url: str) -> str:
    dl_url = ''
    try:
        text_url = re.findall(r'\bhttps?://.*sbembed\.com\S+', url)[0]
    except IndexError:
        raise DirectDownloadLinkException("`No sbembed links found`\n")
    bypasser = lk21.Bypass()
    dl_url=bypasser.bypass_sbembed(text_url)
    lst_link = []
    count = len(dl_url)
    for i in dl_url:
        lst_link.append(dl_url[i])
    return lst_link[count-1]    

def streamsb(url: str) -> str:
    dl_url = ''
    try:
        text_url = re.findall(r'\bhttps?://.*streamsb\.net\S+', url)[0]
    except IndexError:
        raise DirectDownloadLinkException("`No streamsb links found`\n")
    bypasser = lk21.Bypass()
    dl_url=bypasser.bypass_sbembed(text_url)
    lst_link = []
    count = len(dl_url)
    for i in dl_url:
        lst_link.append(dl_url[i])
    return lst_link[count-1]    

def fembed(url: str) -> str:
    dl_url = ''
    try:
        text_url = re.findall(r'\bhttps?://.*fembed\.com\S+', url)[0]
    except IndexError:
        raise DirectDownloadLinkException("`No Fembed links found`\n")
    bypasser = lk21.Bypass()
    dl_url=bypasser.bypass_url(text_url)
    return dl_url

def onedrive(url: str) -> str:
    """ Onedrive direct link generator
    Based on https://github.com/UsergeTeam/Userge """
    dl_url = ''
    try:
        text_url = re.findall(r'\bhttps?://.*1drv\.ms\S+', url)[0]
    except IndexError:
        raise DirectDownloadLinkException("`No OneDrive links found`\n")
    link_without_query = urlparse(text_url)._replace(query=None).geturl()
    direct_link_encoded = str(standard_b64encode(bytes(link_without_query, "utf-8")), "utf-8")
    direct_link1 = f"https://api.onedrive.com/v1.0/shares/u!{direct_link_encoded}/root/content"
    resp = requests.head(direct_link1)
    if resp.status_code != 302:
        return "`Error: Unauthorized link, the link may be private`"
    dl_link = resp.next.url
    file_name = dl_link.rsplit("/", 1)[1]
    resp2 = requests.head(dl_link)
    return dl_link

######## [END] ########

def zippy_share(url: str) -> str:
    link = re.findall("https:/.(.*?).zippyshare", url)[0]
    response_content = (requests.get(url)).content
    bs_obj = BeautifulSoup(response_content, "lxml")

    try:
        js_script = bs_obj.find("div", {"class": "center",}).find_all(
            "script"
        )[1]
    except:
        js_script = bs_obj.find("div", {"class": "right",}).find_all(
            "script"
        )[0]

    js_content = re.findall(r'\.href.=."/(.*?)";', str(js_script))
    js_content = 'var x = "/' + js_content[0] + '"'

    evaljs = EvalJs()
    setattr(evaljs, "x", None)
    evaljs.execute(js_content)
    js_content = getattr(evaljs, "x")

    return f"https://{link}.zippyshare.com{js_content}"


def yandex_disk(url: str) -> str:
    """ Yandex.Disk direct links generator
    Based on https://github.com/wldhx/yadisk-direct"""
    try:
        text_url = re.findall(r'\bhttps?://.*yadi\.sk\S+', url)[0]
    except IndexError:
        reply = "`No Yandex.Disk links found`\n"
        return reply
    api = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?public_key={}'
    try:
        dl_url = requests.get(api.format(text_url)).json()['href']
        return dl_url
    except KeyError:
        raise DirectDownloadLinkException("`Error: File not found / Download limit reached`\n")


def cm_ru(url: str) -> str:
    """ cloud.mail.ru direct links generator
    Using https://github.com/JrMasterModelBuilder/cmrudl.py"""
    reply = ''
    try:
        text_url = re.findall(r'\bhttps?://.*cloud\.mail\.ru\S+', url)[0]
    except IndexError:
        raise DirectDownloadLinkException("`No cloud.mail.ru links found`\n")
    command = f'vendor/cmrudl.py/cmrudl -s {text_url}'
    result = popen(command).read()
    result = result.splitlines()[-1]
    try:
        data = json.loads(result)
    except json.decoder.JSONDecodeError:
        raise DirectDownloadLinkException("`Error: Can't extract the link`\n")
    dl_url = data['download']
    return dl_url


def mediafire(url: str) -> str:
    """ MediaFire direct links generator """
    try:
        text_url = re.findall(r'\bhttps?://.*mediafire\.com\S+', url)[0]
    except IndexError:
        raise DirectDownloadLinkException("`No MediaFire links found`\n")
    page = BeautifulSoup(requests.get(text_url).content, 'lxml')
    info = page.find('a', {'aria-label': 'Download file'})
    dl_url = info.get('href')
    return dl_url


def osdn(url: str) -> str:
    """ OSDN direct links generator """
    osdn_link = 'https://osdn.net'
    try:
        text_url = re.findall(r'\bhttps?://.*osdn\.net\S+', url)[0]
    except IndexError:
        raise DirectDownloadLinkException("`No OSDN links found`\n")
    page = BeautifulSoup(
        requests.get(text_url, allow_redirects=True).content, 'lxml')
    info = page.find('a', {'class': 'mirror_link'})
    text_url = urllib.parse.unquote(osdn_link + info['href'])
    mirrors = page.find('form', {'id': 'mirror-select-form'}).findAll('tr')
    urls = []
    for data in mirrors[1:]:
        mirror = data.find('input')['value']
        urls.append(re.sub(r'm=(.*)&f', f'm={mirror}&f', text_url))
    return urls[0]


def github(url: str) -> str:
    """ GitHub direct links generator """
    try:
        text_url = re.findall(r'\bhttps?://.*github\.com.*releases\S+', url)[0]
    except IndexError:
        raise DirectDownloadLinkException("`No GitHub Releases links found`\n")
    download = requests.get(text_url, stream=True, allow_redirects=False)
    try:
        dl_url = download.headers["location"]
        return dl_url
    except KeyError:
        raise DirectDownloadLinkException("`Error: Can't extract the link`\n")

def mxplayer(url: str) -> str:
    """ mxplayer direct links generator """
    try:
        text_url = re.findall(r'\bhttps?://.*mxplayer\.in\S+', url)[0]
    except IndexError:
        raise DirectDownloadLinkException("`No mxplayer links found`\n")
    page = BeautifulSoup(requests.get(text_url).content, 'lxml')
    info = page.find('a', {'aria-label': 'Download file'})
    dl_url = info.get('href')
    return dl_url

def racaty(url: str) -> str:
    dl_url = ''
    try:
        text_url = re.findall(r'\bhttps?://.*racaty\.net\S+', url)[0]
    except IndexError:
        raise DirectDownloadLinkException("`No Racaty links found`\n")
    reqs=requests.get(text_url)
    bss=BeautifulSoup(reqs.text,'html.parser')
    op=bss.find('input',{'name':'op'})['value']
    id=bss.find('input',{'name':'id'})['value']
    rep=requests.post(text_url,data={'op':op,'id':id})
    bss2=BeautifulSoup(rep.text,'html.parser')
    dl_url=bss2.find('a',{'id':'uniqueExpirylink'})['href']
    return dl_url

def useragent():
    """
    useragent random setter
    """
    useragents = BeautifulSoup(
        requests.get(
            'https://developers.whatismybrowser.com/'
            'useragents/explore/operating_system_name/android/').content,
        'lxml').findAll('td', {'class': 'useragent'})
    user_agent = choice(useragents)
    return user_agent.text
