
version=6
image_tag="ffmpeg:gif-$(version)"

debug:
	@python main.py

test:
	@docker run -p 9100:9100 --name ffmpeg-gif ffmpeg:gif

clean:
	@echo ">>> clean" && \
	ls | grep pyc | xargs -I {} unlink {} && \
	rm -rf *.mp4 *.gif

build_ffmpeg:
	@echo ">>> build FFMPEG" && \
	docker build -f ffmpeg.Dockerfile -t ffmpeg .

build_flask: build_ffmpeg
	@echo ">>> build FLASK" && \
	docker build -f flask.Dockerfile -t ffmpeg:flask .

build: build_flask
	@echo ">>> build MP42GIF" && \
	docker build -t $(image_tag) . && \
	sed -i -e "s/verstr:.*/verstr: v$(version)/" dora.yaml -e "s/image:.*/image: $(image_tag)/" dora.yaml

push: build
	@~/bin/qdoractl push $(image_tag)

release: push
	@~/bin/qdoractl release -d --config .