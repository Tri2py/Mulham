import http.server
import socketserver
import os

PORT = 8080

class VercelHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Enable CORS for local testing
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

    def do_GET(self):
        # Strip query params
        path_only = self.path.split('?')[0]
        
        # Root or index.html -> /home
        if path_only == '/' or path_only == '/index.html' or path_only == '/index':
            self.send_response(308)
            self.send_header('Location', '/home')
            self.end_headers()
            return
        
        # Legacy contacts.html -> /contact
        if path_only == '/contacts.html' or path_only == '/contacts':
            self.send_response(308)
            self.send_header('Location', '/contact')
            self.end_headers()
            return

        # cleanUrls: if path doesn't have an extension and doesn't exist directly, check for .html
        local_path = path_only.lstrip('/')
        if local_path and not os.path.exists(local_path) and '.' not in local_path:
            possible_html = local_path + '.html'
            if os.path.exists(possible_html):
                self.path = '/' + possible_html
        
        return super().do_GET()

class ThreadedHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True
    allow_reuse_address = True

if __name__ == '__main__':
    with ThreadedHTTPServer(('0.0.0.0', PORT), VercelHandler) as httpd:
        print(f'Threaded Vercel-simulation server running at http://localhost:{PORT} and http://127.0.0.1:{PORT}')
        httpd.serve_forever()
