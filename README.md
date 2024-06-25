# Holomat-Homography

This is simply a homography showcase and a tutorial for users who are trying to follow Concept-Bytes' Holomat tutorial and cannot figure out how to warp an image using a Charuco board.

I have a cheap projector so I could not get Charuco boards to work due to the low resolution, so I looked into a computer vision technique called Homography.

This method actually seems to be a lot simpler than using Charuco boards, because you don't have to go through the effort of taking multiple screenshots of a Charuco board on your desk and then calibrating it.

# How to use
Simply add an image into the same directory as homography.py and name is "unwarpedImage.jpg". Once you run the code you must drag a box into each of the separate corners of your screen and then press enter after each corner has been selected (I recommend doing this with a simple rectangle frame or simply you entire projector screen).

An example of this is shown below:

![Homography Example](https://github.com/FARH4D/holomat-homography/blob/main/showcase/Screenshot%202024-06-25%20170313.png?raw=true)

The order of the corners you select is very important, follow this order when selecting the corners:
- Top-left
- Top-right
- Bottom-right
- Bottom-left

If you use this in any project you want to showcase I would appreciate credit, but I will not hunt you down for it 😄