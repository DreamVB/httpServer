# A Very simple web server to serve statoc pages
# By Ben J a.k.a DreamVB
import servfunc
import os.path
import cfgread

from http.server import BaseHTTPRequestHandler, HTTPServer

class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        # Send response status code
        self.send_response(200)
        # Get home root
        root = cfgread.readVal("HOME_DIR")
        # Get the request line
        b = self.raw_requestline.decode("utf-8")
        # Split the line by the spaces
        items = b.split(" ")
        # Get the second item it should be the request page
        page = items[1].replace("/","\\")

        if page == "\\":
            page = cfgread.readVal("DEFAULT_PAGE")
        # Get the file ext
        file_ext = servfunc.getFileExt(page)
        # Get the full path to the page to serv
        full_file = servfunc.fixPath(root) + page
        # Get the file in question mimetype
        mime_type = cfgread.readVal(file_ext)
        # Make sure the full path filename is found
        if os.path.exists(full_file):
            # Send headers
            self.send_header('Content-type', mime_type)
            self.end_headers()
            self.wfile.write(servfunc.get_bytes_from_file(full_file))
        else:
            # Send 404 error page
            self.send_header('Content-type',"text/html")
            self.wfile.write(servfunc.get_bytes_from_file("err_pages\\404.html"))
        return

def start_server():
    print('Starting Server...')
    # Load server config
    cfgread.loadCfg("server.cfg")
    server_address = ("", int(cfgread.readVal("PORT")))
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('Running Server...')
    # Keep the server running
    httpd.serve_forever()

if __name__ == '__main__':
    # Start the web server
    start_server()
