import http.server
import socketserver
import os

PORT = 8080

class VercelHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Remove query strings for path resolution
        path_only = self.path.split('?')[0]
        
        # Native Vercel Redirects
        if path_only == '/' or path_only == '/index.html':
            self.send_response(308)
            self.send_header('Location', '/home')
            self.end_headers()
            return

        # cleanUrls logic: if it has no extension, try appending .html
        local_path = path_only[1:] # strip leading slash
        if local_path and not os.path.exists(local_path) and '.' not in local_path:
            possible_html = local_path + '.html'
            if os.path.exists(possible_html):
                self.path = '/' + possible_html

        return super().do_GET()

# Allow address reuse so we don't get "port already in use"
socketserver.TCPServer.allow_reuse_address = True

with socketserver.TCPServer(("", PORT), VercelHandler) as httpd:
    print(f"Vercel-simulating server running at http://localhost:{PORT}")
    httpd.serve_forever()
