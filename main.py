import os
import logging

from watchFaceParser.config import Config


if __name__ == '__main__':
    import sys
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--vergelite', action='store_true', help='force VergeLite watchface')
    parser.add_argument('--gtr', type=int, choices=[42,47], help='force GTR watchface')
    parser.add_argument('--gtr2', type=int, choices=[42,47], help='force GTR watchface')
    parser.add_argument('--gts', action='store_true', help='force GTS watchface')
    parser.add_argument('--trex', action='store_true', help='force T-REX watchface')
    parser.add_argument('--x', action='store_true', help='force AmazfitX watchface')
    parser.add_argument('--file', nargs='+', help='''watchface.bin - unpacks watchface images and config
    watchface.json - packs config and referenced images to bin file''')
    args = parser.parse_args()

    Config.setVergeLiteMode(args.vergelite)
    Config.setGtrMode(args.gtr)
    Config.setGtrMode2(args.gtr2)
    Config.setGtsMode(args.gts)
    Config.setTrexMode(args.trex)
    Config.setAmazfitXMode(args.x)

    for inputFileName in args.file:
        isDirectory = os.path.isdir(inputFileName)
        isFile = os.path.isfile(inputFileName)
        if not isDirectory and not isFile:
            print("File or direcotry %s doesn't exist." % (inputFileName, ))
            continue
        if isDirectory:
            print("Not supported yet.")
            sys.exit(1)
        _, inputFileExtension = os.path.splitext(inputFileName)
        try:
            import program
            if inputFileExtension == '.bin':
                program.Parser.unpackWatchFace(inputFileName)
            elif inputFileExtension == '.json':
                program.Parser.packWatchFace(inputFileName)
            else:
                print("The app doesn't support file with extension %s." % (inputFileExtension, ))
            print("Done")
        except Exception as e:
            print('[Fatal] %s' % (e, ))
            import traceback
            traceback.print_stack()
            logging.exception(e)

