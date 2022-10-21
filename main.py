import pathlib
import shutil
import time
import os


def copy_func(src, dest):
    print('Copying ' + src.split('/')[-1])
    mp3 = dest.replace('.wav', '.mp3')
    os.system(f'sox "{src}" "{mp3}"')


def main():
    # you may need to change the sr0 value, depending on your hardware
    path = '/run/user/1000/gvfs/cdda:host=sr0'

    number = input('Enter CD #:')
    speaker = input('Enter speaker:')
    date = input('Enter date:')
    title = input('Enter title:')

    dest_path = f'/home/edwin/Music/SR/{number}-{date}-{speaker}-{title}'

    # wait till cd becomes available
    while True:
        time.sleep(0.5)
        if pathlib.Path(path).exists():
            break
        continue

    shutil.copytree(path, dest_path, copy_function=copy_func)


if __name__ == '__main__':
    main()
