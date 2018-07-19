FROM        ffmpeg
RUN         yum install python-pip wget -y
RUN         pip install flask