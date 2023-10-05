import datetime
import frontmatter
import os
from urllib.parse import urljoin
from msgraph.generated.models.external_connectors.access_type import AccessType
from msgraph.generated.models.external_connectors.acl import Acl
from msgraph.generated.models.external_connectors.acl_type import AclType
from msgraph.generated.models.external_connectors.external_activity import ExternalActivity
from msgraph.generated.models.external_connectors.external_activity_type import ExternalActivityType
from msgraph.generated.models.external_connectors.external_item import ExternalItem
from msgraph.generated.models.external_connectors.external_item_content import ExternalItemContent
from msgraph.generated.models.external_connectors.external_item_content_type import ExternalItemContentType
from msgraph.generated.models.external_connectors.identity import Identity
from msgraph.generated.models.external_connectors.identity_type import IdentityType
from msgraph.generated.models.external_connectors.properties import Properties
from typing import List

from connection_configuration import external_connection, user_id
from graph_service import graph_client

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
    # Date must be in the ISO 8601 format
    docDate=datetime.datetime.strptime(post["date"], "%Y-%m-%d %H:%M:%S")
    date=docDate.isoformat()
    yield ExternalItem(
      id=post["slug"],
      properties=Properties(
        additional_data=[
          ("title", post["title"]),
          ("excerpt", post["excerpt"]),
          ("imageUrl", post["image"]),
          ("url", post["url"]),
          ("date", date),
          ("tags@odata.type", "Collection(String)"),
          ("tags", post["tags"])
        ]
      ),
      content=ExternalItemContent(
        type=ExternalItemContentType.Text,
        value=post["content"]
      ),
      acl=[
        Acl(
          type=AclType.User,
          value="everyone",
          access_type=AccessType.Grant
        )
      ],
      activities=[
        ExternalActivity(
          odata_type="#microsoft.graph.externalConnectors.externalActivity",
          type=ExternalActivityType.Created,
          start_date_time=docDate,
          performed_by=Identity(
            type=IdentityType.User,
            id=user_id
          )
        )
      ]
    )

async def _load(content: List[ExternalItem]):
  for doc in content:
    try:
      print(f"Loading {doc.id}...", end="")
      await graph_client.external.connections.by_external_connection_id(
          external_connection.id
        ).items.by_external_item_id(doc.id).put(doc)
      print("DONE")
    except Exception as e:
      print(f"Failed to load {doc.id}: {e}")
      return

async def load_content():
  content = _extract()
  transformed = _transform(content)
  await _load(transformed)
