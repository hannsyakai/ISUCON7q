GOPATH := ${PWD}
export GOPATH

build:
	GOOS=linux GOARCH=amd64 go build -v isubata

build-my:
	go build -o myapp -v isubata
vet:
	go vet ./src/isubata/...

deploy:
	rsync -av isubata isucon@163.43.29.171:/home/isucon/isubata/webapp/go/isubata
	rsync -av isubata isucon@59.106.209.11:/home/isucon/isubata/webapp/go/isubata