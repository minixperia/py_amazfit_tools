from watchFaceParser.config import Config
if Config.isGtr2Mode() or Config.isGts2Mode():  
    from watchFaceParser.models.gtr2.elements.watchFace import WatchFace
else:
    from watchFaceParser.models.elements.watchFace import WatchFace

class PreviewGenerator:
    @staticmethod
    def createAnimation(descriptor, images, states):
        previewWatchFace = WatchFace(descriptor)
        for watchState in states:
            image = PreviewGenerator.createFrame(previewWatchFace, images, watchState)
            yield image


    @staticmethod
    def createImage(descriptor, images, state):
        previewWatchFace = WatchFace(descriptor)
        return PreviewGenerator.createFrame(previewWatchFace, images, state)


    @staticmethod
    def createFrame(watchFace, resources, state):
        from PIL import Image, ImageDraw

        graphics = Image.new('RGBA', Config.getImageSize())
        watchFace.draw3(graphics, resources, state)
        return graphics
