FROM        centos
WORKDIR     /

RUN         yum install -y epel-release && \
            rpm -Uvh http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-1.el7.nux.noarch.rpm && \
            yum install -y ffmpeg

RUN         yum install ffmpeg -y