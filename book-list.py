book_list = [
    {"title": "Oligarchy", "pages": 220, "rating": 5},
    {"title": "Our Tragic Universe", "pages": 376, "rating": 8},
    {"title": "The Third Reich", "pages": 336, "rating": 5},
    {"title": "Nineteen Eighty-Four", "pages": 262, "rating": 9},
    {"title": "The Essex Serpent", "pages": 440, "rating": 7},
    {"title": "Sophie's World", "pages": 448, "rating": 10},
    {"title": "The Star Rover", "pages": 333, "rating": 9},
    {"title": "Walden; or, Life in the Woods", "pages": 247, "rating": 4},
    {"title": "Stoner", "pages": 286, "rating": 10},
]

pages_read = 0

for book in book_list:
  pages_read += book["pages"]
print(f"Vendy read {pages_read} pages.")

print("Books with 8+ rating: ")
for book in book_list:
  if book["rating"] >= 8:
    print(book["title"])