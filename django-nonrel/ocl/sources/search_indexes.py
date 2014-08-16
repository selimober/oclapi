from haystack import indexes
from oclapi.search_backends import SortField
from sources.models import Source

__author__ = 'misternando'


class SourceIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = SortField(model_attr='name', indexed=True, stored=True)
    full_name = indexes.CharField(model_attr='full_name', null=True, indexed=True, stored=True)
    source_type = SortField(model_attr='source_type', null=True, indexed=True, stored=True)
    last_update = indexes.DateTimeField(model_attr='updated_at', indexed=True, stored=True)
    num_stars = indexes.IntegerField(model_attr='num_stars', indexed=True, stored=True)

    def get_model(self):
        return Source



