#!python
import sys
import base64
import string
import urllib

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
  if query.startswith('what'):
    print knowledge(query)
  if query.startswith('where'):
    print maps(clean_question(query[5:]))
  if query.startswith('why') or query.startswith('when'):
    print search(query)
  if query.startswith('define'):
    print dictionary(query[7:].rstrip())
  if query.startswith('python'):
    print api_python(query)
  if query.startswith('make a sound'):
    print mrraa()
  return ''

def trigger(s):
  return s.lower().startswith('spaxe')

def knowledge(s):
  return "http://www.wolframalpha.com/input/?i={}".format(urllib.quote(s))

def maps(s):
  return "https://www.google.com/maps/search/{}".format(urllib.quote(s))

def search(s):
  return "https://duckduckgo.com/?q={}".format(urllib.quote(s))

def dictionary(s):
  return "http://dictionary.reference.com/browse/{}".format(urllib.quote(s))

def api_python(s):
  return help(s)

def mrraa():
  return 'Mrraa!'

if '__main__' in __name__:
  main(sys.argv[1])