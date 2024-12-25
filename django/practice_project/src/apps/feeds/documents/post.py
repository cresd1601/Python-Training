from django.conf import settings
from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl.registries import registry

# Models
from apps.feeds.models import Post, PostStatistics

# Name of the Elasticsearch index
INDEX = Index(settings.ELASTICSEARCH_INDEX_NAMES[__name__])

# See Elasticsearch Indices API reference for available settings
INDEX.settings(number_of_shards=1, number_of_replicas=1)


@INDEX.doc_type
@registry.register_document
class PostDocument(Document):
    id = fields.IntegerField(attr="id")
    title = fields.TextField(attr="title")
    author = fields.TextField(attr="author")
    likes_count = fields.IntegerField(attr="likes_count")
    comments_count = fields.IntegerField(attr="comments_count")
    location = fields.GeoPointField(attr="location")
    created = fields.DateField(attr="created")
    modified = fields.DateField(attr="modified")

    class Index:
        # Name of the Elasticsearch index
        name = "posts"

    class Django:
        # The model associated with this Document
        model = Post
        related_models = [PostStatistics]

    def get_instances_from_related(self, related_instance):
        if isinstance(related_instance, PostStatistics):
            return related_instance.post

    @classmethod
    def apply_search(cls, elastic_search, search):
        if search:
            elastic_search = elastic_search.query("match", title=search)

        return elastic_search

    @classmethod
    def apply_ordering(cls, elastic_search, order_by):
        if order_by:
            return elastic_search.sort({order_by: {"order": "desc"}})

        return elastic_search.sort({"modified": {"order": "desc"}})

    @classmethod
    def apply_distance_filtering(cls, elastic_search, latitude, longitude, distance):
        # Sort by distance if latitude, longitude, and distance are provided
        if all([latitude, longitude, distance]):
            return elastic_search.filter(
                {
                    "geo_distance": {
                        "location": {
                            "lat": float(latitude),
                            "lon": float(longitude),
                        },
                        "distance": distance,
                    }
                }
            )

        return elastic_search
