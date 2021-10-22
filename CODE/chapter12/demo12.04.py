import os
if os.path.exists('data.txt') and not os.path.exists('slink.txt'):
    os.symlink('data.txt','slink.txt')
if os.path.exists('data.txt') and not os.path.exists('link.txt'):
    os.link('data.txt','link.txt')
