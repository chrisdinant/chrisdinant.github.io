Title: Music Video
Date: 2018-10-28
Slug: custom-pixels
headline: Custom pixel replacement for video with FFMPEG

Here's my children dancing around in the yard to my song.  
Have a watch:

<iframe width="560" height="315" src="https://www.youtube.com/embed/7qvhSWrXff4" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

This video was created by a custom python script that replaces pixels of low resolution images with jpegs of 20x20 pixels. Four different jpegs replace pixels of four grey intensity ranges. The python script uses ffmpeg to pipe individual frames of a video to the pixel replacement function and then pipe the new images into a new video file. In this video I use two jpeg sets, one with dots and lines and one with colored circles that look like hama beads (<http://www.hama.dk/welcome-to-a-color>...).  

Here's the import piece of code that extracts frames, replaces pixels and saves the frames back into a video:
```python
def extract_frames(rate = 6, outf = 'perl_light2.avi'):    
    command = [FFMPEG_BIN,
                '-i', 'IMG_1981.MOV',
                '-f', 'image2pipe',
                '-r', '%d' % rate,
                '-pix_fmt', 'rgb24',
                '-vcodec', 'rawvideo', '-']
    pipe = sp.Popen(command, stdout = sp.PIPE, bufsize=10**8)
    cmdstring = [FFMPEG_BIN,
                 '-y',
                 '-r', '%d' % rate,
                 '-f','image2pipe',
                 '-vcodec', 'mjpeg',
                 '-i', 'pipe:',
                 '-vcodec', codec,             
                 outf]
    p = sp.Popen(cmdstring, stdin=sp.PIPE)  

    for x in tqdm(range(55)):         
        raw_image = pipe.stdout.read(1280*720*3)
        # transform the byte read into a numpy array
        image =  np.frombuffer(raw_image, dtype='uint8')
        image = image.reshape((1280,720,3))    
        # throw away the data in the pipe's buffer.
        pipe.stdout.flush()
        image = rgb2gray(image)        
        ori = Image.fromarray(image)
        #crop = ori.crop((260,530,460,730))
        small = ori.resize((72,128))
        # morph the first couple of frames from noise to the first image
        if x == 0:            
            first_frame = np.random.rand(128,72)*255
            inc = (np.array(small) - first_frame)/30        
            for i in range(30):
                first_frame = first_frame + inc
                frame = Image.fromarray(first_frame)
                frame = perlize(frame, board)
                p.stdin.write(frame.tobytes('jpeg', 'RGB'))              
        frame = perlize(small, board)        
        frame = frame.tobytes('jpeg','RGB')
        p.stdin.write(frame)

    p.stdin.close()
```
&#916;9
