package main

import (
	"net/http"
	"flag"
	"fmt"
	"github.com/markbates/pkger"
)

func main() {
	port := flag.Int("port", 3000, "exposed port for the LibreLingo server")
	bind := flag.String("bind", "127.0.0.1", "bind address for the LibreLingo server")
	flag.Parse()

	addr := fmt.Sprintf("%s:%d", *bind, *port)
	dir := http.FileServer(pkger.Dir("/static"))

	fmt.Printf("Running on: %s", addr)
	http.ListenAndServe(addr, dir)
}
