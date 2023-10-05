from msgraph.generated.models.external_connectors.activity_settings import ActivitySettings
from msgraph.generated.models.external_connectors.external_connection import ExternalConnection
from msgraph.generated.models.external_connectors.item_id_resolver import ItemIdResolver
from msgraph.generated.models.external_connectors.url_match_info import UrlMatchInfo

external_connection = ExternalConnection(
    id="waldekblogpython",
    name="Waldek Mastykarz (blog); Python",
    description="Tips and best practices for building applications on Microsoft 365 by Waldek Mastykarz - Microsoft 365 Cloud Developer Advocate",
    activity_settings=ActivitySettings(
        url_to_item_resolvers=[
            ItemIdResolver(
                odata_type="#microsoft.graph.externalConnectors.itemIdResolver",
                priority=1,
                item_id="{slug}",
                url_match_info=UrlMatchInfo(
                    base_urls=[
                        "https://blog.mastykarz.nl"
                    ],
                    url_pattern="/(?<slug>[^/]+)"
                )
            )
        ]
    )
)

_external_connection = {
    "connection": {
        # 3-32 characters
        "id": "waldekblog",
        "name": "Waldek Mastykarz (blog)",
        "description": "Tips and best practices for building applications on Microsoft 365 by Waldek Mastykarz - Microsoft 365 Cloud Developer Advocate",
        "activitySettings": {
            "urlToItemResolvers": [
                {
                    "@odata.type": "#microsoft.graph.externalConnectors.itemIdResolver",
                    "urlMatchInfo": {
                        "baseUrls": [
                            "https://blog.mastykarz.nl"
                        ],
                        "urlPattern": "/(?<slug>[^/]+)"
                    },
                    "itemId": "{slug}",
                    "priority": 1
                }
            ]
        },
        # https://learn.microsoft.com/graph/connecting-external-content-manage-schema
        "schema": [
            {
                "name": "title",
                "type": "String",
                "isQueryable": "true",
                "isSearchable": "true",
                "isRetrievable": "true",
                "labels": [
                    "title"
                ]
            },
            {
                "name": "excerpt",
                "type": "String",
                "isQueryable": "true",
                "isSearchable": "true",
                "isRetrievable": "true"
            },
            {
                "name": "imageUrl",
                "type": "String",
                "isRetrievable": "true"
            },
            {
                "name": "url",
                "type": "String",
                "isRetrievable": "true",
                "labels": [
                    "url"
                ]
            },
            {
                "name": "date",
                "type": "DateTime",
                "isQueryable": "true",
                "isRetrievable": "true",
                "isRefinable": "true",
                "labels": [
                    "lastModifiedDateTime"
                ]
            },
            {
                "name": "tags",
                "type": "StringCollection",
                "isQueryable": "true",
                "isRetrievable": "true",
                "isRefinable": "true"
            }
        ]
    }
}
