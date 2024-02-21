# server.py

#Ahmad Mashal
#Activity 3 
# Date completed Feb 20th 



from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from database import Database

db = Database()

class RequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        if self.path == '/notes':
            self._set_headers()
            notes = db.read_notes()
            self.wfile.write(json.dumps(notes).encode())
        elif self.path.startswith('/notes/'):
            note_id = int(self.path.split('/')[-1])
            note = db.read_note(note_id)
            if note:
                self._set_headers()
                self.wfile.write(json.dumps(note).encode())
            else:
                self._set_headers(404)
                self.wfile.write(json.dumps({'error': 'Note not found'}).encode())
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({'error': 'Endpoint not found'}).encode())

    def do_POST(self):
        if self.path == '/notes':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            post_data_dict = json.loads(post_data)
            title = post_data_dict.get('title')
            content = post_data_dict.get('content')
            if title and content:
                note_id = db.create_note(title, content)
                self._set_headers(201)
                self.wfile.write(json.dumps({'id': note_id}).encode())
            else:
                self._set_headers(400)
                self.wfile.write(json.dumps({'error': 'Title and content are required'}).encode())
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({'error': 'Endpoint not found'}).encode())

    def do_PUT(self):
        if self.path.startswith('/notes/'):
            note_id = int(self.path.split('/')[-1])
            content_length = int(self.headers['Content-Length'])
            put_data = self.rfile.read(content_length).decode('utf-8')
            put_data_dict = json.loads(put_data)
            title = put_data_dict.get('title')
            content = put_data_dict.get('content')
            if title and content:
                db.update_note(note_id, title, content)
                self._set_headers()
                self.wfile.write(json.dumps({'message': 'Note updated successfully'}).encode())
            else:
                self._set_headers(400)
                self.wfile.write(json.dumps({'error': 'Title and content are required'}).encode())
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({'error': 'Endpoint not found'}).encode())

    def do_DELETE(self):
        if self.path.startswith('/notes/'):
            note_id = int(self.path.split('/')[-1])
            db.delete_note(note_id)
            self._set_headers()
            self.wfile.write(json.dumps({'message': 'Note deleted successfully'}).encode())
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({'error': 'Endpoint not found'}).encode())

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
