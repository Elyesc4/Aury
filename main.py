import os
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        filename = str(event.src_path).split('\\')[-1]
        for img_type in image_types:
            if img_type in filename:
                if '.crdownload' not in filename:
                    try:
                        if '-unsplash.jpg' in filename:
                            os.rename(event.src_path, unsplash_dir + "\\" + filename)
                            logger.info("    %s |-> Was moved to ->| %s", event.src_path, unsplash_dir)
                        else:
                            os.rename(event.src_path, image_dir + "\\" + filename)
                            logger.info("    %s |-> Was moved to ->| %s", event.src_path, image_dir)
                    except FileNotFoundError:
                        pass
                    except FileExistsError:
                        logger.error("   FileExistsError: %s ", event.src_path)
                        os.remove(event.src_path)
                        logger.info("    %s | Was deleted! |", event.src_path)


image_types = [".jpg", "jpeg", ".png"]
image_dir = "C:\\Users\\elyes\\OneDrive\\Bilder\\Saved Pictures"
unsplash_dir = image_dir + "\\Unsplash"
downloads_dir = 'C:\\Users\\elyes\\Downloads'

logg_file = 'C:\\Users\\elyes\\OneDrive\\Bilder\\Aury.log'
logger = logging.getLogger(__name__)
logging.basicConfig(filename=logg_file, level=logging.DEBUG)

if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=downloads_dir, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
