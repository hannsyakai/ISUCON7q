GOPATH := ${PWD}
export GOPATH

build:
	GOOS=linux GOARCH=amd64 go build -v -ldflags "-X main.imageFetchServer=192.168.101.2" -o isubata1 isubata
	GOOS=linux GOARCH=amd64 go build -v -ldflags "-X main.imageFetchServer=192.168.101.1" -o isubata2 isubata

vet:
	go vet ./src/isubata/...

deploy:
	ssh isucon@163.43.29.171 "sudo systemctl stop isubata.golang"
	ssh isucon@59.106.209.11 "sudo systemctl stop isubata.golang"
	scp ./isubata1 isucon@163.43.29.171:/home/isucon/isubata/webapp/go/isubata
	scp ./isubata2 isucon@59.106.209.11:/home/isucon/isubata/webapp/go/isubata
	ssh isucon@163.43.29.171 "sudo systemctl start isubata.golang"
	ssh isucon@59.106.209.11 "sudo systemctl start isubata.golang"
	curl 163.43.29.171/initialize
	curl 59.106.209.11/initialize
