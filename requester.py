import unittest
import httpx
import re


class Requester:
    def request(self, url: str):
        print(f'request: {url}')
        return httpx.get(url).text

    def template(self, string_with_template: str, replacements: dict) -> str:
        print('string_with_template', string_with_template, 'replacements', replacements)
        def replace_placeholder(match):
            placeholder = match.group(1)
            key, _, default_value = placeholder.partition(" ")
            print(f'template {default_value}')
            return replacements.get(key, default_value)

        return re.sub(
            r"{([\w=&%-^$#!?/:. ]+)}", replace_placeholder, string_with_template
        )

class TestAddFunction(unittest.TestCase):
    def test_template(self):
        requester = Requester()
        replacements = {'url': 'jnkjk'}
        result = requester.template('https://github.com/{url}', replacements)
        print(result)
        self.assertEqual(result, 'https://github.com/jnkjk')

    def test_template_2(self):
        requester = Requester()
        replacements = {'url': 'jnkjk', 'page': '1'}
        result = requester.template('https://github.com/{url}/{page}', replacements)
        print(result)
        self.assertEqual(result, 'https://github.com/jnkjk/1')