import gzip
import sys
import argparse
import shutil


class AbletonProject(object):
    def __init__(self, filename):
        self.filename = filename

    def _get_name_slice(self):
        '''
            Basically returns abc if filename is abc.als
        '''
        return self.filename[:self.filename.index('.')]

    def unpack(self):
        with gzip.open(self.filename, 'rb') as unzipped_file:
            content = unzipped_file.read()
            with open(f'{self._get_name_slice()}_unpacked.xml', 'wb') as f:
                f.write(content) # default encoding in als files is UTF-8

    def pack(self):
        with open(f'{self.filename}', 'rb') as f:
            with gzip.open(f'{self.filename[:self.filename.index("_")]}_packed.als', 'wb') as als_file:
                shutil.copyfileobj(f, als_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='asdf')
    parser.add_argument('filename', action='store', help='Your .als file')
    parser.add_argument('--unpack', action='store_true', dest="unpack", help='From .als to xml')
    parser.add_argument('--pack', action='store_true', dest="pack", help='From xml to .als')
    args = parser.parse_args()
    abl = AbletonProject(args.filename)
    if args.unpack:
        abl.unpack()
    elif args.pack:
        abl.pack()
