FROM        ffmpeg:flask
COPY        main.py  /main.py
EXPOSE      9100
CMD         ["python", "/main.py"]