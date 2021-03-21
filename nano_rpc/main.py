#!/usr/bin/env python3

import json
import marko
import requests
import os

from bs4 import BeautifulSoup
from bs4.element import Comment


def get_spec(refresh=False):
    cache_file = os.path.join(os.path.expanduser("~"), ".nano-rpc-spec")
    if not os.path.exists(cache_file) or refresh:
        text = requests.get(
            "https://raw.githubusercontent.com/nanocurrency/nano-docs/master/docs/commands/rpc-protocol.md"
        ).text
        with open(cache_file, "w") as outfile:
            outfile.write(text)
    else:
        with open(cache_file, "r") as infile:
            text = infile.read()

    return text


def is_visible(element):
    if element.parent.name in [
        "style",
        "script",
        "head",
        "title",
        "meta",
        "[document]",
    ]:
        return False
    if isinstance(element, Comment):
        return False
    return True


def parse_spec(spec):
    markdown = marko.convert(spec)
    soup = BeautifulSoup(markdown, features="html.parser")
    # print(soup)
    code = [
        s.contents[0]
        for s in soup.findAll("code", {"class": "language-json"})
        if s.contents
    ]
    ret = []
    for c in code:
        try:
            j = json.loads(c)
            ret.append(j)
        except:
            pass
    ret = [r for r in ret if "action" in r]
    return ret


def run_command(args, commands, url=None):
    if not url:
        url = "http://localhost:7076"
    for command in commands:
        if args.action == command["action"]:
            request = {"action": args.action}
            for arg in command:
                if arg != "action":
                    request[arg] = getattr(args, arg)
            response = requests.post(url, json=request)
            return response.json()


def main():
    import argparse

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument(
        "-r",
        "--refresh",
        help="Refresh the local RPC spec document.",
        action="store_true",
    )
    parser.add_argument(
        "-u",
        "--url",
        help="The RPC URL to which requests will be sent.",
        default="http://localhost:7076",
    )
    partial_args, remaining_args = parser.parse_known_args()
    subparsers = parser.add_subparsers(dest="action", help="Nano RPC commands.")
    commands = parse_spec(get_spec(refresh=partial_args.refresh))

    for command in commands:
        args = [arg for arg in command.keys() if arg != "action"]
        new_command = subparsers.add_parser(command["action"])
        for arg in args:
            new_command.add_argument("--{}".format(arg))

    args = parser.parse_args(remaining_args)

    try:
        response = run_command(args, commands, url=partial_args.url)
        print(json.dumps(response, indent=4, sort_keys=True))
    except Exception as e:
        print("Command failed: {}".format(str(e)))


if __name__ == "__main__":
    main()
