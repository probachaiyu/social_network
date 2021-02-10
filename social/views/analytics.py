from rest_framework.generics import ListAPIView

from social.models import PostLike, User
from social.serializers.user import AnaliticSerializer, UserSerializer
from social.serializers.validation import DateSerializer


class AnalyticsViewSet(ListAPIView):
    serializer_class = AnaliticSerializer

    def get_queryset(self):
        query_serializer = DateSerializer(data=self.request.query_params)
        query_serializer.is_valid(raise_exception=True)
        date_from = query_serializer.data.get('date_from')
        date_to = query_serializer.data.get('date_to')
        user_id_field = "'All' as user_id"
        post_id_field = "'All' as post_id"
        group_by = ''
        query = self._get_aggregation(date_from, date_to, group_by, post_id_field, query_serializer, user_id_field)
        return query

    def _get_aggregation(self, date_from, date_to, group_by, post_id_field, query_serializer, user_id_field):
        aggregate_by = query_serializer.data.get('aggregate_by')
        if aggregate_by:
            id_field = f'{aggregate_by}_id'
            group_by = f'GROUP BY {id_field}'
            post_id_field = id_field if id_field in post_id_field else post_id_field
            user_id_field = id_field if id_field in user_id_field else user_id_field
        query = PostLike.objects.raw(
            f"""SELECT 1 as id, {user_id_field}, {post_id_field}, count (id)  as likes_count FROM post_like WHERE (created_at BETWEEN '{date_from}' AND '{date_to}') {group_by}""")
        return query


class UserActivityViewSet(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
