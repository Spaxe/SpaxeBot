#!python
"""Super hacky for now."""

import sys
import time
import base64
import string
import urllib
import urllib2
from bs4 import BeautifulSoup

def lstrip2(s):
  return s.lstrip(string.punctuation+string.whitespace)

def clean_question(s):
  s = lstrip2(s)
  tests = ['\'s', '\'re', 'is', 'are']
  for t in tests:
    if s.startswith(t):
      s = s[len(t):]
      break
  return lstrip2(s)

def main(cmds):
  cmd = base64.b64decode(cmds)
  if not trigger(cmd):
    return

  query = lstrip2(cmd[5:]).rstrip()
  if query.startswith('how old are you'):
    print about()
  if query.startswith('what'):
    print knowledge(query)
  if query.startswith('where'):
    print maps(clean_question(query[5:]))
  if query.startswith('why') or query.startswith('when'):
    print search(query)
  if query.startswith('define'):
    print dictionary(query[7:].rstrip())
  if query.startswith('python'):
    print search(query[7:].lstrip() + " site:docs.python.org")
  if query.startswith('look up python'):
    print search(query[14:].lstrip() + " site:docs.python.org")
  if query.startswith('processing'):
    print search(query[11:].lstrip() + " site:processing.org")
  if query.startswith('look up processing'):
    print search(query[18:].lstrip() + " site:processing.org")
  if query.startswith('look up'):
    print search(query[7:].strip())
  if query.startswith('make a sound'):
    print mrraa()
  return ''

def trigger(s):
  return s.lower().startswith('spaxe')

def knowledge(s):
  return "http://www.wolframalpha.com/input/?i={}".format(urllib.quote(s))

def maps(s):
  return "https://www.google.com/maps/search/{}".format(urllib.quote(s))

def dictionary(s):
  return "http://dictionary.reference.com/browse/{}".format(urllib.quote(s))

def api_python(s):
  help(s)

def search(s):
  html = urllib2.urlopen('https://duckduckgo.com/html/?q={}'.format(urllib.quote(s))).read()
  # return result
  soup = BeautifulSoup(html)
  results = []
  for s in soup.select('div.web-result'):
    results.append(s)
  # return soup
  for result in results:
    if 'web-result-sponsored' in result['class']:
      continue
    return result.text.strip()


def mrraa():
  return 'Mrraa!'

def about():
  return 'This clone of Spaxe was created on 11 December, 2014 at approximately 1pm.'

if '__main__' in __name__:
  main(sys.argv[1])