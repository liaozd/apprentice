#!/usr/bin/env python


def read_file_by_chunks(filename, chunksize=100):
    file_object = open(filename, 'rb')
    while True:
        chunk = file_object.read(chunksize)
        if not chunk:
            break
        yield chunk
    file_object.close()


for chunk in read_file_by_chunks("/tmp/config-err-ReeLBQ"):
    print chunk
