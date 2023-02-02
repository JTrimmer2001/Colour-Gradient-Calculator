from Astropyfits import image_viewer
i=6

while i == 6:
    print("image to view: 1, table to read: 2")
    choice = input()

    if choice == 1:
        image_viewer()