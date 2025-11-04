#!/usr/bin/env python3
from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import random

# Collection of motivational quotes
QUOTES = [
    {"content": "The only way to do great work is to love what you do.", "author": "Steve Jobs"},
    {"content": "Believe you can and you're halfway there.", "author": "Theodore Roosevelt"},
    {"content": "Success is not final, failure is not fatal: it is the courage to continue that counts.", "author": "Winston Churchill"},
    {"content": "The future belongs to those who believe in the beauty of their dreams.", "author": "Eleanor Roosevelt"},
    {"content": "It does not matter how slowly you go as long as you do not stop.", "author": "Confucius"},
    {"content": "Everything you've ever wanted is on the other side of fear.", "author": "George Addair"},
    {"content": "Believe in yourself. You are braver than you think, more talented than you know, and capable of more than you imagine.", "author": "Roy T. Bennett"},
    {"content": "I learned that courage was not the absence of fear, but the triumph over it.", "author": "Nelson Mandela"},
    {"content": "There is nothing impossible to they who will try.", "author": "Alexander the Great"},
    {"content": "The only impossible journey is the one you never begin.", "author": "Tony Robbins"},
    {"content": "In the middle of every difficulty lies opportunity.", "author": "Albert Einstein"},
    {"content": "Start where you are. Use what you have. Do what you can.", "author": "Arthur Ashe"},
    {"content": "The best time to plant a tree was 20 years ago. The second best time is now.", "author": "Chinese Proverb"},
    {"content": "Don't watch the clock; do what it does. Keep going.", "author": "Sam Levenson"},
    {"content": "You are never too old to set another goal or to dream a new dream.", "author": "C.S. Lewis"},
    {"content": "The way to get started is to quit talking and begin doing.", "author": "Walt Disney"},
    {"content": "Don't let yesterday take up too much of today.", "author": "Will Rogers"},
    {"content": "You learn more from failure than from success. Don't let it stop you.", "author": "Unknown"},
    {"content": "It's not whether you get knocked down, it's whether you get up.", "author": "Vince Lombardi"},
    {"content": "Failure will never overtake me if my determination to succeed is strong enough.", "author": "Og Mandino"},
    {"content": "We may encounter many defeats but we must not be defeated.", "author": "Maya Angelou"},
    {"content": "Knowing is not enough; we must apply. Wishing is not enough; we must do.", "author": "Johann Wolfgang Von Goethe"},
    {"content": "Imagine your life is perfect in every respect; what would it look like?", "author": "Brian Tracy"},
    {"content": "Whether you think you can or think you can't, you're right.", "author": "Henry Ford"},
    {"content": "Security is mostly a superstition. Life is either a daring adventure or nothing.", "author": "Helen Keller"}
]

class QuoteHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers and cache control
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def do_GET(self):
        if self.path == '/api/quote':
            try:
                # Select a random quote
                quote = random.choice(QUOTES)
                
                # Send successful response
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(quote).encode('utf-8'))
                
            except Exception as e:
                # Send error response
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                error_response = json.dumps({'error': str(e)})
                self.wfile.write(error_response.encode('utf-8'))
        else:
            # Serve static files
            super().do_GET()

if __name__ == '__main__':
    PORT = 5000
    server = HTTPServer(('0.0.0.0', PORT), QuoteHandler)
    print(f'Server running on port {PORT}')
    server.serve_forever()
