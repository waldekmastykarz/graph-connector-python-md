import frontmatter
import os
from urllib.parse import urljoin
from msgraph.generated.models.external_connectors.external_item import ExternalItem

def _extract():
  base_url = "https://blog.mastykarz.nl"
  folder_path = "content"

  for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if not os.path.isfile(file_path) and (filename.endswith(".markdown") or filename.endswith(".md")):
        return
    
    with open(file_path, "r") as file:
      post = frontmatter.load(file)
      post.url = urljoin(base_url, post["slug"])
      post.image = urljoin(base_url, post["image"])
      yield post

def _transform(content) -> ExternalItem:
  for post in content:
    yield ExternalItem(
      
    ) {
      "title": post["title"],
      "excerpt": post["excerpt"],
      "imageUrl": post["image"],
      "url": post["url"],
      "date": post["date"],
      "tags": post["tags"]
    }

async def _load():
  pass

async def load_content():
  content = _extract()
  transformed = _transform(content)
  await _load(transformed)
