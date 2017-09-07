# -*- coding: utf-8 -*-

import os
import sys

def file2list(filepath):
    ret = []
    with open(filepath, 'r') as f:
        ret = [line.rstrip('\n') for line in f.readlines()]
    return ret

def list2file(filepath, ls):
    with open(filepath, 'w') as f:
        f.writelines(['%s\n' % line for line in ls] )

def file2str(filepath):
    ret = None
    with open(filepath, 'r') as f:
        ret = f.read()
    return ret

def str2file(filepath, rawstr):
    with open(filepath, 'w') as f:
        f.write(rawstr)

def terminalencoding2utf8(bytestr):
    return bytestr.decode(sys.stdin.encoding).encode('utf8')

def raise_option_error(msg, lineno, line):
    raise RuntimeError('{0} at line {1}, "{2}".'.format(msg, lineno, line))

def append_to_out(appendee_list, appender, use_ignore=False):
    if use_ignore:
        return
    appendee_list.append(appender)

def parse_arguments():
    import argparse

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument('-i', '--input', default=None, required=True,
        help='A input filename.')
    parser.add_argument('-o', '--output', default=None, required=True,
        help='A output filename.')
    parser.add_argument('-t', '--template', default=None, required=True,
        help='A template filename.')

    args = parser.parse_args()
    return args

args = parse_arguments()

MYDIR = os.path.abspath(os.path.dirname(__file__))
infile = os.path.join(MYDIR, args.input)
outfile = os.path.join(MYDIR, args.output)
templatefile = os.path.join(MYDIR, args.template)

# Fix body contents from source markdown.
# ---------------------------------------

lines = file2list(infile)
outlines = []
for i,line in enumerate(lines):
    # blank line
    if len(line)==0:
        continue

    # comment line
    #   ; comment
    #   <!-- comment -->
    #   // comment
    if line[0]==';' or line[0]=='<' or line[0]=='/':
        continue

    # section line
    if line[0]=='#':
        # '# 見出し名'
        #
        # '<h1>見出し名</h1>'
        sectionname = line[1:].strip()
        outline = '<h1>{:}</h1>'.format(sectionname)
        outlines.append(outline)
        continue

    # content line
    if line[0]=='-':
        # '- Title, URL Keywords...'
        #
        # '<li class="bookmark-entry"><a href="URL">Title</a> Keywords</li>'
        body = line[1:].strip()
        title, rest   = body.split(',', 1)

        # これしないと Title と URL の間のスペースが次の split 時にひっかかる.
        rest = rest.strip()

        if rest.find(' ')!=-1:
            url, keywords = rest.split(' ', 1)
        else:
            url = rest
            keywords = ''
        outline = '<li class="bookmark-entry"><a href="{:}">{:}</a> {:}</li>'.format(
            url, title, keywords
        )
        outlines.append(outline)
        continue

    if line[0]=='*':
        # '* Comment'
        #
        # <li>Comment</li>
        comment = line[1:].strip()
        outline = '<li>{:}</li>'.format(comment)
        outlines.append(outline)
        continue
outbody = '\n'.join(outlines)

# Merge fixed body to the template.
# ---------------------------------

template_content = file2str(templatefile)
merged_content = template_content.replace('{{body}}', outbody)

# Save.
# -----

str2file(outfile, merged_content)
