# получение номер произведения из адресной сроки
class CurrentTitle_id:
    requires_context = True

    def __call__(self, serializer_field):
        return serializer_field.context['request'].__dict__['parser_context']['kwargs']['title_id']


# получение номера рецензии из адресной строки
class CurrentReview_id:
    requires_context = True

    def __call__(self, serializer_field):
        return serializer_field.context['request'].__dict__['parser_context']['kwargs']['review_id']